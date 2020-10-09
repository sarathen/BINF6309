#!/usr/bin/env python3
# BioPython_seqio.py

from Bio.Seq import Seq
from Bio import SeqIO

reverse_seq = []
for original_seq in SeqIO.parse("/Users/Sara/Documents/yeast.fasta","fasta"):
    original_seq.reverse_complement()

with open('original_seq_reverse_complement.fasta','w') as f:
    f.write('\n'.join(reverse_seq))

