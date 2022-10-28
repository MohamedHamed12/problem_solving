
import sys

from io import BytesIO, IOBase
import os


def solve():
    aa, bb = tuple(map(int, sys.stdin.readline().split()))
    if (aa+bb) % 2 == 0:
        print('Tonya')

    else:
        print('Burenka')


for i in range(int(input())):
    (solve())