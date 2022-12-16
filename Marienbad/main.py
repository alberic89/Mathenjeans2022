#!/usr/bin/env pypy3

from itertools import combinations_with_replacement

def main():
	number = list(range(1,10))
	for row in range(1,100):
		temp = combinations_with_replacement(number, row)
		for i in list(temp):
			if isGood(i) : print(i)

def isGood(combinations):
	somme = 0
	for j in combinations :
		somme += int(bin(j)[2:])
	good = True
	for k in str(somme):
		if int(k)%2!=0 :
			good = False
			break
	return good

if __name__ == "__main__" :
	main()