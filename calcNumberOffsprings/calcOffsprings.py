#! /usr/bin/env python
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""

"""
import numpy as np
import pandas as pd
import argparse 

'''
Each couple has 2 offsprings.
  1. AA-AA
  2. AA-Aa
  3. AA-aa
  4. Aa-Aa
  5. Aa-aa
  6. aa-aa
'''

def calc_offsprings(cpl):
    return 2*(sum(cpl[:3]))+2*0.75*cpl[3]+cpl[4]

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('file')
    args=parser.parse_args()

    with open(args.file,'r') as f:
        couples=f.readline().split(" ")
    couples=[int(x) for x in couples]

    if len(couples)==6:
        print(calc_offsprings(couples))


