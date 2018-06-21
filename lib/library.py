from lib.entry import Entry
import json
import os

class Library():
	
	def __init__(self, save_fp='./save.json', verbose=False):

		self.fp = save_fp
		self.verbose = verbose
		if not os.path.isfile(self.fp):
			self.init_save(self.fp)
	
		self.library_dict = self.init_library_dict(self.fp)
		self.library_obj = self.init_library_obj(self.library_dict)

	def add_entry(self, title, author, date, owner='', pages=0, 
		      genre=[], language='Deutsch', publisher='', price=0.):
		entry = Entry(title, author, date, owner, pages, genre, language, 
			      publisher, price)
		if self.verbose:
			self._print_entry(entry)
		ent_dict = entry.get_config()
		self.library_dict[ent_dict['id']] = ent_dict
		self.library_obj[ent_dict['id']] = entry
		return(0)

	def edit_entry(self, entry_id, attr, change):
		self.library_dict[entry_id][attr] = change
		self.library_obj[entry_id].set_attr(self.library_dict[entry_dict])
	
	def remove(entry_id):
		del self.library_dict[entry_id], self.library_obj[entry_id]

	def save_lib(self):
		fobj = open(self.fp, 'w')
		json.dump(self.library_dict, fobj, indent=4, sort_keys=True)
		fobj.close()

	def search(self, search, by='all'):
		all_states = list()
		for entry_id in self.library_dict:
			if by == 'all':
				for attr in self.library_dict[entry_id]:
					if str(search) in str(self.library_dict[entry_id][attr]):
						all_states.append((entry_id, attr, self.library_obj[entry_id]))
						
			else:
				if str(search) in str(self.library[entry_id][by]):
						all_states.append((entry_id, by, self.library_obj[entry_id]))
			
		if self.verbose:
			for item in all_states:
				print('Following entry found containing {} in {}:'.format(search, item[1]))
				self._print_entry(item[-1])

		return(all_states)

	def get_lib(self):
		return(self.library_obj)
	
	def init_library_dict(self, fp):
		fobj = open(fp, 'r')
		lib = json.load(fobj)
		fobj.close()
		return(lib)	

	def init_library_obj(self, lib):
		dic = dict()
		for ent_id in lib:
			l = lib[ent_id]
			entry = Entry()
			entry.set_attr(l)
			dic[ent_id] = entry	
		return(dic)

	def init_save(self, fp):
		os.system('touch {}'.format(self.fp))
		
		fobj = open(fp, 'w')
		# create sample entry:
		entry = Entry(title='Harry Potter und der Halbblutprinz', 
					  author='Joanne K. Rowling', date=2005)
		if self.verbose:
			self._print_entry(entry)
		write_dict = dict()
		write_dict[entry.get_config()['id']] = entry.get_config()
		json.dump(write_dict, fobj, indent=4, sort_keys=True)
		fobj.close()				

	def _print_entry(self, entry):
		e = entry.get_config()
		print('----------------------------------------------------------------------------')
		print('Entry:')
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
		print('\t -- number of entries: {}'.format(len(self.library_dict)))
		print('----------------------------------------------------------------------------')



