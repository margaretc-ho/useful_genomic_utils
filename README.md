# useful_genomic_utils
Useful scripts for accomplishing genomic tasks

The **split_scaffolds_at_gaps.py** script takes a fasta file as input and outputs an expanded fasta that has been split at gaps (indicated by any number of N's)

Scaffolds containing a gap are divided into separate fasta entries. Each subsequence is labeled with the name of the scaffold and with a subseq number appended. Scaffolds without a gap are left alone.

Usage:

split_scaffolds_at_gaps.py input_fasta.fa > output_fasta.fa
