#live weather reporting
import requests
api_address='https://api.openweathermap.org/data/2.5/weather?appid=b3c37ca365210e7900ea4aa7c99c50d2&q='
city=input("city name:")
url=api_address+city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
print(formatted_data)
