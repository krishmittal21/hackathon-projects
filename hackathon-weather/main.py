import argparse
import pyfiglet
from simple_chalk import chalk
import requests
# API key for openweathermap
API_KEY="0e1c4740f95a2a0f0093a52a7d6195d8"
#Base URL fro openweathermap API
#github copilot wrote this for me
BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
# Map weather  codes to weather icons
#github copilot wrote this for me

WEATHER_ICONS={
    #day icons
    "01d":"☀️",
    "02d":"🌤",
    "03d":"🌥",
    "04d":"☁️",
    "09d":"🌧",
    "10d":"🌦",
    "11d":"🌩",
    "13d":"🌨",
    "50d":"🌫",
    #night icons
    "01n":"🌙",
    "02n":"🌤",
    "03n":"🌥",
    "04n":"☁️",
    "09n":"🌧",
    "10n":"🌦",
    "11n":"🌩",
    "13n":"🌨",
    "50n":"🌫",
}
# Construct API url with query parameters
#github copilot wrote this for me

parser=argparse.ArgumentParser(description="Weather Forecast")
parser.add_argument("city",help="City name")
args=parser.parse_args()
url=f"{BASE_URL}q={args.city}&appid={API_KEY}&units=metric"
#Make API call
response=requests.get(url)
if response.status_code!=200:
    print(chalk.red("Error: Unable to retrieve data"))
    exit()
#Parse response
data=response.json()
# get info from data
#github copilot wrote this for me

temperature=data["main"]["temp"]
feels_like=data["main"]["feels_like"]
description=data["weather"][0]["description"]
icon=data["weather"][0]["icon"]
city=data["name"]
# contruct output
#github copilot wrote this for me

weather_icon=WEATHER_ICONS.get(icon,"")
output =f"{pyfiglet.figlet_format(city)}\n\n"
output +=f"{weather_icon} {description}\n"
output +=f"Temperature: {temperature}°C\n"
output +=f"Feels like: {feels_like}°C\n"
# print output
#github copilot wrote this for me

print(chalk.green(output))
