#! /usr/bin/env python
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""

"""
import argparse
from functools import lru_cache

@lru_cache(40)
def rabbitRecurion(n,k):
    '''
    Calculates the number of rabbits after n months when a pair of adult rabbits produce k pairs.
    They become adults after 1 month.
    Recursion equation F(n)=F(n-1)+k*F(n-2)
    '''
    if n<3:
        return 1
    return rabbitRecurion(n-1,k)+k*rabbitRecurion(n-2,k)

if __name__=="__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("file")
    args=parser.parse_args()

    with open(args.file,'r') as f:
        line=f.readline()
    n,k=[int(x) for x in line.split(" ")]
    result= rabbitRecurion(n,k)

    with open("answer.txt", 'w') as f:
        f.write(str(result))

