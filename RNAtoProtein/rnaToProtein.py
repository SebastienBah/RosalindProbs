#! /usr/bin/env python
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""

"""
import numpy as np
import pandas as pd
import re
import argparse 

table="""UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """

def parse_table(table):
    '''Returns a dictionnary with codons as keys and proteins as values.'''
    return dict(re.findall("(\w{3}) (\w+)",table))

def translate_rna2protein(rna,table):
    codons=[rna[n:n+3] for n in range(0,len(rna),3)]
    protein="".join([table[x] for x in codons])
    try:
        index_stop=protein.find('Stop')
        protein=protein[:index_stop]
    except ValueError:
        pass
    return protein

if __name__=="__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("file")
    args=parser.parse_args()

    with open(args.file, 'r') as f:
        rna=f.read().replace("\n","")

    codon_table=parse_table(table)
    protein=translate_rna2protein(rna,codon_table)
    #print(protein)
    with open('answer.txt', 'w') as f:
        f.write(protein)



