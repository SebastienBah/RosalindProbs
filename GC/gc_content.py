#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""
Find GC content
"""
import numpy as np
from collections import OrderedDict
from pprint import pprint
import argparse

def count_cg(line):
    return (line.count("C")+line.count("G"))/len(line)*100

if __name__=="__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("file")
    args=parser.parse_args()

    dna_str={}

    # Read file into a list
    with open(args.file) as f:
        lines=f.readlines()

    # Print file
    #pprint(lines)

    # Populate dictionnary
    x=0
    latest=""
    while(x<len(lines)):
        # Start of fasta entry
        if lines[x].startswith(">Rosalind_"):
            latest=lines[x].replace(">","").strip()
            dna_str[latest]=""
        # Line contains DNA
        elif len(lines[x]):
            add=lines[x].strip()
            dna_str[latest]=dna_str[latest]+add
        x+=1

    gc_cont={}
    # Calculate GC content
    for k,v in dna_str.items():
        gc_cont[k]=count_cg(v)

    # Sort dictionnary
    sorted_dict=OrderedDict(sorted(gc_cont.items(),key=lambda x: x[1]))

    # Print out result
    #print(sorted_dict)

    # Print out result
    largest=sorted_dict.popitem()
    with open("answer.txt",'w') as f:
        f.write("{}\n{:2.7}".format(largest[0],largest[1]))
    #print(largest[0])
    #print(largest[1])
