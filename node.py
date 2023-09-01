class Node:
	def __init__(self,name,key,price,rating,address,tline,tstop):
		self.name = name
		self.key = key
		self.price = price
		self.rating = rating
		self.address = address
		self.tline = tline
		self.tstop = tstop
		self.name_lower = self.name.lower()

	def __str__(self):
		text = 'Restaurant Name: '
		text += self.name + '\n'
		text += 'Price: '
		text += int(self.price)*'$' + '\n'
		text += 'Rating: '
		text += self.rating + '\n'
		text += 'Address: '
		text += self.address + '\n'
		text += 'Closest Sation: '
		text += self.tline + ' line ' + self.tstop + ' station'
		text += '\n================================================='
		return text
