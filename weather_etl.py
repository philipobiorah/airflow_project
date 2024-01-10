import requests
import pandas as pandas

api_url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=775ce95223886fd4d68d7401358687d5"

#Make the API call
response = requests.get(api_url)

#Check if the request was successful
if response.status_code == 200:
    data = response.json()


print(data)