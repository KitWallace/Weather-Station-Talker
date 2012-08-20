#!/usr/bin/python
import sys
import subprocess
import speak
from menu import *
from weather import *

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      target = item.getAttribute("target")
      target = targets[target]
      text = eval(action)
   say_text = speak.expand(text,Weather.substitutes)
   print text
   speak.say(speak.ssml_break(300)+say_text) # start with a bit of silance
 
targets = {}
name = sys.argv[1]
menu = Menu(name)

#create each station in the menu
for item in menu.root.childNodes :
   name = item.getAttribute("name")
   url = item.getAttribute("url")
   station = Weather(name,url,30)
   targets[name] = station

menu.run(visit)


