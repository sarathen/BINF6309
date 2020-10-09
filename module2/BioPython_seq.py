#!/usr/bin/env python3
# Bio_Python_seq.py

from Bio.Seq import Seq
seq = Seq("aaaatgggggggggggccccgtt")
from Bio.SeqRecord import SeqRecord
seq_r = SeqRecord(seq, id="#12345", description = "example 1", alphabet = "generic dna")
seq_r
seq_r.id

SeqIO.write(seq_r, "BioPython_seq.gb","gb")

