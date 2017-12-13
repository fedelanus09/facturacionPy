from json import loads
from json import dump

def loadData():
	inventory = loads(open("outfile.json").read())
	
	inventory = []
	
	len(inventory)
	
def saveData(inventory):
	with open("outfile.json", "w") as fout:
		dump(inventory, fout)
