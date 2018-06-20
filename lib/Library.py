from Entry import Entry
import json
import os

class Library():
	
	def __init__(self, save_fp='./save.json', verbose=False):

		self.fp = save_fp
		self.verbose = verbose
		if not os.path.isfile(self.fp):
			self.init_save(self.fp)
	
		self.library = self.init_library_dict(self.fp)

	def add_entry(self, title, author, date, owner='', pages=0, 
		      genre=[], language='Deutsch', publisher='', price=0.):
		entry = Entry(title, author, date, owner, pages, genre, language, 
			      publisher, price)
		if self.verbose:
			self._print_entry(entry)
		ent_dict = entry.get_config()
		self.library[ent_dict['id']] = ent_dict
		return(0)

	def save_lib(self):
		fobj = open(self.fp, 'w')
		json.dump(self.library, fobj, indent=4, sort_keys=True)
		fobj.close()

	def get_lib(self):
		return(self.library)

	def edit_entry(self, entry_id, attr, change):
		self.library[entry_id][attr] = change
	
	def init_library_dict(self, fp):
		fobj = open(fp, 'r')
		lib = json.load(fobj)
		fobj.close()
		return(lib)		

	def init_save(self, fp):
		os.system('touch {}'.format(self.fp))
		
		fobj = open(fp, 'w')
		# create sample entry:
		entry = Entry('Harry Potter und der Halbblutprinz', 'Joanne K. Rowling', 2005)
		if self.verbose:
			self._print_entry(entry)
		write_dict = dict()
		write_dict[entry.get_config()['id']] = entry.get_config()
		json.dump(write_dict, fobj, indent=4, sort_keys=True)
		fobj.close()				

	def _print_entry(self, entry):
		e = entry.get_config()
		print('----------------------------------------------------------------------------')
		print('Added Entry:')
		print('{} by {}'.format(e['title'], e['author']))
		print('\t -- date: {}'.format(e['date']))
		print('\t -- owner: {}'.format(e['owner']))
		print('\t -- pages: {}'.format(e['pages']))
		print('\t -- language: {}'.format(e['language']))
		print('\t -- publisher: {}'.format(e['publisher']))
		print('\t -- price: {}'.format(e['price']))
		print('(referenced by {})'.format(e['id']))
		print('----------------------------------------------------------------------------')

	def _print_general_state(self):
		print('----------------------------------------------------------------------------')
		print('General state of library:')
		print('\t -- number of entries: {}'.format(len(self.library)))
		print('----------------------------------------------------------------------------')


a = Library(verbose=True)
a.add_entry('Codex Alera: Die Elementare von Calderon', 'Jim Butcher', 2013, owner='Jan-Menno',
			pages=605, publisher='blanvalet', price=9.99)
a.save_lib()
a._print_general_state()




