# Weather Data ETL Project

This project involves a Python script that performs an Extract, Transform, Load (ETL) process for weather data. The script retrieves current weather information for a specified location and stores this data in an AWS S3 bucket.

## Key Components and Functionalities

### 1. Data Extraction
- Utilizes the `requests` library to make an API call to OpenWeatherMap API.
- Retrieves current weather data for London, using an API key.

### 2. Data Transformation
- Parses the JSON response to extract relevant weather information, including:
  - City ID
  - City name
  - Timezone
  - Temperature
  - Humidity
  - Wind speed
- Converts the timestamp into a readable date and time format using `datetime`.

### 3. Data Loading
- Converts the data into a pandas DataFrame for easier manipulation.
- Checks for an existing `current_weather_data.csv` file in an AWS S3 bucket.
- Appends new data to the existing file or creates a new file if it doesn't exist.

### 4. AWS S3 Integration
- Uses Boto3 library for interacting with the S3 service.
- Handles reading from and writing data to the S3 bucket.

### 5. Error Handling
- Includes handling for scenarios where the S3 file does not exist, creating a new file as needed.

### 6. Use Case
- Can be scheduled for regular execution, enabling continuous weather data collection.
- Useful for applications such as weather trend analysis, forecasting, or integration into larger data systems.

## Conclusion
This project demonstrates efficient gathering, processing, and storage of external API data using Python, pandas, and AWS S3, exemplifying automated data pipeline processes for real-time data feeds.
