from json import loads
from json import dump

def loadData():
	inventory = loads(open("outfile.json").read())
	
	for product in inventory:
		print("    " + product["cantidad"] + "    | " + product["producto"] \
			+ "  |     $" + product["precio"] + "    |")
		
def saveData():
	inventory = []
	
	product = {}
	
	product["producto"] = input("Nombre del producto: ")
	product["cantidad"] = input("Cantidad: ")
	product["precio"] = input("Precio unit. $: ")

	inventory.append(product)
	
	with open("outfile.json", "w") as fout:
		dump(inventory, fout)
