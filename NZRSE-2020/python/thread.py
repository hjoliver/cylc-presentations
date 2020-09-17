#!/usr/bin/env python

from multiprocessing.pool import ThreadPool
from doit import proc

if __name__ == "__main__":
   p = ThreadPool(3)
   p.map(proc, range(3))
   p.close()
   p.join()
