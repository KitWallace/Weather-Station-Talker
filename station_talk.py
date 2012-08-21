#!/usr/bin/python
import sys
import subprocess
import speak
from menu import *
from weather import *

stations = {}
def station(name) :
   try :
      station = stations[name]
      return station
   except :
      station_item = menu.item(name)
      url = station_item.getAttribute("url")
      refresh = station_item.getAttribute("refresh")
      station = Weather(name,url,refresh)
      stations[name] = station
      return station

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   say_text = speak.expand(text,Weather.substitutes)
   print text
   speak.say(say_text) 

menu_name = sys.argv[1]
menu = Menu(menu_name)

menu.run(visit)


