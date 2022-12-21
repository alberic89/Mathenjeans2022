#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  generator.py
#
#  Copyright 2022 alberic89 <alberic89@gmx.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
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


import os, sys
from itertools import combinations_with_replacement
from tkinter import *
from tkinter import simpledialog


def generateTable(nbjetons: int, nbtas: int) -> tuple:
	result = []
	number = list(range(1, nbjetons + 1))
	for row in range(1, nbtas + 1):
		temp = combinations_with_replacement(number, row)
		for i in list(temp):
			if checkCombination(list(i)):
				result.append(i)
	return result


def checkCombination(liste: list) -> bool:
	ok = True
	maxlen = len(bin(max(liste))[2:])
	for i in range(len(liste)):
		liste[i] = bin(liste[i])[2:]
	combination = tuple(liste)
	for i in range(1, maxlen + 1):
		s = 0
		for obj in combination:
			if i <= len(obj):
				s += int(obj[-i])
		if s % 2 != 0:
			ok = False
			break
	return ok


def mainCLI(arg: tuple) -> None:
	if arg[1] == None:
		nb_jetons = int(input("Nombre maximal de jetons par tas : "))
	else:
		nb_jetons = arg[1]
	if arg[2] == None:
		nb_tas = int(input("Nombre maximal de tas : "))
	else:
		nb_tas = arg[2]
	out = generateTable(nb_jetons, nb_tas)
	for i in out:
		print(i)


def launchGUI(input_arg: tuple) -> None:
	ROOT = Tk()
	ROOT.title("Marienbad Generator")
	window_width = 660
	window_height = 495

	# get the screen dimension
	screen_width = ROOT.winfo_screenwidth()
	screen_height = ROOT.winfo_screenheight()

	# find the center point
	center_x = int(screen_width / 2 - window_width / 2)
	center_y = int(screen_height / 2 - window_height / 2)

	# set the position of the window to the center of the screen
	ROOT.geometry(
		str(window_width)
		+ "x"
		+ str(window_height)
		+ "+"
		+ str(center_x)
		+ "+"
		+ str(center_y)
	)
	jetons_lbl = Label(ROOT, text="Nombre de jetons maximum par tas:")
	jetons_spin = Spinbox(ROOT, from_=1.0, to=1000, increment=1.0)
	tas_lbl = Label(ROOT, text="Nombre de tas de jetons maximum :")
	tas_spin = Spinbox(ROOT, from_=1.0, to=1000, increment=1.0)
	button = Button(
		ROOT,
		text="Launch",
		command=lambda: [result.delete("1.0","end"),result.insert(
			"1.0", mainGUI((False, int(jetons_spin.get()), int(tas_spin.get())))
		)],
	)
	result = Text(ROOT)
	s = Scrollbar(ROOT, orient=VERTICAL, command=result.yview)
	result["yscrollcommand"] = s.set

	jetons_lbl.grid(column=0, row=0, sticky=(E), pady=5)
	jetons_spin.grid(column=1, row=0, sticky=(W))
	tas_lbl.grid(column=0, row=1, sticky=(E), pady=5)
	tas_spin.grid(column=1, row=1, sticky=(W))
	button.grid(column=0, row=2, columnspan=2, pady=5)
	result.grid(column=0, row=3, columnspan=2, sticky=(N, W, E, S))
	s.grid(column=3, row=3, sticky=(N, S))

	if input_arg[1] != None:
		jetons_spin.delete("0","end")
		jetons_spin.insert("0", input_arg[1])
	if input_arg[2] != None:
		tas_spin.delete("0","end")
		tas_spin.insert("0", input_arg[2])

	mainloop()


def mainGUI(arg: tuple) -> str:
	if arg[1] == None:
		nb_jetons = setInputJetons()
	else:
		nb_jetons = arg[1]
	if arg[2] == None:
		nb_tas = setInputTas()
	else:
		nb_tas = arg[2]
	out = generateTable(nb_jetons, nb_tas)
	msg = ""
	for i in out:
		msg += str(i) + "\n"
	return msg[:-1]


def findArguments() -> list:
	arg = [False, None, None]
	if "--help" in sys.argv or "-h" in sys.argv:
		print(
			f"""Utilisation : {sys.argv[0]} [OPTIONS]...
Génère toutes les combinaisons gagnante au jeu de Marienbad
avec une limite du nombre de jetons par tas et de tas.

Options :

  -h,   --help    Affiche l'aide.
  -jN             Utilise N jetons au maximum par tas.
  -tN             Utilise N tas de jetons au maximum.
	--no-gui  Lance la version en ligne de commande.
		  Par défaut, si une interface graphique
		  est disponible, elle sera utilisée.
		  Cette option force l'usage du terminal.

Exemples :
  {sys.argv[0]} -j5 -t7
  {sys.argv[0]} -t3 --no-gui -j12
  {sys.argv[0]} -j28"""
		)
		exit()
	elif len(sys.argv) > 4:
		print("Trop d'arguments")
		exit()
	for i in range(1, len(sys.argv)):
		if sys.argv[i] == "--no-gui":
			arg[0] = True
		elif sys.argv[i].find("-j") == 0:
			arg[1] = int(sys.argv[i][2:])
		elif sys.argv[i].find("-t") == 0:
			arg[2] = int(sys.argv[i][2:])
		else:
			print("Ho ho ! Entrée illégale !")
			exit()
	return arg


def main() -> None:
	input_arg = tuple(findArguments())
	if os.path.os.environ.get("DISPLAY") == None or input_arg[0] == True:
		mainCLI(input_arg)
	else:
		launchGUI(input_arg)


if __name__ == "__main__":
	main()
