import argparse
import apogee.align as align
import os.path
import tempfile
import shutil
import re


def apogee(fq1, fq2=None, ref_fasta=None, alt_fasta=None, bam=None,
           threads=1, mem=2, tmp_dir=None):
    '''Align RNA-seq data to a personalized genome.

    Arguments:
    - fq1: FASTQ for read1 (can be gzipped)
    - fq2: (optional) If paired-end, this is the FASTQ for read2
    - ref_fasta/alt_fasta: Paths to two fasta files, which one is specified
    as ref or alt doesn't matter.
    - bam: output BAM
    - threads: number of threads for alignment
    - tmp_dir: (optional) directory for temporary files
    '''
    
    if tmp_dir is None:
        tmp_dir = tempfile.mkdtemp(dir=os.path.dirname(bam))
    else:
        tmp_dir = tmp_dir
    
    outpref = re.sub('.bam$', '', os.path.basename(bam))

    ref_bam1 = os.path.join(tmp_dir, outpref + '_ref_1.bam')
    ref_bam2 = os.path.join(tmp_dir, outpref + '_ref_2.bam')
    ref_bam = os.path.join(tmp_dir, outpref + '_ref.bam')
    ref_nsorted = os.path.join(tmp_dir, outpref + '_ref_nsorted.bam')
    alt_bam1 = os.path.join(tmp_dir, outpref + '_alt_1.bam')
    alt_bam2 = os.path.join(tmp_dir, outpref + '_alt_2.bam')
    alt_bam = os.path.join(tmp_dir, outpref + '_alt.bam')
    alt_nsorted = os.path.join(tmp_dir, outpref + '_alt_nsorted.bam')
    final_nsorted = os.path.join(tmp_dir, outpref + '_nsorted.bam')

    # Align to reference
    align.olego_align(fq1, fastq2=fq2, index=ref_fasta, threads=threads, mem=mem,
                      out_bam1=ref_bam1, out_bam2=ref_bam2, out_bam=ref_bam)
    align.name_sort_bam(ref_bam, ref_nsorted, threads=threads, mem=mem)
    
    # Align to personal genome
    align.olego_align(fq1, fastq2=fq2, index=alt_fasta, threads=threads, mem=mem,
                      out_bam1=alt_bam1, out_bam2=alt_bam2, out_bam=alt_bam)
    align.name_sort_bam(alt_bam, alt_nsorted, threads=threads, mem=mem)
    
    # Merge the two sets of alignments
    align.merge_bams(ref_nsorted, alt_nsorted, final_nsorted, is_paired=fq2 is not None)
    
    # Position-sort and index the merged BAM
    align.position_sort_bam(final_nsorted, bam, threads=threads, mem=mem)

    if tmp_dir is None:
        shutil.rmtree(tmp_dir)
    

DESC = '''Align RNA-seq data to a personalized genome.

Each read (or read-pair in case of paired data) is aligned against two FASTAs (correponding
to two haplotypes or to a reference with and without an individual's variants). Then for
each read (or read-pair) the best alignment across the two FASTAs is chosen.

The order in which the two references are given (i.e. which one is specified as <ref_fasta>
and which one is specified as <alt_fasta>) does not matter.

Note that a lot of intermediate files are created. If <tmp_dir> is specified, all intermediate
files will be stored there, with a prefix matching the prefix of the output BAM. In this case,
it's up to you to delete that directory. If <tmp_dir> is not specified a temporary directory
will be created, in the same directory as the output BAM and then DELETED.
'''


def main():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('--fq1', required=True,
                        help='FASTQ file with all reads (for single-end) or read1 reads (for paired-end)')
    parser.add_argument('--fq2', help='FASTQ file with read2 reads')
    parser.add_argument('--ref_fasta', required=True, help='First FASTA against which to align')
    parser.add_argument('--alt_fasta', required=True, help='Second FASTA against which to align')
    parser.add_argument('--bam', required=True, help='Output BAM')
    parser.add_argument('--tmp_dir', help='Directory of intermediate files')
    parser.add_argument('--threads', default=1, type=int,
                        help='Number of threads for alignment [%(default)s]')
    parser.add_argument('--mem', default=2, type=int,
                        help='Mem (in Gb) to use for sorting [%(default)s]')
    args = parser.parse_args()
    
    apogee(**vars(args))


if __name__ == '__main__':
    main()
