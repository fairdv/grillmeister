from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty



class ScreenEins(Screen):
	pass

class ScreenZwei(Screen):
	pass

class ScreenDrei(Screen):
	pass
	
class ScreenVier(Screen):
	pass

class Manager(ScreenManager):
	
	screen_eins = ObjectProperty(None)
	screen_zwei = ObjectProperty(None)
	screen_drei = ObjectProperty(None)
	screen_vier = ObjectProperty(None)
	

class ScreensApp(App):
	
	def build(self):
		m = Manager(transition= WipeTransition())
		return m

if __name__ == "__main__":
	ScreensApp().run()

	
