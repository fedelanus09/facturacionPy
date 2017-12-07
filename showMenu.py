def showMenu():
	print("       Lista de mercaderia")
	print("       ===== == ==========")
	print()
	print(" 1) Mostrar todos los productos")
	print(" 2) Volver al menu anterior")

def show(showMenu, showAll):

	while True:
		showMenu

		showOption = input("Elija una opcion: ")
		
		if showOption == "1"
			showAll()
			input("Presione ENTER para finalizar...")
		elif showOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)

def showAll():
	print("Lista de Productos")
	print("===== == =========")
	print()
	print("Cantidad | Producto  | Precio unit. $ |")
	print(inventary)
	print()
