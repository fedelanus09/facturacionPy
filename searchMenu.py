from os import system
from time import time

def searchMenu():
	system('clear')
	
	print("Lista de mercaderia")
	print("===== == ==========")
	print()
	print(" 1) Mostrar todos los productos")
	print(" 2) Volver al menu anterior")
	print()

def search():
	while True:
		seachMenu()

		searchOption = input("Elija una opcion: ")
		
		if searchOption == "1":
			showAll()
			print()
			input("Presione ENTER para volver al menu...")
		elif searchOption == "2":
			invalid_input = False
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)

def showAll():
	system('clear')
	
	print(" Lista de Productos")
	print(" ===== == =========")
	print()
	print(" Cantidad | Producto  | Precio unit. $ |")
	
	loadData()
	
	for products in inventory:
		print("    " + str(products["quantity"]) + " | " + products["product"] \
			+ "  |$" + str(products["price"]))
		
	return search
