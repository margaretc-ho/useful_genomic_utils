#!/usr/bin/env python

### author: Margaret Ho, margaret.ho@nih.gov
### last updated: Aug 15 2023

### This script takes fasta input and outputs an expanded fasta that has been ### split at gaps (indicated by any number of N's)
### Scaffolds with a gap are divided into separate entries, each subsequence has a subseq number appended to their fasta file
### Scaffolds without a gap are left alone

import argparse

def main():
	parser = argparse.ArgumentParser(description='Process an input fasta file, which will be split into fasta sequences if gaps (indicated by Ns) are detected')
	
	# Add an argument for the input file
	parser.add_argument('input_file', type=str, help='Path to the input fasta file')

	args = parser.parse_args()

	input_file = args.input_file
	#print(f"Processing input file: {input_file}")

	f = open(input_file)
	parsed_seqs = parse_fasta_file(f)
	f.close()
	return parsed_seqs

def parse_fasta_file(file_handle):
	"""Return a dict of {id:gene_seq} pairs based on the sequences in the input FASTA file
	input_file -- a file handle for an input fasta file
	"""
	parsed_seqs = {} #dictionary
	curr_seq_id = None 
	curr_seq = [] #list

	for line in file_handle:
		line = line.strip()

		if line.startswith(">"):
			if curr_seq_id is not None:
				parsed_seqs[curr_seq_id] = ''.join(curr_seq)

			curr_seq_id = line[1:] #store the part of the fasta line header except the ">"
			curr_seq = []
			continue

		curr_seq.append(line)

	#Add the final sequence to the dict
	parsed_seqs[curr_seq_id] = ''.join(curr_seq)
	return parsed_seqs

def split_sequence(sequence, delimiter='N'):
	sequences = sequence.split(delimiter)
	non_empty_sequences = [s for s in sequences if s]
	return non_empty_sequences

if __name__ == '__main__':
	parsed_seqs = main()
#print(parsed_seqs)
#for key in parsed_seqs:
#	print(key, parsed_seqs[key])

	for key in parsed_seqs:
#	print(len(split_sequence(parsed_seqs[key])))
		if len(split_sequence(parsed_seqs[key])) <= 1:
			print(">"+ key + "\n")
			print(parsed_seqs[key])
		else:
			for subseq_n in range(len(split_sequence(parsed_seqs[key]))):
				print(">" + key + "_subseq" + str(subseq_n+1))
				print(split_sequence(parsed_seqs[key])[subseq_n])
main()
