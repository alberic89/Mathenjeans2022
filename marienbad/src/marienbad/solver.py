#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  solver.py
#
#  Copyright 2022 alberic89 <alberic89@gmx.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

version = "0.1"
import sys
from marienbad.generator import checkCombination


def findSolution(situation: tuple) -> (tuple or bool):
	"""Retourne UNE des solutions possible à cette situation"""
	"""Usage : findSolution(situation: tuple)"""
	"""Retourne False si pas de solution, ou une solution sous forme de tuple."""
	"""Nécessite le module marienbad.generator pour fonctionner."""
	# Si la situation est gagnante, pas de solutions.
	if checkCombination(situation) == True:
		return False
	# Pour chaque tas on enlève tour à tour un jetons à la fois, et on teste.
	for tas in range(len(situation)):
		s = list(situation)
		while s[tas] > 0:
			s[tas] -= 1
			# Si la combinaison est gagnante, on la propose.
			if checkCombination(s) == True:
				return tuple(s)
	return False


def findAllSolutions(situation: tuple) -> (tuple or bool):
	"""Retourne TOUTES les solutions possible à cette situation"""
	"""Usage : findAllSolutions(situation: tuple)"""
	"""Retourne False si pas de solution, ou les solutions sous forme de tuple de tuple."""
	"""Nécessite le module marienbad.generator pour fonctionner."""
	# Si la situation est gagnante, pas de solutions.
	if checkCombination(situation) == True:
		return False
	allsolutions = []
	# Pour chaque tas on enlève tour à tour un jetons à la fois, et on teste.
	for tas in range(len(situation)):
		s = list(situation)
		while s[tas] > 0:
			s[tas] -= 1
			# Si la combinaison est gagnante, on la propose.
			if checkCombination(s) == True:
				allsolutions.append(tuple(s))
	if allsolutions != []:
		return tuple(allsolutions)
	return False


def findArguments() -> list:
	arg = [False, False, None]
	if len(sys.argv) == 1:
		tmp = tuple(input("Entrez la situation :").split())
		arg[2] = tuple([int(i) for i in tmp])
		return arg
	if "--help" in sys.argv or "-h" in sys.argv:
		print(
			f"""Utilisation : {sys.argv[0]} [OPTIONS]... "C O M B I N A I S O N"
Trouve une ou plusieurs solutions à une situation du jeu de Marienbad.

Options :

|  -h,  --help     Affiche l'aide.
|  -a,  --all      Trouve toutes les solutions.
|  -o,  --one      Trouve une seule solution. Option par défaut.
|       --no-gui   Lance la version en ligne de commande.
|                  Par défaut, si une interface graphique
|                  est disponible, elle sera utilisée.
|                  Cette option force l'usage du terminal.
|  -v,  --version  Affiche le numéro de version.

Exemples :
  {sys.argv[0]} --all --no-gui "1 3 5 7"
  {sys.argv[0]} -v
  {sys.argv[0]} --one "55 41 87 98 66 355 4\""""
		)
		exit()
	elif "-v" in sys.argv or "--version" in sys.argv:
		print(version)
		exit()
	elif len(sys.argv) > 3:
		print("Trop d'arguments")
		raise ValueError("Trop d'arguments")
		exit()
	for i in range(1, len(sys.argv) - 1):
		if sys.argv[i] == "--no-gui":
			arg[0] = True
		elif sys.argv[i] == "-a" or sys.argv[i] == "--all":
			arg[1] = True
		elif sys.argv[i] == "-o" or sys.argv[i] == "--one":
			arg[1] = False
		else:
			print("Ho ho ! Entrée illégale !")
			raise ValueError("Entrée illégale !")
	try:
		arg[2] = tuple(sys.argv[len(sys.argv)].split())
	except:
		print(
			'Impossible d\'interpréter la combinaison.\n Utilisez le format : "1 36 559 7".'
		)
		raise ValueError(
			'Impossible d\'interpréter la combinaison.\n Utilisez le format : "1 36 559 7".'
		)
	return arg


def mainCLI(situation: tuple, allsolutions=False) -> None:
	if allsolutions:
		print(findAllSolutions(situation))
	else:
		print(findSolution(situation))


def main():
	args = findArguments()
	mainCLI(args[2], args[1])


if __name__ == "__main__":
	main()
