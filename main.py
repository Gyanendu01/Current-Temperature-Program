import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=0e244906bfea4aa4a2b23637240805&q={city}&aqi=no"
engine = pyttsx3.init()
r = requests.get(url)
print("Current Temperature of your Location in celcius and farenheit is: ")
wdic = json.loads(r.text)
print(wdic['current']['temp_c'])
print(wdic['current']['temp_f'])
engine.say(f"Current Temperature of your Location is degrees Celsius is: {wdic['current']['temp_c']} celcius") 
engine.say(f"Current Temperature of your Location is degrees farenheit is: {wdic['current']['temp_f']} farenheit") 
engine.runAndWait()