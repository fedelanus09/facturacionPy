from json import dump
from json import loads
from pathlib import Path

def saveData(products):
	with open("outfiel.json", "w") as fout:
		dump(products, fout)

def loadData():
	products = []

	outfile = Path("./outfile.json")
	
	if outfile.is_file():
		products = loads(open("outfile.json").read())
		
		return products

def exitApp(products):
	saveData(products)
	quit()
