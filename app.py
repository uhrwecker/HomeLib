import lib.library as library
import appJar as appjar
import os

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
		app.addMenuItem('File', 'Save', func=self.__save_library, shortcut='Control-s')
		app.addMenuItem('File', 'Load', func=self.__load_library, shortcut='Control-o')
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
		self.root.setGuiPadding(5, 5)

		self.root.addLabel('labl', 'Add Entry:', row=0, column=0, colspan=6)
		self.root.addHorizontalSeparator(row=1, column=0, colspan=6)
		
		self.root.addLabelEntry('Title: \t', row=2, column=0, colspan=6)
		self.root.addLabelEntry('Author: \t', row=3, column=0, colspan=6)
		dates = list()
		for i in range(1900, 2019):
			dates.append(i)
		self.root.addLabelSpinBox('Date: \t', dates, row=4, column=0, colspan=6)
		self.root.addLabelEntry('Owner: \t', row=5, column=0, colspan=6)
		self.root.addLabelNumericEntry('Pages: \t', row=6, column=0, colspan=6)
		self.root.addLabelEntry('Genre: \t', row=7, column=0, colspan=6)
		self.root.addLabelEntry('Language:', row=8, column=0, colspan=6)
		self.root.addLabelEntry('Publisher:', row=9, column=0, colspan=6)
		self.root.addLabelNumericEntry('Price: \t', row=10, column=0, colspan=6)	

		self.root.addHorizontalSeparator(row=11, column=0, colspan=6)	
		
		self.root.setSticky('')
		self.root.addButton('Add', self.__add_entry, row=12, column=0, colspan=1)
		self.root.addButton('Exit', self.__hide_addEntry, row=12, column=5, colspan=1)
		self.root.showSubWindow('Add Entry')
		self.root.stopSubWindow()

	def __add_entry(self):
		entry_dict = dict()
		entry_dict['title'] = self.root.getEntry('Title: \t')
		entry_dict['author'] = self.root.getEntry('Author: \t')
		entry_dict['owner'] = self.root.getEntry('Owner: \t')
		entry_dict['pages'] = self.root.getEntry('Pages: \t')
		entry_dict['language'] = self.root.getEntry('Language:')
		entry_dict['publisher'] = self.root.getEntry('Publisher:')
		entry_dict['price'] = self.root.getEntry('Price: \t')
		entry_dict['date'] = self.root.getSpinBox('Date: \t')
		genre = []
		for item in self.root.getEntry('Genre: \t').split(', '):
			genre.append(item)
		entry_dict['genre'] = genre
		
		self.lib.add_entry(entry_dict)
		if not self.root.questionBox('Added Entry', 'Succesfully added entry to library! Want to add another entry?'):
			self.root.hideSubWindow('Add Entry')
		self.root.info('Added Entry with title {}'.format(entry_dict['title']))

	def __load_library(self):
		current_path = os.getcwd()
		fp = self.root.openBox(title='Load library ...', dirName=current_path+'/doc/', fileTypes=[('lib_type', '*.json')])
		self.lib.load_lib(fp)
		self.root.info('Successfully Loaded Library File')

	def __save_library(self):
		current_path = os.getcwd()
		fp = self.root.saveBox(title='Save library ...', dirName=current_path+'/doc/', fileExt='.json', fileTypes=[('lib_type', '*.json')])
		self.lib.save_lib(fp)
		self.root.info('Successfully saved library file')

	def __check_stop(self):
		if self.root.yesNoBox('Confirm Exit', 'Are you sure you want to exit the application?'):
			self.root.stop()

	def __hide_addEntry(self):
		self.root.hideSubWindow('Add Entry')

App()
