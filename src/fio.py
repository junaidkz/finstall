#creates a list of lists to store login username and password from a tab seperated file
class logInfo:
	data=[]
	def getData(self):
		with open('lgnin.inp','r') as fi:
			for line in fi:
				space=line.rstrip('\n')
				self.data.append(space.split('\t'));


if __name__=="__main__":
	n=logInfo()
	n.getData()

	for item1 in n.data:
    		print item1[0],item1[1]



	
