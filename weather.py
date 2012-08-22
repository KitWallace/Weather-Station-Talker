#!/usr/bin/python
import urllib
import time
import conv

class Weather :
  
  substitutes = { 
     "W":"West","N":"North","S":"South","E":"East",
     "km/h":"kilometers per hour","C":"Celsius","mph":"miles per hours",
     "Mon":"Monday","Tue":"Tuesday","Wed":"Wednesday","Thu":"Thursday","Fri":"Friday","Sat":"Saturday","Sun":"Sunday",
     "NNE":"Nor Nor East","NE":"Nor East","ENE":"East Nor East","ESE":"East Sow East", 
     "SE":"Sow East" ,"SSE" :"Sow Sow East", "SSW":"Sow Sow West","SW":"Sow West","WSW":"West Sow West",
     "WNW":"West Nor West","NW":"Nor West","NNW":"Nor Nor West",
     "%":"percent"
     }

  def __init__(self,id,url,rate) :
      self.url = url
      self.id = id 
      self.ts = 0
      self.rate = int(rate)
      self.refresh()

  def refresh(self) :
    if time.time() - self.ts > self.rate :
      try :
        page = urllib.urlopen(self.url)
        report = page.readline()
        data = report.split(" ")
        self.wind_speed = data[1]
        self.gust_speed = data[2]
        self.direction = data[3]
        self.outdoor_temp = data[4]
        self.humidity = data[5]
        self.baro = data[6]
        self.last_update = time.strftime('%H:%M:%S')
        self.ts = time.time()
      except :
        pass
   else :
       pass
  
  def get_wind_speed(self) :
      self.refresh()
      dir = conv.degree_to_compass_point(int(self.direction))
      return "Wind speed "+ self.wind_speed + " knots from the "+ dir 
  
  def get_baro(self) :
      self.refresh()
      return "Barometer is " + str(int(float(self.baro))) 

  def get_temp(self) :
      self.refresh()
      return "Temperature " + self.outdoor_temp + " degrees C : humidity "  + self.humidity + "%" 
  

