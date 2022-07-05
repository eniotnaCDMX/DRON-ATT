# Importing other libraries
from datetime import datetime
import pymysql
import pandas as pd
import os
import numpy as np
import openpyxl 

# Importing all the googlemaps stuffs
import googlemaps

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
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

# Google maps API 

API_Key = "See in Passwords DRON911"

map_client = googlemaps.Client(API_Key)

# Access to the RDS Database 
Host = "See in Passwords DRON911"
User = "See in Passwords DRON911"
ID = "See in Passwords DRON911"
Password = "See in Passwords DRON911"
Port = 3306

# Start of the KV script

Builder.load_string("""
            
<FirstPage>:
    Image:
        source: "1 - Home Page.jpg"
        keep_ratio: False
        allow_stretch: True
        
<SecondPage>:
    num: Texte.text
    Image:
        source: "2 - Phone Number.jpg"
        keep_ratio: False
        allow_stretch: True
    
    TextInput:
        background_color: 0, 0, 0, 0
        multiline: False
        pos_hint: {'x':0.114, 'y':0.203}
        size_hint: 0.76,0.059
        id : Texte
            
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.114, 'y':0.081}
        size_hint: 0.76,0.059
        on_press: root.manager.current = root.switch()
        
<SecondPageBis>
    Image:
        source: "2bis - Numero Invalido.jpg"
        keep_ratio: False
        allow_stretch: True
    
    TextInput:
        background_color: 0, 0, 0, 0
        multiline: False
        pos_hint: {'x':0.114, 'y':0.203}
        size_hint: 0.76,0.059
        id: Texte2
        
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.114, 'y':0.081}
        size_hint: 0.76,0.059
        on_press: root.manager.current = root.switch2()
    
<ThirdPage>:
    Image:
        source: "3 - Calling option.jpg"
        keep_ratio: False
        allow_stretch: True
        
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.16, 'y':0.17}
        size_hint: 0.16,0.1
        on_press: root.manager.current = 'Fourth'
    
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.68, 'y':0.17}
        size_hint: 0.16,0.1
        on_press: root.manager.current = 'First'
        
    
<FourthPage>:
    Image:
        source: "4 - willing_to_call.jpg"
        keep_ratio: False
        allow_stretch: True
        
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.18, 'y':0.164}
        size_hint: 0.65,0.06
        on_press: root.manager.current = 'Fifth'
    
    Button:
        background_color: 0, 0, 0, 0
        pos_hint: {'x':0.18, 'y':0.0825}
        size_hint: 0.65,0.059
        on_press: root.manager.current = 'First'
    
<FifthPage>:
    Image:
        source: "5 - calling.jpg"
        keep_ratio: False
        allow_stretch: True
        
""")

def get_desktop():    
    desktop = os.path.join(os.path.join
    (os.environ['USERPROFILE']), 'Desktop') 
    return desktop

class FirstPage(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch, 3)
        
    def switch(self, *args):
        self.manager.current = "Second"

class SecondPage(Screen):
    num = StringProperty()
    def switch(self):
        Contenu = self.ids.Texte.text
        if Contenu[0] == "+" and len(Contenu) == 13:
            for i in range(1,len(Contenu)):
                try:
                    int(Contenu[i])
                except:
                    self.ids.Texte.select_all()
                    self.ids.Texte.delete_selection(from_undo=False)
                    self.manager.current = "SecondBis"
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                os.remove(get_desktop() + "\\NewNumber.csv")
                d = pd.DataFrame([[self.num]],columns = ["Col1"])
                d.to_csv(get_desktop() + "\\NewNumber.csv")            
                self.manager.current = "Third"
            else:
                d = pd.DataFrame([[self.num]],columns = ["Col1"])
                d.to_csv(get_desktop() + "\\NewNumber.csv")            
                self.manager.current = "Third"
        elif len(Contenu) == 10:
            for i in range(len(Contenu)):
                try:
                    int(Contenu[i])
                except:
                    self.ids.Texte.select_all()
                    self.ids.Texte.delete_selection(from_undo=False)
                    self.manager.current = "SecondBis"
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                os.remove(get_desktop() + "\\NewNumber.csv")
                d = pd.DataFrame([[self.num]],columns = ["Col1"])
                d.to_csv(get_desktop() + "\\NewNumber.csv")            
                self.manager.current = "Third"
            else:
                d = pd.DataFrame([[self.num]],columns = ["Col1"])
                d.to_csv(get_desktop() + "\\NewNumber.csv")            
                self.manager.current = "Third"
        else:
            self.ids.Texte.select_all()
            self.ids.Texte.delete_selection(from_undo=False)
            self.manager.current = "SecondBis"
    
class SecondPageBis(Screen):
    def switch2(self):
        Contenu = self.ids.Texte2.text
        if Contenu[0] == "+" and len(Contenu) == 13:
            for i in range(1,len(Contenu)):
                try:
                    int(Contenu[i])
                except:
                    self.ids.Texte2.select_all()
                    self.ids.Texte2.delete_selection(from_undo=False)
                    self.manager.current = "SecondBis"
            SecondPage.Phone_Number = Contenu
            self.manager.current = "Third"
        elif len(Contenu) == 10:
            for i in range(len(Contenu)):
                try:
                    int(Contenu[i])
                except:
                    self.ids.Texte2.select_all()
                    self.ids.Texte2.delete_selection(from_undo=False)
                    self.manager.current = "SecondBis"
            SecondPage.Phone_Number = Contenu
            self.manager.current = "Third"
        else:
            self.ids.Texte2.select_all()
            self.ids.Texte2.delete_selection(from_undo=False)
            self.manager.current = "SecondBis"
    
