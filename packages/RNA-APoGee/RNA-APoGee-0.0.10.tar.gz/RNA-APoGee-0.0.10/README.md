# RNA-APoGee

RNA-APoGee (RNA Alignment to Personal Genomes) is a package to align RNA-seq data while
minimizing reference biases. It can also be used to align RNA-seq data to haplotype resolved variants.
Currently, RNA-APoGee relies on the Olego aligner, although
other aligners could be used instead.

## Pre-requisites:
- RNA-APoGee has only been tested on Linux and requires Python 3.
- [Olego](https://zhanglab.c2b2.columbia.edu/index.php/OLego_Documentation) must be installed and on your PATH.
- [samtools](http://samtools.sourceforge.net/)

## Installation
```pip install RNA-APoGee```

## Command line utilities
Alignment involves two steps:
1. Generating a "personalized" genome that has the variants of the
individual embedded into the reference genome.
2. Aligning against the reference and the personal genome (or against two haplotypes) and then merging
the two sets of alignment to pick the best alignment for each read.

### Generating a personal genome

`create_genomes` creates versions of an input FASTA with sample-specific SNVs replacing
reference bases.

If you have phased variants, you can create two 
VCFs corresponding to the variants of each haplotype and then create two versions of
the reference by calling `create_genomes` twice, once for each haplotype
(unfortunately currently this script ignores the phasing of the variants.)

```
create_genomes --fasta FASTA
               --vcf VCF
               --outdir OUTDIR
               [--samples SAMPLES]
               [--min_gq MIN_GQ]
               [--chunk CHUNK]

  --fasta FASTA      FASTA file that will be used as the base for generating
                     personal genomes. For each sample in the input VCF, an
                     individual genome will be created by substituting the
                     sample's SNVs into this base FASTA. SNVs will be
                     considered only if the FILTER field is PASS, and the
                     genotype quality is greater than <min_gq>.

  --vcf VCF          VCF with variant calls. Can have multiple samples.

  --outdir OUTDIR    Personal genome for sample <sample> will be in
                     <outdir>/<sample>.fa

  --samples SAMPLES  (Optional) Comma separated list of samples from the input VCF. If
                     provided, only the personal genomes for these samples
                     will be created, otherwise personal genomes for all
                     samples in the input VCF will be created.

  --min_gq MIN_GQ    (Optional) Minimum genotype quality to consider a variant

  --chunk CHUNK      (Optional) How many bases to keep in memory. Reduce if running OOM.
```

### Aligning against the reference and the personal genome

`apogee` aligns RNA-seq data to a personalized genome. Each read (or read-pair in case
of paired data) is aligned against two FASTAs (correponding to two haplotypes
or to a reference with and without an individual's variants). Then for each
read (or read-pair) the best alignment across the two FASTAs is chosen. The
order in which the two references are given (i.e. which one is specified as
`ref_fasta` and which one is specified as `alt_fasta`) does not matter. Note
that a lot of intermediate files are created. If `tmp_dir` is specified, all
intermediate files will be stored there, with a prefix matching the prefix of
the output BAM. In this case, it's up to you to delete that directory. If
`tmp_dir` is not specified a temporary directory will be created, in the same
directory as the output BAM and then deleted (so all intermediate files will be lost).

```
apogee --fq1 FQ1
       --ref_fasta REF_FASTA
       --alt_fasta ALT_FASTA
       --bam BAM
       [--fq2 FQ2]
       [--tmp_dir TMP_DIR]

  --fq1 FQ1              FASTQ file with all reads (for single-end) or read1
                         reads (for paired-end)
  --fq2 FQ2              (Optional) FASTQ file with read2 reads
  --ref_fasta REF_FASTA
                         First FASTA against which to align
  --alt_fasta ALT_FASTA
                         Second FASTA against which to align
  --bam BAM              Output BAM
  --tmp_dir TMP_DIR      (Optional) Directory of intermediate files
  --threads THREADS      (Optional) Number of threads for alignment [1]
```