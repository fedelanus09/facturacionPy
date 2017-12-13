import time
from os import system
from persistence import saveData

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
			time.sleep(1)
			system('clear')
			addProduct()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		elif createOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)
		

def addProduct():
	print("INGRESO DE NUEVO PRODUCTO")
	print("======= == ===== ========")
	print()
	
	product = {}
	
	product["producto"] = input("Nombre de producto: ")
	product["cantidad"] = int(input("Cantidad: "))
	product["precio"] = int(input("Precio: "))
	
	inventory.append(product)
	
	saveData(inventory)
	
