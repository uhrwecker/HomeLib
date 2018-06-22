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
		app.setSize(600, 500)
		app.setTitle('HomeLib - library software for home usage')
		app.setResizable(canResize=True)
		app.setLocation('CENTER')
		app.setBg('LIGHT BLUE', tint=True)

		file_menu = ['Save', '-', 'Close']
		app.addMenuList('File', file_menu, [self.lib.save_lib, self.root.stop])
		app.addMenuItem('File', 'Save', func=self.lib.save_lib, shortcut='Control-s')
		app.addMenuItem('File', 'Close', func=self.__check_stop, shortcut='Control-q')

	def run(self):
		self.root.go()

	def __check_stop(self):
		if self.root.yesNoBox('Confirm Exit', 'Are you sure you want to exit the application?'):
			self.root.stop()

App()
