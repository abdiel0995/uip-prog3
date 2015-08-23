import pyodbc 
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
class ParcialApp(App):
	pass
if __name__ == '__main__':
	ParcialApp().run()



DBfile = 'base.accdb'
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.accdb)};DBQ='+DBfile)
cursor = conn.cursor()


