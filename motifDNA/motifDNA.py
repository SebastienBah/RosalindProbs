#! /usr/bin/env python
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""
Finds all the starting position of a motif in a sequence of DNA (1 indexed)
"""
import argparse 

def index_motif(motif,dna):
    pos=[]
    loc=-1
    while True:
        loc=dna.find(motif,loc+1)
        if loc==-1:
            break
        pos.append(str(loc+1))
    return pos


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("file",help="File that contains the DNA string and the search motif.")
    args=parser.parse_args()

    with open(args.file,'r') as f:
        lines= f.readlines()
    dna=lines[0].strip()
    motif=lines[1].strip()
    
    indexes=index_motif(motif,dna)

    with open('answer.txt','w') as f:
        f.write(" ".join(indexes))

