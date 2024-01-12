import requests
import pandas as pd
import datetime as dt
import os
import boto3
from io import StringIO
from dotenv import load_dotenv

def run_weather_etl():
    load_dotenv()
    api_url = os.environ.get('API_URL')
    weather_data_list = [] 

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

    # Convert to DatFrame
    df = pd.DataFrame(weather_data_list)

    #### when writing to 'current_weather_data.csv'###
    # # Check if file exists to determine if header is needed
    # file_exists = os.path.isfile('current_weather_data.csv')
    # # Append data to CSV file
    # df.to_csv('current_weather_data.csv', mode='a', header=not file_exists, index=False)


    #print(df)

    #S3 Bucket and file name
    bucket = 'philip-airflow-weather-bucket'
    file_name = 'current_weather_data.csv'

    #Create S3 client
    s3_client = boto3.client('s3')

    # Read existing file form S3
    try:
        obj = s3_client.get_object(Bucket=bucket, Key=file_name)
        existing_df = pd.read_csv(obj['Body'])
        all_data = pd.concat([existing_df, df])
    except s3_client.exceptions.NoSuchKey:
        all_data = df    

    # Convert DataFrame to CSV
    csv_buffer = StringIO()
    all_data.to_csv(csv_buffer, index=False)

    #Write back to S3
    s3_client.put_object(Bucket=bucket, Key=file_name, Body=csv_buffer.getvalue())


    # df.to_csv('s3://philip-airflow-weather-bucket/current_weather_data.csv')

#run_weather_etl()