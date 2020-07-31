from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window 
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView


import os, re
import sys
#sys.path.insert(1, '.virtualenvs/backend/scanning/nampVulScanner.py')
import Vulscan
import CVEnumbersExtractor
import CVEdescriptionAndSolutionsGetter
import windows_7
'''
RGBA = Red, Green, Blue, Opacity
https://www.rapidtables.com/web/color/RGB_Color.html => Use this wheel to help pick colors 
Lets say you want a navy blue color which is (0,51,102) in RBG format
Must convert into Kivy syntax. Take each number and divide by 255.0
(0,8,18) => (0/255.0, 8/255.0, 18/255.0, 1). Can actually divide it => (0, 0.03, 0.07, 1 ) 
Don't forget the trailing 1 at the end for opacity 
'''

'''
TO DO:
1. See how to put a white canvas/label/rectangle box to hold the data table
2. Research how to put a data table: recycleview example
3. make sure data table can be scrollable
4. make rows based on number of CVES 
5. use sample CVE list and description to plug into empty boxes 
6. adjust colors and size of table accordingly 
'''
Window.clearcolor= (0, 8/255.0, 18/255.0, 1 )

class MainWindow(Screen):
	pass

class HomeWindow(Screen):
	pass

class PatchingWindow(Screen):
	def load_patches(self):

#THE REAL SOLUTION

		results = CVEdescriptionAndSolutionsGetter.getCveDescription()
		data = {}

		CVEs = []
		CVE_Number = {}
		CVE_Description = {}
		CVE_Solution = {}


		with open('CVEnumbers.txt') as my_file:
			CVEs = my_file.readlines()
			CVEs = [x.strip() for x in CVEs] 
	

		for index, x in enumerate(CVEs):
			CVE_Number[index] = x
			CVE_Description[index] = results.get(x).get("description")
			CVE_Solution[index] = results.get(x).get("href")

		data["CVE Number"] = CVE_Number
		data["Description"] = CVE_Description
		data["Solution"] = CVE_Solution

			
		column_titles = [x for x in data.keys()]
		rows_length = len(data[column_titles[0]])
		self.columns = len(column_titles)

		table_data = []
		for y in column_titles:
			table_data.append({'text':str(y),'size_hint_y':None,'pos_hint':{'top': 0.1},'height':30,'bcolor':(.05,.30,.80,1)}) #append the data

		for z in range(rows_length):
			for y in column_titles:
				table_data.append({'text':str(data[y][z]),'size_hint_y':None,'height':60,'bcolor':(.06,.25,.50,1)}) #append the data

		self.ids.table_floor_layout.cols = self.columns #define value of cols to the value of self.columns
		self.ids.table_floor.data = table_data #add table_data to data value
	
	def display_result(self):
		pass


class NetworkWindow(Screen):
	def press_block(self,ip_address):
		try:
			print(ip_address)
			self.display.text = ip_address
			# https://github.com/scipag/vulscan
			windows_7.add_rule("Blocked IP From Console", ip_address)
			print(ip_address)
		except:
			print("YOu FAIL")

	def press_remove(self,ip_address):
		try:
			print(ip_address)
			self.display.text = ip_address
			# https://github.com/scipag/vulscan
			windows_7.delete_rule("Remove Blocked IP From Console", ip_address)
			print(ip_address)
		except:
			print("YOu FAIL")

	def press_modify(self,ip_address):
		try:
			print(ip_address)
			self.display.text = ip_address
			# https://github.com/scipag/vulscan
			windows_7.modify_rule("Blocked IP From Console", ip_address)
			print(ip_address)
		except:
			print("YOu FAIL")

	def display_result(self):
		pass

class ScanningWindow(Screen):
	## Look up floatlayout to replace gridlayout, more freedom and less box'ey 
	def press_scan(self,ip_address):
		try:
			print(ip_address)
			self.display.text = ip_address

			# https://github.com/scipag/vulscan
			Vulscan.scan(ip_address)
			print("1")

		except:
			self.display.text = "error"
			print("2")

		try: 
			CVEnumbersExtractor.vulnScanExtract()
			print ("VulnScanner running")
		except:
			print("Anthony Can't Code")

		try: 
			CVEdescriptionAndSolutionsGetter.getCveDescription()
			print ("CVE Descirption Works")
		except:
			print("Anthony Can't Code2")


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


 