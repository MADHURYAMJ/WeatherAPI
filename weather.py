#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

def get_weather(date):
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    params = {"dt": date}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["main"]["temp"]
    else:
        return None

def get_wind_speed(date):
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    params = {"dt": date}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["wind"]["speed"]
    else:
        return None

def get_pressure(date):
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    params = {"dt": date}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["main"]["pressure"]
    else:
        return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")
        option = input("Enter your option: ")
        if option == "1":
            date = input("Enter the date: ")
            temp = get_weather(date)
            if temp is not None:
                print("The temperature for {} is {} degrees Celsius".format(date, temp))
            else:
                print("Error getting weather data for {}".format(date))
        elif option == "2":
            date = input("Enter the date: ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print("The wind speed for {} is {} meters per second".format(date, wind_speed))
            else:
                print("Error getting wind speed data for {}".format(date))
        elif option == "3":
            date = input("Enter the date: ")
            pressure = get_pressure(date)
            if pressure is not None:
                print("The pressure for {} is {} hPa".format(date, pressure))
            else:
                print("Error getting pressure data for {}".format(date))
        elif option == "0":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()


# In[ ]:




