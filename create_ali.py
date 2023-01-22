import os
from Bio import SeqIO
import argparse

from modeller import *

#create the parser
parser = argparse.ArgumentParser(
    description='create separate fasta and ali files from a fasta file with multiple sequences'
)
parser.add_argument('--fasta_in', type=str, help='The name of the input fasta file')
parser.add_argument('--fasta_out', type=str, help='The target directory of the fasta files')
parser.add_argument('--ali_out', type=str, help='The target directory of the ali files')

#Parse the argument
args = parser.parse_args()

with open(f"{args.fasta_in}", "r") as f_input:
    for rec in SeqIO.parse(f_input, "fasta"):
        ID = rec.id
        seq = rec.seq
        desc = rec.description
        with open(f"{args.fasta_out}/{ID}.fasta", "w") as f_output:
            f_output.write(">"+str(desc)+"\n"+str(seq))

files = [os.path.splitext(x)[0] for x in os.listdir(f"{args.fasta_out}/") if x.endswith(".fasta")]

for f in files:
    e = Environ()
    a = Alignment(e, file=f"{args.fasta_out}/{f}.fasta", alignment_format='FASTA')
    a.write(file=f"{args.ali_out}/{f}.ali", alignment_format='PIR')
