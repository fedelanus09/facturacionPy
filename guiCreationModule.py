from persistence import *

def addItem(products, productNameEntry, quantityEntry, priceEntry):
	item = {"productName": productNameEntry.get(), \
		"quantity":int(quantityEntry.get()), "price":int(priceEntry.get())}
	
	products.append(item)
