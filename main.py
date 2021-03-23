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

class AddPlWindow(Screen):
    sinp = ObjectProperty(None)
    songsele = ""
    seco = ""
    def addPla(self):
        if self.sinp.text != "":
            cur.execute("SELECT playlistid FROM playlist WHERE name LIKE '%" + self.sinp.text + "%' LIMIT 1")
            opcion1 = cur.fetchall()
            s = str(opcion1)
            s = s.replace(',', '')
            s = s.replace('(', '')
            s = s.replace(')', '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace("'", '')
            playid = int(s)
            cur.execute("SELECT t.trackid FROM track t WHERE t.name = '" + self.songsele + "' LIMIT 1")
            opcion1 = cur.fetchall()
            if len(opcion1) == 0:
                cur.execute("SELECT t.trackid FROM track t WHERE t.name = '" + self.seco + "' LIMIT 1")
                opcion1 = cur.fetchall()
            print(opcion1)
            s = str(opcion1)
            s = s.replace(',', '')
            s = s.replace('(', '')
            s = s.replace(')', '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace("'", '')
            print(s)
            trackid = int(s)

            cur.execute("INSERT INTO playlisttrack VALUES(%s, %s)", (playid, trackid))
            con.commit()

class FourthWindow(Screen):
    songe = ObjectProperty(None)
    name1 = ObjectProperty(None)
    resu = ObjectProperty(None)
    userActual = ""

    pl1 = ObjectProperty(None)
    pl2 = ObjectProperty(None)
    pl3 = ObjectProperty(None)
    pl4 = ObjectProperty(None)
    pl5 = ObjectProperty(None)
    pl6 = ObjectProperty(None)
    pl7 = ObjectProperty(None)
    pl8 = ObjectProperty(None)
    pl9 = ObjectProperty(None)
    pl10 = ObjectProperty(None)
    songDur = 0
    songCur = 0
    currtime = ObjectProperty(None)
    name1 = ObjectProperty(None)
    opcion1 = []

    songsel = ""
    segund = []
    def search(self):
        canciones = []
        self.songsel = self.songe.text
        arti = ""
        self.songe.text = ""
        cur.execute(
            "SELECT track.name, artist.name FROM track INNER JOIN album on album.albumid = track.albumid INNER JOIN artist on artist.artistid = album.artistid WHERE track.name LIKE '%" + self.songsel + "%' LIMIT 10")
        self.opcion1 = cur.fetchall()
        print(self.opcion1)
        if len(self.opcion1) == 0:
            cur.execute("SELECT track.name, artist.name FROM track INNER JOIN album on album.albumid = track.albumid INNER JOIN artist on artist.artistid = album.artistid WHERE artist.name LIKE '%" + self.songsel + "%' LIMIT 10")
            self.opcion1 = cur.fetchall()
            if len(self.opcion1) == 0:
                cur.execute(
                    "SELECT track.name, artist.name FROM track INNER JOIN album on album.albumid = track.albumid INNER JOIN artist on artist.artistid = album.artistid WHERE album.title LIKE '%" + self.songsel + "%' LIMIT 10")
                self.opcion1 = cur.fetchall()
                if len(self.opcion1) == 0:

                    self.pl1.text = "No results found"
                    self.pl2.text = ""
                    self.pl3.text = ""
                    self.pl4.text = ""
                    self.pl5.text = ""
                    self.pl6.text = ""
                    self.pl7.text = ""
                    self.pl8.text = ""
                    self.pl9.text = ""
                    self.pl10.text = ""
                else:

                    for s in self.opcion1:
                        s = str(s)
                        s = s.replace("', ", ' by ')
                        s = s.replace('", ', ' by ')
                        s = s.replace(',', '')
                        s = s.replace('(', '')
                        s = s.replace(')', '')
                        s = s.replace('[', '')
                        s = s.replace(']', '')
                        s = s.replace("'", '')
                        s = s.replace('"', '')
                        canciones.append(s)
            else:

                for s in self.opcion1:
                    s = str(s)
                    s = s.replace("', ", ' by ')
                    s = s.replace('", ', ' by ')
                    s = s.replace(',', '')
                    s = s.replace('(', '')
                    s = s.replace(')', '')
                    s = s.replace('[', '')
                    s = s.replace(']', '')
                    s = s.replace("'", '')
                    s = s.replace('"', '')
                    canciones.append(s)

        else:
            for s in self.opcion1:
                s = str(s)
                s = s.replace("', ", ' by ')
                s = s.replace('", ', ' by ')
                s = s.replace(',', '')
                s = s.replace('(', '')
                s = s.replace(')', '')
                s = s.replace('[', '')
                s = s.replace(']', '')
                s = s.replace("'", '')
                s = s.replace('"', '')
                canciones.append(s)

        if len(canciones) > 0:
            self.pl1.text = canciones[0]
            self.pl2.text = ""
            self.pl3.text = ""
            self.pl4.text = ""
            self.pl5.text = ""
            self.pl6.text = ""
            self.pl7.text = ""
            self.pl8.text = ""
            self.pl9.text = ""
            self.pl10.text = ""
            if len(canciones) > 1:
                self.pl2.text = canciones[1]
                if len(canciones) > 2:
                    self.pl3.text = canciones[2]
                    if len(canciones) > 3:
                        self.pl4.text = canciones[3]
                        if len(canciones) > 4:
                            self.pl5.text = canciones[4]
                            if len(canciones) > 5:
                                self.pl6.text = canciones[5]
                                if len(canciones) > 6:
                                    self.pl7.text = canciones[6]
                                    if len(canciones) > 7:
                                        self.pl8.text = canciones[7]
                                        if len(canciones) > 8:
                                            self.pl9.text = canciones[8]
                                            if len(canciones) > 8:
                                                self.pl10.text = canciones[9]
        print(canciones)


        print(self.opcion1)
        for s in self.opcion1:
            s = str(s)
            s = s.replace('", ', ' by ')
            s = s.replace("', ", ' by ')
            s = s.replace(',', '')
            s = s.replace("'", "''")
            s = s.replace('(', '')
            s = s.replace(')', '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace('"', '')
            self.segund.append(s)
    def addPla(self, indexe):
        if indexe == 1:
            names = self.pl1.text
            seco = self.segund[0]
        elif indexe == 2:
            names = self.pl2.text
            seco = self.segund[1]
        elif indexe == 3:
            names = self.pl3.text
            seco = self.segund[2]
        elif indexe == 4:
            names = self.pl4.text
            seco = self.segund[3]
        elif indexe == 5:
            names = self.pl5.text
            seco = self.segund[4]
        elif indexe == 6:
            names = self.pl6.text
            seco = self.segund[5]
        elif indexe == 7:
            names = self.pl7.text
            seco = self.segund[6]
        elif indexe == 8:
            names = self.pl8.text
            seco = self.segund[7]
        elif indexe == 9:
            names = self.pl9.text
            seco = self.segund[8]
        elif indexe == 10:
            names = self.pl10.text
            seco = self.segund[9]
        if str(names) != "":
            titl = names.split(" by", 1)
            print(titl)
            second = seco.split(" by", 1)
            print(seco)
            AddPlWindow.songsele = titl[0]
            AddPlWindow.seco = second[0]
            self.manager.current = 'addPlaylist'
    def selected(self, indexe):
        self.playbtn(indexe)
    
    def playtime(self, interval):
        if self.songCur != self.songDur:
            self.songCur = self.songCur + 1
            self.currtime.value = self.songCur / self.songDur

        else:
            self.songCur = 0
            self.currtime.value = 0

    def playbtn(self, indexe):
        if indexe == 1:
            names = self.pl1.text
            seco = self.segund[0]
        elif indexe == 2:
            names = self.pl2.text
            seco = self.segund[1]
        elif indexe == 3:
            names = self.pl3.text
            seco = self.segund[2]
        elif indexe == 4:
            names = self.pl4.text
            seco = self.segund[3]
        elif indexe == 5:
            names = self.pl5.text
            seco = self.segund[4]
        elif indexe == 6:
            names = self.pl6.text
            seco = self.segund[5]
        elif indexe == 7:
            names = self.pl7.text
            seco = self.segund[6]
        elif indexe == 8:
            names = self.pl8.text
            seco = self.segund[7]
        elif indexe == 9:
            names = self.pl9.text
            seco = self.segund[8]
        elif indexe == 10:
            names = self.pl10.text
            seco = self.segund[9]
        if str(names) != "":
            conserv = names
            titl = names.split(" by", 1)
            print(titl)
            second = seco.split(" by", 1)
            print(seco)
            names = titl[0]
            Clock.unschedule(self.playtime)

            print(conserv)
            result = YoutubeSearch(conserv, max_results=1).to_json()
            resultado = ast.literal_eval(result)
            valor = list(resultado.values())
            try:
                values = list(valor[0][0].values())
                url = 'https://www.youtube.com' + str(values[1])
                file1 = values[1].split('=')
                file_name = file1[1]

                def my_hook(d):
                    if d['status'] == 'finished':
                        print('Done downloading, now converting ...')

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(id)s',
                    'noplaylist': True,
                    'progress_hooks': [my_hook],
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                try:
                    os.rename(file_name, file_name + '.mp3')
                except:
                    print("")
                os.system("start " + file_name + '.mp3')
            except:
                print("Esta cancion no se encuentra disponible en este momento")
                print("Intente de nuevo en un momento")


            print(names[0])
            cur.execute(
                "SELECT trackid FROM track WHERE name = '" + str(names) + "' LIMIT 1")
            opcion6 = cur.fetchall()
            if len(opcion6) != 0:

                s = str(opcion6[0])
                s = s.replace(',', '')
                s = s.replace('(', '')
                s = s.replace(')', '')
                tid = s
                print("aho")
                print(tid)
                print(self.userActual)
                cur.execute(
                    "update track set views = views + 1 , modify = '" + str(self.userActual) + "' where trackid = " + str(tid) + "")
                con.commit()
            self.songCur = 0
            cur.execute(
                "SELECT milliseconds FROM track WHERE name = %s LIMIT 1", (str(names),))
            opcion3 = cur.fetchall()
            if len(opcion3) == 0:
                cur.execute(
                "SELECT milliseconds FROM track WHERE name = '" + str(second[0]) + "' LIMIT 1")
                opcion3 = cur.fetchall()
                if len(opcion3) == 0:
                    opcion3.append(300000)
            s = str(opcion3[0])
            s = s.replace(',', '')
            s = s.replace('(', '')
            s = s.replace(')', '')
            self.songDur = (float(s)) / 1000

            self.name1.text = "Now Playing: " + str(conserv)
            Clock.schedule_interval(self.playtime, 1)

    def buy(self, indexe):
        if indexe == 1:
            names = self.pl1.text
            seco = self.segund[0]
        elif indexe == 2:
            names = self.pl2.text
            seco = self.segund[1]
        elif indexe == 3:
            names = self.pl3.text
            seco = self.segund[2]
        elif indexe == 4:
            names = self.pl4.text
            seco = self.segund[3]
        elif indexe == 5:
            names = self.pl5.text
            seco = self.segund[4]
        elif indexe == 6:
            names = self.pl6.text
            seco = self.segund[5]
        elif indexe == 7:
            names = self.pl7.text
            seco = self.segund[6]
        elif indexe == 8:
            names = self.pl8.text
            seco = self.segund[7]
        elif indexe == 9:
            names = self.pl9.text
            seco = self.segund[8]
        elif indexe == 10:
            names = self.pl10.text
            seco = self.segund[9]
        if str(names) != "":
            NineteenWindow.songsele = names
            NineteenWindow.seco = seco
            self.manager.transition.direction = "left"
            self.manager.current = 'cart'


class NineteenWindow(Screen):
    songsele = ""
    seco = ""
    userActual = ""

    pl1 = ObjectProperty(None)
    pl2 = ObjectProperty(None)
    pl3 = ObjectProperty(None)
    pl4 = ObjectProperty(None)
    pl5 = ObjectProperty(None)
    pl6 = ObjectProperty(None)
    pl7 = ObjectProperty(None)
    pl8 = ObjectProperty(None)
    pl9 = ObjectProperty(None)
    pl10 = ObjectProperty(None)

    avail = []
    totalprice = 0


    def on_enter(self, *args):
        self.addSel()
    def addSel(self):
        if len(self.avail) < 10:
            if self.songsele not in self.avail:
                self.avail.append(self.songsele)
                self.setS()


    def setS(self):
        if len(self.avail) <= 10:
            self.pl1.text = ""
            self.pl2.text = ""
            self.pl3.text = ""
            self.pl4.text = ""
            self.pl5.text = ""
            self.pl6.text = ""
            self.pl7.text = ""
            self.pl8.text = ""
            self.pl9.text = ""
            self.pl10.text = ""
            if len(self.avail) > 0 and self.avail[0]:
                self.pl1.text = self.avail[0]
                if len(self.avail) > 1:
                    self.pl2.text = self.avail[1]
                    if len(self.avail) > 2:
                        self.pl3.text = self.avail[2]
                        if len(self.avail) > 3:
                            self.pl4.text = self.avail[3]
                            if len(self.avail) > 4:
                                self.pl5.text = self.avail[4]
                                if len(self.avail) > 5:
                                    self.pl6.text = self.avail[5]
                                    if len(self.avail) > 6:
                                        self.pl7.text = self.avail[6]
                                        if len(self.avail) > 7:
                                            self.pl8.text = self.avail[7]
                                            if len(self.avail) > 8:
                                                self.pl9.text = self.avail[8]
                                                if len(self.avail) > 8:
                                                    self.pl10.text = self.avai[9]

    def removes(self, indexe):
        print(self.avail[indexe - 1])
        self.avail.remove(self.avail[indexe - 1])
        self.setS()

    found = True
    def checkout(self):
        if len(self.avail) > 0:
            cur.execute(
                "SELECT MAX(invoicelineid) + 1 FROM invoiceline")
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", "")
            print(r)
            print(opcion3)
            self.invoicelineid = int(r)

            cur.execute(
                "SELECT MAX(invoiceid) + 1 FROM invoiceline")
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            print(opcion3)
            self.invoiceid = int(r)

            cur.execute(
                "SELECT customer.customerid FROM customer INNER JOIN users on customer.customerid = users.customerid WHERE users.username = '" + str(self.userActual) + "'")
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            print(opcion3)
            self.cusid = int(r)

            today = datetime.datetime.now()
            d1 = today.strftime("%Y-%m-%d %H:%M:%S")

            cur.execute(
                "SELECT address FROM customer WHERE customerid = " + str(self.cusid))
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            print(opcion3)
            self.address = str(r)

            cur.execute(
                "SELECT city FROM customer WHERE customerid = " + str(self.cusid))
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            print(opcion3)
            self.city = str(r)

            cur.execute(
                "SELECT state FROM customer WHERE customerid = " + str(self.cusid))
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            print(opcion3)
            self.state = str(r)

            cur.execute(
                "SELECT country FROM customer WHERE customerid = " + str(self.cusid))
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            self.country = str(r)

            cur.execute(
                "SELECT postalcode FROM customer WHERE customerid = " + str(self.cusid))
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            self.postal = str(r)

            i = 0
            for r in self.avail:

                titl = r.split(" by", 1)
                print(titl)
                cur.execute(
                    "SELECT trackid FROM track WHERE name = '" + str((titl[0])) + "' LIMIT 1")
                opcion3 = cur.fetchall()
                r = str(opcion3)
                r = r.replace('[', "")
                r = r.replace(']', "")
                r = r.replace('(', "")
                r = r.replace(')', "")
                r = r.replace("'", "")
                r = r.replace('"', "")
                r = r.replace(",", '')
                print(opcion3)
                if len(opcion3):
                    self.idss = 3
                    self.found = False
                else:

                    self.idss = int(r)

                cur.execute(
                    "SELECT unitprice FROM track WHERE trackid = " + str(self.idss))
                opcion3 = cur.fetchall()
                r = str(opcion3)
                r = r.replace('[', "")
                r = r.replace(']', "")
                r = r.replace('(', "")
                r = r.replace(')', "")
                r = r.replace('Decimal', "")
                r = r.replace("'", "")
                r = r.replace('"', "")
                r = r.replace(",", '')
                print(opcion3)
                self.price = float(r)