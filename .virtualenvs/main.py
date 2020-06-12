from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window 

import os, re
import sys
#sys.path.insert(1, '.virtualenvs/backend/scanning/nampVulScanner.py')
import nmapVulScannerCopy
'''
RGBA = Red, Green, Blue, Opacity
https://www.rapidtables.com/web/color/RGB_Color.html => Use this wheel to help pick colors 
Lets say you want a navy blue color which is (0,51,102) in RBG format
Must convert into Kivy syntax. Take each number and divide by 255.0
(0,8,18) => (0/255.0, 8/255.0, 18/255.0, 1). Can actually divide it => (0, 0.03, 0.07, 1 ) 
Don't forget the trailing 1 at the end for opacity 
'''
Window.clearcolor= (0, 8/255.0, 18/255.0, 1 )

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
			print(ip_address)
			self.display.text = ip_address

			# https://github.com/scipag/vulscan
			nmapVulScannerCopy.scan(ip_address)
			print("1")
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


 