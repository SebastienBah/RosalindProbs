#! /usr/bin/env python
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""

"""
import argparse 

def cc(n,k):
    '''Modified combination equation `n` choose `k` where `k`<=2'''
    if n<k:
        return 0
    elif n==k:
        return 1
    elif k==1:
        return n
    total=1
    for x in range(n-k+1,n+1):
        total*=x
    return total/2

def number_choices(k,m,n):
    t=k+m+n
    return 2*t*(t-1)

def prob_1dom(k,m,n):
    '''Calc from no dom allele'''
    '''from either Aa*Aa or Aa*aa or aa*aa'''
    max_choices=number_choices(k,m,n)
    all_recessive=cc(m,2)+cc(m,1)*cc(n,1)*2+cc(n,2)*4
    return (max_choices-all_recessive)/max_choices



if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("file")
    args=parser.parse_args()

    with open(args.file,'r') as f:
        k,m,n=[int(x) for x in f.readline().split(" ")]

    print("Probability that at least one dominant allele is ",prob_1dom(k,m,n))
