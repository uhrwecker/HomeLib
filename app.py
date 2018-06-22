import lib.library as library
import appJar as appjar

class App():
	def __init__(self):
		self.lib = library.Library()
		self.root = appjar.gui()
		self.main_window(self.root)
		self.run()

	def main_window(self, app, fp='./doc/main.log'):
		app.setLogFile(fp)
		app.setSize(800, 800)
		app.setTitle('HomeLib - library software for home usage')
		app.setResizable(canResize=True)
		app.setLocation('CENTER')
		app.setFg('WHITE')
		app.setBg('BLUE', tint=True)

		app.createMenu('File')
		app.addMenuItem('File', 'Save', func=self.lib.save_lib, shortcut='Control-s')
		app.addMenuSeparator('File')
		app.addMenuItem('File', 'Close', func=self.__check_stop, shortcut='Control-q')

		app.createMenu('Edit')
		app.addMenuItem('Edit', 'Add Entry', func=self.open_add_entry, shortcut='Control-d')

	def run(self):
		self.root.go()

	def open_add_entry(self):
		self.root.startSubWindow('Add Entry', modal=True)
		self.root.setSize(500, 700)
		self.root.setBg('LIGHT BLUE', tint=True)
		self.root.setFg('BLACK')
		self.root.setStretch('both')
		self.root.setSticky('nesw')

		self.root.addLabel('labl', 'Add Entry:', row=0, column=0, colspan=6)
		self.root.addHorizontalSeparator(row=1, column=0, colspan=6)
		
		self.root.addLabelEntry('Title:', row=2, column=0, colspan=6)
		self.root.addLabelEntry('Author:', row=3, column=0, colspan=6)
		dates = list()
		for i in range(1900, 2019):
			dates.append(i)
		self.root.addLabelSpinBox('Date:', dates, row=4, column=0, colspan=6)
		self.root.addLabelEntry('Owner:', row=5, column=0, colspan=2)
		self.root.addLabelEntry('Pages:', row=6, column=0, colspan=6)
		self.root.addLabelEntry('Language:', row=7, column=0, colspan=6)
		self.root.addLabelEntry('Publisher:', row=8, column=0, colspan=6)
		self.root.addLabelEntry('Price:', row=9, column=0, colspan=6)	

		self.root.addHorizontalSeparator(row=10, column=0, colspan=6)	
		
		self.root.addButton('Add', self.__add_entry, row=11, column=0)
		self.root.addButton('Exit', self.__hide_addEntry, row=11, column=5)
		self.root.showSubWindow('Add Entry')
		self.root.stopSubWindow()

	def __add_entry(self):
		entry_dict = dict()
		entry_dict['title'] = self.root.getEntry('Title:')
		entry_dict['author'] = self.root.getEntry('Author:')
		entry_dict['owner'] = self.root.getEntry('Owner:')
		entry_dict['pages'] = self.root.getEntry('Pages:')
		entry_dict['language'] = self.root.getEntry('Language:')
		entry_dict['publisher'] = self.root.getEntry('Publisher:')
		entry_dict['price'] = self.root.getEntry('Price:')
		entry_dict['date'] = self.root.getSpinBox('Date:')
		
		self.lib.add_entry(entry_dict)
		if self.root.infoBox('Added Entry', 'Succesfully added entry to library!'):
			self.root.hideSubWindow('Add Entry')
		print(len(self.lib.library_dict))

	def __check_stop(self):
		if self.root.yesNoBox('Confirm Exit', 'Are you sure you want to exit the application?'):
			self.root.stop()

	def __hide_addEntry(self):
		self.root.hideSubWindow('Add Entry')

App()
