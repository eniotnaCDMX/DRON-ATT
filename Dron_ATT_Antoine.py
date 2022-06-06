# -*- coding: utf-8 -*-
import time

# Importing all the kivy items
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.config import Config

# Permit page swiching
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition



# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
            
<FirstPage>:
    Image:
        source: "1 - Home Page.jpg"
        keep_ratio: False
        allow_stretch: True
        
<SecondPage>:
    Image:
        source: "2 - Calling option.jpg"
        keep_ratio: False
        allow_stretch: True
        
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.16, 'y':0.17}
        size_hint: 0.16,0.1
        on_press: root.manager.current = 'Third'
    
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.68, 'y':0.17}
        size_hint: 0.16,0.1
        on_press: root.manager.current = 'First'
        
    
<ThirdPage>:
    Image:
        source: "3 - willing_to_call.jpg"
        keep_ratio: False
        allow_stretch: True
        
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.18, 'y':0.164}
        size_hint: 0.65,0.06
        on_press: root.manager.current = 'Fourth'
    
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.18, 'y':0.0825}
        size_hint: 0.65,0.059
        on_press: root.manager.current = 'First'
    
<FourthPage>:
    Image:
        source: "4 - calling.jpg"
        keep_ratio: False
        allow_stretch: True
 
""")

class FirstPage(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch, 4)
        
    def switch(self, *args):
        self.manager.current = "Second"

class SecondPage(Screen):
    pass
    
class ThirdPage(Screen):
    pass

class FourthPage(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(FirstPage(name='First'))
        sm.add_widget(SecondPage(name='Second'))
        sm.add_widget(ThirdPage(name='Third'))
        sm.add_widget(FourthPage(name='Fourth'))
        return sm

if __name__ == '__main__':
    TestApp().run()

