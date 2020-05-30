from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os, re
import sys
#sys.path.insert(1, '.virtualenvs/backend/scanning/nampVulScanner.py')
import nmapVulScannerCopy

class MainWindow(Screen):
	pass

class HomeWindow(Screen):
	pass

class PatchingWindow(Screen):
	pass

class NetworkWindow(Screen):
	pass

class ScanningWindow(Screen):
	## Look up floatlayout to replace gridlayout, more freedom and less box'ey 
	def press_scan(self,ip_address):
		try:
			self.display.text = ip_address
			nmapVulScannerCopy.scan(ip_address)
		except:
			self.display.text = "error"
			print("2")

	def display_result(self):
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
