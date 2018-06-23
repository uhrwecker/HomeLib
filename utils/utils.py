class Util():
	def __init__(self):
		self.a = 0

	def sort_dict(self, dic, by='title'):
		sort_list = list()
		by_list = list()
		for ent_id in dic:
			by_list.append(dic[ent_id][by])
		sorted(by_list)
		for item in by_list:
			for ent_id in dic:
				if dic[ent_id][by] == item and not dic[ent_id] in sort_list:
					sort_list.append(dic[ent_id])
		return(sort_list)
	
