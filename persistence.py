from json import dump
from json import loads
from pathlib import Path

def saveData(inventory):
	with open("outfile.json", "w") as fout:
		dump(inventory, fout)

def loadData():
	inventary = []

	outfile = Path("./outfile.json")
	
	if outfile.is_file():
		inventary = loads(open("outfile.json").read())
		
		return inventory
