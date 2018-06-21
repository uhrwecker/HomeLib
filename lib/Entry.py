class Entry():
	
	def __init__(self, title='', author='', date=0, owner='', pages=0, 
		     genre=[], language='Deutsch', publisher='', price=0.):
		self.title = title
		self.author = author
		self.date = date
		self.owner = owner
		self.pages = pages
		self.genre = genre
		self.pages = pages
		self.language = language
		self.publisher = publisher
		self.price = price

		self.id = self.title[:5] + self.author[:5] + str(self.date)

	def get_config(self):
		cnfg = dict()
		cnfg['title'] = self.title
		cnfg['author'] = self.author
		cnfg['date'] = self.date
		cnfg['owner'] = self.owner
		cnfg['pages'] = self.pages
		cnfg['language'] = self.language
		cnfg['publisher'] = self.publisher
		cnfg['price'] = self.price
		cnfg['id'] = self.id
		
		return(cnfg)

	def set_attr(self, attr):
		self.title = attr['title']
		self.author = attr['author']
		self.date = attr['date']
		self.owner = attr['owner']
		self.pages = attr['pages']
		self.language = attr['language']
		self.publisher = attr['publisher']
		self.price = attr['price']

		self.id = self.title[:5] + self.author[:5] + str(self.date)