class ThirdPage(Screen):
    pass
    
class FourthPage(Screen):
    pass

class FifthPage(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch, 4)
        
    def switch(self, *args):
        self.manager.current = "Sixth"

class SixthPage(Screen):
    #def __init__(self, **kwargs):
    def on_enter(self, **kwargs):   
        #super(SixthPage, self).__init__(**kwargs)
        gl = GridLayout(cols=1)
        marker = MapMarkerPopup(lat = map_client.geolocate()["location"]["lat"], lon = map_client.geolocate()["location"]["lng"])
        mapview = MapView(zoom=17, lat = map_client.geolocate()["location"]["lat"], lon = map_client.geolocate()["location"]["lng"])
        Latitude_First_Call = map_client.geolocate()["location"]["lat"]
        Longitude_First_Call = map_client.geolocate()["location"]["lng"]
        Hour_First_Call = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        LatLon = (Latitude_First_Call,Longitude_First_Call)
        Adresse = list(map_client.reverse_geocode(LatLon)[0].values())[1]
        print(Adresse.split(sep = ","))
        DB = pymysql.connect(host = Host, password = Password, user = User, port = Port)
        cursor = DB.cursor()
        cursor.execute('''USE Client_Emission_Call''')
        if len(Adresse.split(sep = ",")) == 3:
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                a = pd.read_csv(get_desktop() + "\\NewNumber.csv")            
                Calle = Adresse.split(sep = ",")[0]
                Estado = Adresse.split(sep = ",")[1][1:]            
                # Sending the data to the RDS Database
                cursor.execute("INSERT INTO Client_Emission_Call_Table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(list(a["Col1"])[0],Hour_First_Call,Latitude_First_Call,Longitude_First_Call,Calle,np.nan,np.nan,np.nan,Estado))
                cursor.connection.commit()
                os.remove(get_desktop() + "\\NewNumber.csv")
            
        elif len(Adresse.split(sep = ",")) == 4:
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                a = pd.read_csv(get_desktop() + "\\NewNumber.csv")
                Calle = Adresse.split(sep = ",")[0]
                Codigo_Postal = Adresse.split(sep = ",")[1][1:6]
                Ciudad = Adresse.split(sep = ",")[1][7:]
                Estado = Adresse.split(sep = ",")[2][1:]            
                # Sending the data to the RDS Database
                cursor.execute("INSERT INTO Client_Emission_Call_Table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(list(a["Col1"])[0],Hour_First_Call,Latitude_First_Call,Longitude_First_Call,Calle,np.nan,Ciudad,Codigo_Postal,Estado))
                cursor.connection.commit()
                os.remove(get_desktop() + "\\NewNumber.csv")
            
        elif len(Adresse.split(sep = ",")) == 5:
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                a = pd.read_csv(get_desktop() + "\\NewNumber.csv")
                Calle = Adresse.split(sep = ",")[0]
                Colonia = Adresse.split(sep = ",")[1][1:]
                Codigo_Postal = Adresse.split(sep = ",")[2][1:6]
                Ciudad = Adresse.split(sep = ",")[2][7:]
                Estado = Adresse.split(sep = ",")[3][1:]            
            # Sending the data to the RDS Database
                cursor.execute("INSERT INTO Client_Emission_Call_Table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(list(a["Col1"])[0],Hour_First_Call,Latitude_First_Call,Longitude_First_Call,Calle,Colonia,Ciudad,Codigo_Postal,Estado))
                cursor.connection.commit()
                os.remove(get_desktop() + "\\NewNumber.csv")                   
        
        elif len(Adresse.split(sep = ",")) == 6:
            if os.path.exists(get_desktop() + "\\NewNumber.csv"):
                a = pd.read_csv(get_desktop() + "\\NewNumber.csv")
                Calle = Adresse.split(sep = ",")[0]
                Colonia = Adresse.split(sep = ",")[1][1:]
                Codigo_Postal = Adresse.split(sep = ",")[3][1:6]
                Ciudad = Adresse.split(sep = ",")[3][7:]
                Estado = Adresse.split(sep = ",")[4][1:]            
            # Sending the data to the RDS Database
                cursor.execute("INSERT INTO Client_Emission_Call_Table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(list(a["Col1"])[0],Hour_First_Call,Latitude_First_Call,Longitude_First_Call,Calle,Colonia,Ciudad,Codigo_Postal,Estado))
                cursor.connection.commit()                   
                os.remove(get_desktop() + "\\NewNumber.csv")        
        mapview.add_marker(marker)
        gl.add_widget(mapview)
        self.add_widget(gl)

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        # Create the pages
        sm.add_widget(FirstPage(name='First'))
        sm.add_widget(SecondPage(name='Second'))
        sm.add_widget(SecondPageBis(name='SecondBis'))
        sm.add_widget(ThirdPage(name='Third'))
        sm.add_widget(FourthPage(name='Fourth'))
        sm.add_widget(FifthPage(name='Fifth'))
        sm.add_widget(SixthPage(name='Sixth'))
        return sm

if __name__ == '__main__':
    TestApp().run()



