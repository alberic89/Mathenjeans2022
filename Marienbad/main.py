#!/usr/bin/env pypy3

from itertools import combinations_with_replacement

def generate(nbjetons=10,nbtas=10):
	number = list(range(1,nbjetons+1))
	for row in range(1,nbtas+1):
		temp = combinations_with_replacement(number, row)
		for i in list(temp):
			if isGood(i) : print(i)


def isGood(liste):
	ok = True
	liste = list(liste)
	maxlen = len(bin(max(liste))[2:])
	for i in range(len(liste)):
		liste[i]=bin(liste[i])[2:]
	l = tuple(liste)
	for i in range(1,maxlen+1):
		s = 0
		for obj in l :
			if i <= len(obj) :
				s += int(obj[-i])
		if s%2 != 0:
			ok = False
			break
	return ok

if __name__ == "__main__" :
	generate()