from os import system
from time import time

def sellMenu():
	osystem('clear')
	
	print("Ventas")
	print("======")
	print()
	print(" 1) Realizar venta")
	print(" 2) Volver al menu anterior")
	print()

def sell():
	while True:
		sellMenu()
		
		sellOption = int(input("Seleccione una opcion: "))
		
		if sellOption == "1":
			sale()
			print()
			input("Presione ENTER para volver al menu...")
		elif sellOption == "2":
			invalid_input = False
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)
			
		return sell

def sale():
	system('clear')
	
	showAll()
	
	while True:
		saleOption = input("Nombre de producto: ")
		
		if saleOption == "Remera":
			tshirtSale()
		elif saleOption == "Jean":
			jeanSale()
		elif saleOption == "Musculosa":
			topSale()
		elif saleOption == "Short":
			shortSale()
		elif saleOption == "Camisa":
			shirtSale()
		else:
			print()
			print("ERROR! NOMBRE DE PRODUCTO INCORRECTO")
			sleep(1)
			sale()

		return sell
