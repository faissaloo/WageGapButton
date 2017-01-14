#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.core.window import Window
from kivy.core.text import Label

class gapBtn(Widget):
	def __init__(self):
		#Call the Widget constructor so we don't segfault
		super(gapBtn, self).__init__()
		
		#768 is the width of the image, and
		#that's for a 1080p screen so let's scale that
		#We're using the constant 0.71 because
		#for some reason 768/1080 leads to the result
		#being zero, floating point error?
		self.spriteWidth=0.71*min(Window.size)
		self.spriteHeight=0.71*min(Window.size)
		self.sprite=['res/button.png','res/button2.png']
		#Resources
		self.sound = SoundLoader.load("res/shoe.mp3")
		
		with self.canvas:
			Rectangle(source=self.sprite[0],size=(self.spriteWidth,self.spriteHeight),pos=((Window.size[0]-self.spriteWidth)/2,(Window.size[1]-self.spriteHeight)/2))
	
	def on_size(self, *args):
		with self.canvas:
			self.canvas.clear()
			Rectangle(source=self.sprite[0],size=(self.spriteWidth,self.spriteHeight),pos=((Window.size[0]-self.spriteWidth)/2,(Window.size[1]-self.spriteHeight)/2))
	
	def on_touch_down(self,touch):
		#So that we can replay if it's already playing
		if self.sound.status=="play":
			self.sound.stop()
		self.sound.play()
		
		with self.canvas:
			self.canvas.clear()
			Rectangle(source=self.sprite[1],size=(self.spriteWidth,self.spriteHeight),pos=((Window.size[0]-self.spriteWidth)/2,(Window.size[1]-self.spriteHeight)/2))
		
	def on_touch_up(self,touch):
		with self.canvas:
			Rectangle(source=self.sprite[0],size=(self.spriteWidth,self.spriteHeight),pos=((Window.size[0]-self.spriteWidth)/2,(Window.size[1]-self.spriteHeight)/2))
		


class main(App, BoxLayout):
	def build(self):
		self.icon='icon.png'
		return gapBtn()
		
if __name__ == "__main__":
	main().run()
