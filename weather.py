# returns current weather details 
# Response Body
# {
#     "location": {
#         "name": "Goa",
#         "region": "Goa",
#         "country": "India",
#         "lat": 15.4,
#         "lon": 73.8,
#         "tz_id": "Asia/Kolkata",
#         "localtime_epoch": 1682039872,
#         "localtime": "2023-04-21 6:47"
#     },
#     "current": {
#         "last_updated_epoch": 1682039700,
#         "last_updated": "2023-04-21 06:45",
#         "temp_c": 25.7,
#         "temp_f": 78.3,
#         "is_day": 1,
#         "condition": {
#             "text": "Partly cloudy",
#             "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#             "code": 1003
#         },
#         "wind_mph": 4.0,
#         "wind_kph": 6.5,
#         "wind_degree": 35,
#         "wind_dir": "NE",
#         "pressure_mb": 1007.0,
#         "pressure_in": 29.73,
#         "precip_mm": 0.0,
#         "precip_in": 0.0,
#         "humidity": 87,
#         "cloud": 27,
#         "feelslike_c": 28.6,
#         "feelslike_f": 83.5,
#         "vis_km": 10.0,
#         "vis_miles": 6.0,
#         "uv": 7.0,
#         "gust_mph": 6.3,
#         "gust_kph": 10.1
#     }
# }
#


# import json
import requests
# from urllib.request import urlopen

def getWeather():
    res = requests.get("http://api.weatherapi.com/v1/current.json?key=e6b47162328d4d09a5911554232104 &q=Goa&aqi=no")
    data = res.json()

    return data
