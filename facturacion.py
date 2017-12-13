#!/usr/bin/env python3

import time
from createMenu import *
from mainMenu import *
from searchMenu import *
from sellMenu import *

def menu():
	while True:
		mainMenu()
	
		mainOption = input("Seleccione una opcion: ")
		
		if mainOption == "1":
			time.sleep(1)
			create()
		elif mainOption == "2":
			time.sleep(1)
			search()
		elif mainOption == "3":
			time.sleep(1)
			sell()
		elif mainOption == "4":
			time.sleep(1)
			print()
			print("Gracias!")
			print()
			time.sleep(1)
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

menu()
