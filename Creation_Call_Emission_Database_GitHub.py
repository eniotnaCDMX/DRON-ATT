# CON ESTE SCRIPT SE CREO LA BASE DE DATOS : Client_Emision_Call

import pandas as pd
import pymysql
import datetime
import os
import openpyxl

def get_desktop():    
    desktop = os.path.join(os.path.join
    (os.environ['USERPROFILE']), 'Desktop') 
    return desktop


# CREDENCIALES USADOS PARA ACCEDER A LA BASE DE DATOS

Host = "See Passwords DRON911"
User = "See Passwords DRON911"
ID = "See Passwords DRON911"
Password = "See Passwords DRON911"
Port = 3306


DB = pymysql.connect(host = Host, password = Password, user = User, port = Port)

cursor = DB.cursor()


# CREATION OF THE DATA BASE
#SQL1 = '''CREATE DATABASE IF NOT EXISTS Client_Emission_Call'''
#SQL2 = '''USE Client_Emission_Call'''
#SQL3 = '''
#CREATE TABLE Client_Emission_Call_Table(
#Phone_Number VARCHAR(20) NOT NULL,
#Hour_Of_Call VARCHAR(25),
#Latitude DOUBLE(17,15),
#Longitude DOUBLE(17,15),
#Street_Coordinates VARCHAR(60),
#District VARCHAR(40),
#City VARCHAR(35),
#Post_Code VARCHAR(10),
#State VARCHAR(35),
#PRIMARY KEY (Phone_Number,Hour_Of_Call)
#)'''
#cursor.execute(SQL1)
#cursor.connection.commit()
#cursor.execute(SQL2)
#cursor.execute(SQL3)
#cursor.connection.commit()



# REINITIALISATION OF THE WHOLE DATA BASE

#SQL1 = '''CREATE DATABASE IF NOT EXISTS Client_Emission_Call'''
#SQL2 = '''USE Client_Emission_Call'''
#SQL4 = "DROP TABLE Client_Emission_Call_Table"
#SQL3 = '''
#CREATE TABLE Client_Emission_Call_Table(
#Phone_Number VARCHAR(20) NOT NULL,
#Hour_Of_Call VARCHAR(25),
#Latitude DOUBLE(17,15),
#Longitude DOUBLE(17,15),
#Street_Coordinates VARCHAR(60),
#District VARCHAR(40),
#City VARCHAR(35),
#Post_Code VARCHAR(10),
#State VARCHAR(35),
#PRIMARY KEY (Phone_Number,Hour_Of_Call)
#)'''
#cursor.execute(SQL1)
#cursor.connection.commit()
#cursor.execute(SQL2)
#cursor.execute(SQL4)
#cursor.connection.commit()
#cursor.execute(SQL3)
#cursor.connection.commit()


# CHECK THE CONTENT OF THE DATABASE
#cursor.execute("USE Client_Emission_Call")
#SQL5 = " SELECT * FROM Client_Emission_Call_Table"
#df = pd.read_sql(SQL5,DB)






