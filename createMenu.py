def createMenu():
	system("clear")
	
	print("   Registro de mercaderia")
	print("   ======== == ==========")
	print()
	print(" 1) Ingresar nuevo producto")
	print(" 2) Volver al menu anterior")
	print()

def create(createMenu, newProduct):
	while True:
		createMenu()
	
		createOption = input("Seleccione una opcion: ")
	
		if createOption == "1":
			newProduct()
		elif createOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			sleep(1)

def newProduct():
	system("clear")
	
	inventary = []
	
	for i in range(3):
		products = {}
		
		products["quantity"] = int(input("Cantidad: "))
		products["itemName"] = input("Nombre del producto: ")
		products["priceItem"] = int(input("Precio unit. $: "))
		
		inventary.append(products)
		
	print()
	print("Registro de producto exitosa...")
	sleep(1)
