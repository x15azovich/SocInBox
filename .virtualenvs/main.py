from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.floatlayout import FloatLayout

class MainWindow(Screen):
	pass

class HomeWindow(Screen):
	pass

class PatchingWindow(Screen):
	pass

class NetworkWindow(Screen):
	pass

class ScanningWindow(Screen):
	pass

class HostbaseWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	MyMainApp().run()
