#!/usr/bin/env python3
.

import time
from mainMenu import *
from createMenu import *
from showMenu import *
from sellMenu import *
from persistence import *
from os import system

loadData(products)

while True:
	mainMenu()
	
	mainOption = int(input("Seleccione una opcion: "))
		
	if mainOption == "1":
		createMenu()
	elif mainOption == "2":
		showMenu()
	elif mainOption == "3":
		sellMenu()
	elif mainOption == "4":
		print()
		print("Gracias!")
		print()
	else:
		print()
		print("ERROR! OPCION INCORRECTA")
		time.sleep(1)
	
	if mainOption == "4":
		break

saveData(products)
