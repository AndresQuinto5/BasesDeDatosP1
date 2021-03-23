import kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from queries import *
import datetime
from reportlab.pdfgen import canvas
from youtube_search import YoutubeSearch
import ast
import youtube_dl
import os
import random
Window.clearcolor = (201/255.0, 149/255.0, 223/255.0, 1)
Window.size = (1100, 700)


import psycopg2
import csv

#connect to de database
con = psycopg2.connect(
    host = "localhost",
    database = "proshecto",
    user = "postgres",
    password = "admin")

#create a cursor
cur = con.cursor()

#MongoDB
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JDiegoSolorzano:Diego199@cluster0-5fvcd.mongodb.net/proyectiFinal?retryWrites=true&w=majority")
db = cluster["proyectiFinal"]
collection = db["compras"]


class MainWindow(Screen):
    errM = ObjectProperty(None)


    def userVer(self):
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        EleventhWindow.userActual = usern
        TwelveWindow.userActual = usern
        ThirteenWindow.userActual = usern
        FourthWindow.userActual = usern
        FifteenWindow.userActual = usern
        FourteenWindow.userActual = usern
        NineteenWindow.userActual = usern

        if usern != '':
            cur.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = %s AND roleid = 3", (str(usern), str(passw)))
            opcion1 = cur.fetchall()
            s = str(opcion1)
            if s != '[(0,)]':
                self.errM.text = ''
                self.manager.transition.direction = "left"
                self.manager.current = 'home'
            else:
                self.errM.text = 'Invalid username or password'


class SecondWindow(Screen):
    errM = ObjectProperty(None)

    def userVer(self):
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        EleventhWindow.userActual = usern
        TwelveWindow.userActual = usern
        ThirteenWindow.userActual = usern
        FourthWindow.userActual = usern
        FifteenWindow.userActual = usern
        FourteenWindow.userActual = usern
        NineteenWindow.userActual = usern
        TwentyWindow.userActual = usern

        if usern != '':
            cur.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = %s AND roleid = 1",
                        (str(usern), str(passw)))
            opcion1 = cur.fetchall()
            s = str(opcion1)
            if s != '[(0,)]':

                self.errM.text = ''
                self.manager.current = 'homeA'
                self.manager.transition.direction = "left"
            else:
                self.errM.text = 'Invalid username or password'


class ThirdWindow(Screen):
    pass