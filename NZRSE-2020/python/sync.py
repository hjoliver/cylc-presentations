#!/usr/bin/env python

from doit import proc

def main():
	 print([proc(i) for i in range(3)])

if __name__ == "__main__":
	 main()
