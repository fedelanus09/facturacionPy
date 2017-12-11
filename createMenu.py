from os import system
from time import time

def registerMenu():
	system('clear')
	
	print("Registro de mercaderia")
	print("======== == ==========")
	print()
	print(" 1) Ingresar nuevo producto")
	print(" 2) Volver al menu anterior")
	print()

def create():
	while True:
		registerMenu()
		
		createOption = input("Seleccione una opcion: ")
	
		if createOption == "1":
			newProduct()
			print()
			input("Presione ENTER para volver al menu...")
		elif createOption == "2":
			menu()
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)
		

def newProduct():
	system('clear')
	
	inventory = []

	for i in range(5):
		products = {}
		
		system('clear')
		print("INGRESO DE NUEVO PRODUCTO")
		print()
		products["quantity"] = int(input("Cantidad: "))
		products["product"] = input("Producto: ")
		products["price"] = int(input("Precio: "))
		
		inventory.append(products)

	saveData()
