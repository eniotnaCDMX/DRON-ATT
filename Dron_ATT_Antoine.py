# -*- coding: utf-8 -*-


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

def callback(instance):
    print("Bonjou Maxi")
    
def OtherFunction(instance,x):
    return x**2 - 1

class TestBoutons(BoxLayout):
    def __init__(self,**kwags):
        super().__init__(**kwags)
        self.orientation = "vertical"
        bA = Button(text = "Bouton A",color = "red",background_color = "blue")
        bA.bind(on_press = callback)
        bB = Button(text = "Bouton B")
        bB.bind(on_press = OtherFunction)
        bC = Button(text = "Bouton C")
        self.add_widget(bA)
        self.add_widget(bB)
        self.add_widget(bC)

class HelloWorld(App):
    def build(self):
        #return Builder(KV1)
        return TestBoutons()
        
if __name__ == "__main__":
    HelloWorld().run()
