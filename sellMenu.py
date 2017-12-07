def sellMenu():
	system("clear")
	
	print("    Ventas")
	print("    ======")
	print()
	print(" 1) Realizar venta")
	print(" 2) Volver al menu anterior")
	print()

def sell(sellMenu, sale):
	while True:
		sellMenu()
		
		sellOption = int(input("Seleccione una opcion: "))
		
		if sellOption == "1":
			sale()
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)
		
		if sellOption == "2"
			break

def sale(showAll):
	system("clear")
	
	print(showAll(inventory))
	
	while True:
		saleOption = input("Nombre de producto: ")
		
		
