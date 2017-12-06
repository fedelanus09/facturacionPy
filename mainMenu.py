import time

def main()
	choice = "0"
	
	while choice == "0"
		print("Menu Principal")
		print("==== =========")
		print("1) Realizar venta")
		print("2) Control de inventario")
		print("3) Salir")
	
	choice = int(input("Seleccionar una opcion: "))
	
	if choice == "1":
		sellMenu()
	elif choice == "2":
		inventoryMenu()
	elif choice == "3":
		print("Gracias")
		exitApp(products)
		time.sleep(1)
	else:
		
