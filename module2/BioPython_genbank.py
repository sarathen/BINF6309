#!/usr/bin/env python3
# BioPython_genbank.py

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "then.sara@northeastern.edu"

seq_record = []
with Entrez.efetch(db="nucleotide", rettype="gbwithparts",retmode="text", id="515056") as handle:
    seq_record = SeqIO.read(handle, "gb")
print(seq_record.features)

with Entrez.efetch(db="nucleotide", rettype="gbwithparts",retmode="text", id="JO1673.1") as handle:
    seq_record = SeqIO.read(handle,"gb")
print(seq_record.features)

