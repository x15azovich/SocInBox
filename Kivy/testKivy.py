import portScanner
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


def callback(instance):
	print('The button <%s> is being pressed' % instance.text)
	print(password)

class GaddysClass(GridLayout):
	def __init__(self, **kwargs):
		super(GaddysClass, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)
		MyButton = Button(text='HEllow')
		MyButton.bind(on_press=callback(self.password))
		self.add_widget(MyButton)

class FirstKivy(App):
	def build(self):
		return GaddysClass()
	#button = Button(text='Hello world', font_size=14)
	#btn1 = Button(text='Hello world 1')
	#btn1.bind(on_press=callback)
	#btn2 = Button(text='Hello world 2')
	#btn2.bind(on_press=callback)

FirstKivy().run()

portScanner.scan_port()
