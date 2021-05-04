import pandas as pd
import time 
import requests 
import urllib
import json
import matplotlib.pyplot as plt
import plotly.express as px
import turtle

url='http://api.open-notify.org/iss-now.json'
pic= plt.imread(r'C:/Users/lado9/Desktop/Code/astronaut.gif')


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
screen=turtle.Screen()
screen.setworldcoordinates(-180,-90,180,90)
screen.register_shape('astronaut.gif')
my_turtle.screen.bgpic('world_map.gif')
my_turtle.shape('astronaut.gif')
my_turtle.setheading(45)
my_turtle.penup()
my_turtle.screen.title("ISS True Location")

while True:
  response= urllib.request.urlopen(url)
  result=json.loads(response.read())
  location=result['iss_position']
  lat= float(location['latitude'])
  lon= float(location['longitude'])
  my_turtle.goto(lon, lat)
  
  time.sleep(20)
