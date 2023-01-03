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

from marienbad.generator import checkCombination


def findSolution(situation: tuple) -> (tuple or bool):
	'''Retourne UNE des solutions possible à cette situation'''
	'''Usage : findSolution(situation: tuple)'''
	'''Retourne False si pas de solution, ou une solution sous forme de tuple.'''
	'''Nécessite le module marienbad.generator pour fonctionner.'''
	# Si la situation est gagnante, pas de solutions.
	if checkCombination(situation) == True:
		return False
	# Pour chaque tas on enlève tour à tour un jetons à la fois, et on teste.
	for tas in range(len(situation)):
		s = list(situation)
		while s[tas] > 0 :
			s[tas] -= 1
			# Si la combinaison est gagnante, on la propose.
			if checkCombination(s) == True:
				return tuple(s)
	return False
