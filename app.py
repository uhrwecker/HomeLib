import lib.library as library
import appJar as appjar

class App():
	def __init__(self):
		self.root = appjar.gui()
		self.main_window(self.root)

	def main_window(self, app, fp='./doc/main.log'):
		app.setLogFile(fp)
		app.setSize(600, 500)
		app.setTitle('HomeLib - library software for home usage')
		app.setResizable(canResize=True)
		app.setLocation('CENTER')
		app.setBg('LIGHT BLUE', tint=True)

	def run(self):
		self.root.go()

