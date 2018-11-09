############################
# REMUS Easy Matrix v0.9.2 #
############################

########### Error codes and notes #############
#Error 0x000001 Static table is forcing more than acceptable columns. Request ignored
#Error 0x000002 Static table is forcing more than acceptable Rows. Request ignored
#Error 0xFFFFFF an unkown error has occured
#Connecting two nonexistant nodes will result in the request being ignored
#Connecting an existant node to a non-existant node will force creation of the nonexistant node, locally. If isBidirectional is Ture
#Connecting an existant node to a non-existant node or connecting a non-existant node to an existant will ignore request to connect nodes. If isBidirectional is False
#Request to connect a node to itself is ignored
#Killing Nodes may not completely destroy all of its refrences
#### Warning, Documentation does not exist for this module, you silly goose ####

## Lisencing Notice ##
# Officially licensed to https://remusmtf.com/ of REMUS by Kudzayi Mberi
# You may use this product for comercial or non-comercial purpouses.
# If use is for comecrical purpuses, You must also include the version number.
# If it is for non-comercial use, you must include this entire header.
# Copyright © 2018 by https://remusmtf.com/

class KMMatrix():

	def __init__(self, size, maxConnections, isDynamic = True):
		self.table = [[None for x in range(maxConnections + 1)] for y in range(size)]
		self.maxConnections = maxConnections
		self.isDynamic = isDynamic
		self.size = size

	def seeTable(self):
		print(self.table)

	def createNode(self, *args):
		for socket in args:
			for i in range(0, len(self.table)):
				if self.table[i][0] == None:
					self.table[i][0] = socket
					break
				elif None not in [i[0] for i in self.table] and self.isDynamic == True:
					self.table.append([None for x in range(self.maxConnections + 1)])
					self.table[len(self.table) - 1][0] = socket
					break
				elif None not in [i[0] for i in self.table] and self.isDynamic == False:
					print("Error code: 0x000002")
					break

	#Note to self, make sure to dissacosiate other connected nodes not just base nodes
	def killNode(self, *args):
		for socket in args:
			for i in range(0, len(self.table)):
				if self.table[i][0] == socket and self.isDynamic == True and len([i[0] for i in myMatrix.table]) <= self.size:
					self.table[i:(i+1)] = []
					self.table.append([None for x in range(self.maxConnections + 1)])
					break
				elif self.table[i][0] == socket and self.isDynamic == True and len([i[0] for i in myMatrix.table]) > self.size:
					del self.table[i]
					break


	def connectNode(self, socket, isBidirectional = True, *args):
		for plug in args:
			for i in range(0, len(self.table)):
				if self.table[i][0] == socket and (plug not in self.table[i]):
					for x in range(0, len(self.table[i])):
						if self.table[i][x] == None:
							self.table[i][x] = plug
							break
						elif (None not in self.table[i]) and self.isDynamic == True:
							self.table[i].append(plug)
							break
						elif (None not in self.table[i]) and self.isDynamic == False:
							print("Error code: 0x000001")
							break
					break
			if isBidirectional == True:
				for i in range(0, len(self.table)):
					if self.table[i][0] == plug and (socket not in self.table[i]):
						for x in range(0, len(self.table[i])):
							if self.table[i][x] == None:
								self.table[i][x] = socket
								break
							elif (None not in self.table[i]) and self.isDynamic == True:
								self.table[i].append(socket)
								break
							elif (None not in self.table[i]) and self.isDynamic == False:
								print("Error code: 0x000001")
								break
						break

	def disconnectNode(self, socket, plug, isBidirectional = True):
		for i in range(0, len(self.table)):
			if self.table[i][0] == socket and (plug in self.table[i]):
				for x in range(0, len(self.table[i])):
					if self.table[i][x] == plug and len(self.table[i]) <= (self.maxConnections + 1):
						self.table[i][x] = None
						self.table[i][x:(x+1)] = []
						self.table[i].append(None)
						break
					elif self.table[i][x] == plug and len(self.table[i]) > (self.maxConnections + 1) and self.isDynamic == True:
						del self.table[i][x]
						break
				break
		if isBidirectional == True:
			for i in range(0, len(self.table)):
				if self.table[i][0] == plug and (socket in self.table[i]):
					for x in range(0, len(self.table[i])):
						if self.table[i][x] == socket and len(self.table[i]) <= (self.maxConnections + 1):
							self.table[i][x] = None
							self.table[i][x:(x+1)] = []
							self.table[i].append(None)
							break
						elif self.table[i][x] == socket and len(self.table[i]) > (self.maxConnections + 1) and self.isDynamic == True:
							del self.table[i][x]
							break
					break





if __name__ == "__main__":
    #Example Code.
    myMatrix = KMMatrix(9, 3)
    myMatrix.seeTable()
    myMatrix.createNode("England", "France", "Germany", "Switzerland", "Italy", "South Africa", "Brazil", "USA")
    myMatrix.createNode("Canada")
    myMatrix.createNode("Heaven")
    myMatrix.connectNode("England", True, "Italy", "Switzerland", "Germany", "Canada")
    print()
    myMatrix.seeTable()
    print()
    myMatrix.killNode("Heaven", "Brazil", "Italy")
    print(len(myMatrix.table[0]))
    myMatrix.seeTable()
    print()
    print([i[0] for i in myMatrix.table])
