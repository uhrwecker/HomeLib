import lib.library as library
from utils.utils import *
import appJar as appjar
import os

class App():
	def __init__(self):
		self.lib = library.Library()
		self.root = appjar.gui()
		self.main_window(self.root)
		self.window_add_entry()
		self.run()

	def main_window(self, app, fp='./doc/main.log'):
		app.setLogFile(fp)
		app.setSize(800, 800)
		app.setTitle('HomeLib - library software for home usage')
		app.setResizable(canResize=True)
		app.setLocation('CENTER')
		app.setFg('BLACK')
		app.setBg('LIGHT BLUE', tint=True)
		app.setGuiPadding(5, 5)
		app.setStretch('both')

		app.createMenu('File')
		app.addMenuItem('File', 'Save', func=self.__save_library, shortcut='Control-s')
		app.addMenuItem('File', 'Load', func=self.__load_library, shortcut='Control-o')
		app.addMenuSeparator('File')
		app.addMenuItem('File', 'Close', func=self.__check_stop, shortcut='Control-q')

		app.createMenu('Edit')
		app.addMenuItem('Edit', 'Add Entry', func=self.open_add_entry, shortcut='Control-d')
		app.addMenuItem('Edit', 'Delete selected item', func=self.delete_entry, shortcut='Control-x')

		app.createMenu('View')
		app.addSubMenu('View', 'Font size')
		app.addMenuItem('Font size', 'Increase font size', func=app.increaseFont, shortcut='Control-I')
		app.addMenuItem('Font size', 'Decrease font size', func=app.decreaseFont, shortcut='Control- L')

		# top left
		sort_keys = ['title', 'author', 'date', 'owner', 'pages', 'genre', 'language', 'publisher', 'price']
		app.startLabelFrame('Search & Select', row=0, column=0, colspan=2)
		app.addLabelOptionBox('Sort by: ', sort_keys, default=sort_keys[0], row=1, column=0, colspan=2)
		app.addButton('Sort', self.update_listbox, row=1, column=2)

		# top right
		search_keys = sort_keys
		search_keys.append('all')
		app.addLabelOptionBox('Search by: ', search_keys, default=search_keys[-1], row=0, column=3, colspan=2)
		app.addLabelEntry('Search: ', row=1, column=3, colspan=2)
		app.addButton('Go!', self.search_entry, row=1, column=6)
		app.stopLabelFrame()

		
		# bottom right
		app.startLabelFrame('Entry List', row=1, column=0, rowspan=8)
		app.setSticky('nesw')
		entry_list = self.__generate_entry_list(self.lib.get_lib())
		app.addListBox('Entries', entry_list, colspan=5)
		app.selectListItem('Entries', entry_list[0])
		app.setListBoxRows('Entries', 10)
		app.stopLabelFrame()
		#app.stopScrollPane()


		# bottom right#
		app.startLabelFrame('Entry', row=1, column=1, rowspan=8)
		app.setSticky('nw')
		func = self.show_entry
		app.enableEnter(func)
		self.__update_entry_frame(app, entry_list, update=False)
		app.addButton('Delete', self.delete_entry, row=9, column=3)
		app.stopLabelFrame()


	def run(self):
		self.root.go()

	def search_entry(self):
		search_opt = self.root.getOptionBox('Search by: ')
		search_str = self.root.getEntry('Search: ')
		lib_list = self.lib.search(search_str, by=search_opt)
		lib = dict()
		for item in lib_list:
			lib[item['id']] = item
		entry_list = self.__generate_entry_list(lib)
		self.root.updateListBox('Entries', entry_list)
		self.root.selectListItem('Entries', entry_list[0])
		self.__update_entry_frame(self.root, entry_list)
		self.show_entry()

	def delete_entry(self):
		util = Util()
		entry_string = self.root.getListBox('Entries')[0]
		entry_list = self.__generate_entry_list(self.lib.get_lib())
		index = entry_list.index(entry_string)	
		sorted_lib = util.sort_dict(self.lib.get_lib(), by=self.root.getOptionBox('Sort by: '))
		if self.root.questionBox('rm Entry', 'Warning: Are you sure you want to delete the entry {}?'.format(entry_string)):
			self.lib.remove(sorted_lib[index]['id'])
		self.update_listbox()
		
	
	def show_entry(self):
		entry_list = self.__generate_entry_list(self.lib.get_lib())
		self.__update_entry_frame(self.root, entry_list)
	
	def update_listbox(self):
		entry_list = self.__generate_entry_list(self.lib.get_lib())
		self.root.updateListBox('Entries', entry_list)
		self.root.selectListItem('Entries', entry_list[0])
		self.__update_entry_frame(self.root, entry_list)
		self.show_entry()

	def open_add_entry(self):
		self.root.showSubWindow('Add Entry')

	def window_add_entry(self):
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
		self.root.stopSubWindow()

	def __add_entry(self):
		entry_dict = dict()
		entry_dict['title'] = self.__entry_ex('Title: \t')
		entry_dict['author'] = self.__entry_ex('Author: \t')
		entry_dict['owner'] = self.__entry_ex('Owner: \t')
		entry_dict['pages'] = int(self.__entry_ex('Pages: \t', typ='int'))
		entry_dict['language'] = self.__entry_ex('Language:')
		entry_dict['publisher'] = self.__entry_ex('Publisher:')
		entry_dict['price'] = float(self.__entry_ex('Price: \t', typ='int'))
		entry_dict['date'] = int(self.root.getSpinBox('Date: \t'))
		genre = []
		for item in self.root.getEntry('Genre: \t').split(', '):
			genre.append(item)
		entry_dict['genre'] = genre
		
		self.lib.add_entry(entry_dict)
		if not self.root.questionBox('Added Entry', 'Succesfully added entry to library! Want to add another entry?'):
			entry_list = self.__generate_entry_list(self.lib.get_lib())
			self.root.updateListBox('Entries', entry_list)
			self.root.hideSubWindow('Add Entry')
			
		self.root.info('Added Entry with title {}'.format(entry_dict['title']))

	def __entry_ex(self, title, typ='str'):
		if self.root.getEntry(title) == '' and typ=='str':
			return('None')
		elif self.root.getEntry(title) == None and typ=='int':
			return(0)
		else:
			return(self.root.getEntry(title))
			

	def __update_entry_frame(self, app, lis, update=True):
		util = Util()
		index = lis.index(app.getListBox('Entries')[0])
		entry = util.sort_dict(self.lib.get_lib(), by=app.getOptionBox('Sort by: '))[index]
		if not update:
			app.addLabel('title', 'Title: \t \t {}'.format(entry['title']), row=0, column=0, colspan=3)
			app.addLabel('author', 'Author: \t \t {}'.format(entry['author']), row=1, column=0, colspan=3)
			app.addLabel('date', 'Date: \t \t {}'.format(entry['date']), row=2, column=0, colspan=3)
			app.addLabel('owner', 'Owner: \t \t {}'.format(entry['owner']), row=3, column=0, colspan=3)
			app.addLabel('pages', 'Pages: \t \t {}'.format(entry['pages']), row=4, column=0, colspan=3)
			app.addLabel('genre', 'Genre: \t \t {}'.format(entry['genre']), row=5, column=0, colspan=3)
			app.addLabel('language', 'Language: \t {}'.format(entry['language']), row=6, column=0, colspan=3)
			app.addLabel('publisher', 'Publisher: \t {}'.format(entry['publisher']), row=7, column=0, colspan=3)
			app.addLabel('price', 'Price: \t \t {}'.format(entry['price']), row=8, column=0, colspan=3)
		else:
			app.setLabel('title', 'Title: \t \t {}'.format(entry['title']))
			app.setLabel('author', 'Author: \t \t {}'.format(entry['author']))
			app.setLabel('date', 'Date: \t \t {}'.format(entry['date']))
			app.setLabel('owner', 'Owner: \t \t {}'.format(entry['owner']))
			app.setLabel('pages', 'Pages: \t \t {}'.format(entry['pages']))
			app.setLabel('genre', 'Genre: \t \t {}'.format(entry['genre']))
			app.setLabel('language', 'Language: \t {}'.format(entry['language']))
			app.setLabel('publisher', 'Publisher: \t {}'.format(entry['publisher']))
			app.setLabel('price', 'Price: \t \t {}'.format(entry['price']))
			
	def __generate_entry_list(self, libra):
		util = Util()
		sorted_lib = util.sort_dict(libra, by=self.root.getOptionBox('Sort by: '))
		ent_list = list()
		for item in sorted_lib:
			string = item['title'] + ' by ' + item['author'] + ', ' + str(item['date'])
			ent_list.append(string)
		return(ent_list)

	def __load_library(self):
		current_path = os.getcwd()
		fp = self.root.openBox(title='Load library ...', dirName=current_path+'/doc/', fileTypes=[('lib_type', '*.json')])
		if not type(fp) == str:
			return(0)
		else:
			self.lib.load_lib(fp)
			self.root.info('Successfully Loaded Library File')

	def __save_library(self):
		current_path = os.getcwd()
		fp = self.root.saveBox(title='Save library ...', dirName=current_path+'/doc/', fileExt='.json', fileTypes=[('lib_type', '*.json')])
		if not type(fp) == str:
			return(0)
		else:
			self.lib.save_lib(fp)
			self.root.info('Successfully saved library file')

	def __check_stop(self):
		if self.root.yesNoBox('Confirm Exit', 'Are you sure you want to exit the application?'):
			self.root.stop()

	def __hide_addEntry(self):
		self.root.hideSubWindow('Add Entry')
		self.update_listbox()

App()
