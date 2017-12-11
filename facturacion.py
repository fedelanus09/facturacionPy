#!/usr/bin/env python3

from createMenu import *
from mainMenu import *
from persistence import *
from searchMenu import *
from sellMenu import *
from time import time

def menu():
	while True:
		mainMenu()
	
		mainOption = input("Seleccione una opcion: ")
		
		if mainOption == "1":
			create()
		elif mainOption == "2":
			search()
		elif mainOption == "3":
			sell()
		elif mainOption == "4":
			print()
			print("Gracias!")
			print()
			sleep(1)
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)
			
menu()
