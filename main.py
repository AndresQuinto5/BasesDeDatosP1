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
Window.clearcolor = (72/255.0, 19/255.0, 95/255.0, 1)
Window.size = (1100, 700)


import psycopg2
import csv