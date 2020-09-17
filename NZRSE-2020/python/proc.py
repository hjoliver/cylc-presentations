#!/usr/bin/env python

from multiprocessing import Pool
from doit import proc

if __name__ == "__main__":
   p = Pool(3)
   p.map(proc, range(3))
   p.close()
   p.join()
