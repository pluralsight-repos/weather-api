import requests

city = 'New York'
url = 'http://api.weatherapi.com/v1/current.json?key=5f4604d56fde475db96194007241805&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json()

# print(weather_json)

temp = weather_json['current']['temp_c']
description = weather_json['current']['condition']['text']

print(f"Today's weather in {city} is", description, 'and', temp,"degrees.")

temp1 = weather_json.get('current').get('temp_c')
description1 = weather_json.get('current').get('condition').get('text')

print(f"Today's weather in {city} is", description1, 'and', temp1,"degrees.")





