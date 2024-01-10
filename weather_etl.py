import requests
import pandas as pd
import datetime as dt

weather_data_list = [] 

def run_weather_etl():

    #api_url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=775ce95223886fd4d68d7401358687d5"
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=775ce95223886fd4d68d7401358687d5"
    #Make the API call
    response = requests.get(api_url)

    #Check if the request was successful
    if response.status_code == 200:
        data = response.json()



    #Extract data and store in a DataFrame
    
    weather_data = {
    'id': data['id'],   
    'city':data['name'],
    'timezone': data['timezone'],
    'temperature':data['main']['temp'],
    'humidity':data['main']['humidity'],
    'windspeed': data['wind']['speed'],
    'date':dt.datetime.utcfromtimestamp(data['dt']).strftime("%Y-%m-%d"),
    'time': dt.datetime.utcfromtimestamp(data['dt']).strftime("%H:%M:%S")
    }

    weather_data_list.append(weather_data)

    df = pd.DataFrame(weather_data_list)

    print(df)
    df.to_csv('current_weather_data.csv')
    
    
    
run_weather_etl()