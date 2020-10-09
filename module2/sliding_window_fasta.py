#!/usr/bin/env python3
# sliding_window_fasta.py

import re
import sys
from Bio import SeqIO

dengue.fasta = "https://www.ncbi.nlm.nih.gov/search/api/sequence/NC_001477.1/?report=fasta"
wget.download(dengue.fasta, '/~/Downloads/denguesequence.fasta')

def sliding_window(k, string):
    """Returns a list of all k-mers in the given string"""

    dna= []
    end= len(string) - k + 1
    for start in range(0, end):
        dna.append(string[start:start + k])

    return dna

def gc_content(dna):
    """Returns [0,1], the fraction of GC's in the given string"""

    dna= dna.lower()
    #Count the number of g's and c's 
    gc=0
    for nucleotide in dna:
        if nucleotide in ['g','c']:
            gc += 1
        return gc/len(dna)

if __name__ == "__main__":
    #Check to make sure there are at least two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: a kmer size and then a string")

    k = int(sys.argv[1])
    string = sys.argv[2]
    dna = sys.argv[1]
    result = gc_content(dna)
    for i in range(len(dna)):
        print("{}\t{.2}".format(dna,result))

