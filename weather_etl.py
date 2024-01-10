import requests
import pandas as pd


#api_url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=775ce95223886fd4d68d7401358687d5"
api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=775ce95223886fd4d68d7401358687d5"
#Make the API call
response = requests.get(api_url)

#Check if the request was successful
if response.status_code == 200:
    data = response.json()


for x,y in data.items():
    print(x,y)
#Extract data and store in a DataFrame
weather_data = {
'id': data['id'],   
'city':data['name'],
'timezone': data['timezone'],
'temperature':data['main']['temp'],
'humidity':data['main']['humidity'],
'windspeed': data['wind']['speed'],
'timestamp': data['dt']

}

df = pd.DataFrame([weather_data])

print(df)
    
    
    
