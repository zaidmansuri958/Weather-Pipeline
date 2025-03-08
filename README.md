# Weather Forecast ETL Pipeline

## Overview
This project implements an ETL (Extract , Transform , Load) pipeline using AWS services to fetch data from [Yahoo weather API](https://rapidapi.com/apishub/api/yahoo-weather5) , process it , and store data and push data to AWS . The project shows weather forcast for ahmedabad city which get automatically updates each day with AWS trigger.

## Architecture
The pipeline follows a structured ETL process:
  1. **Extract:** AWS Lambda extracts data from the Weather API.
  2. **Transform:** The extracted data is processed and structured using AWS Lambda.
  3. **Load:** Transformed data is stored in Amazon S3, with schema inference using AWS Glue, enabling querying through Amazon Athena.


### Architecture Diagram
![Architecture](/Architecture/architecture.png)

## Tech Stack
- AWS Services: Lambda, S3, Glue, Athena, CloudWatch
- Programming Language: Python
- Yahoo Weather API: Weather Forcast Data
- Data Processing: Pandas, JSON , numpy

## Folder Structure
```
weather_etl_pipeline/
├── backend/
      ├── lambda_function/
                ├── get_weather_data.py               # AWS Lambda function to extract data and push to API
                ├── weather_data_extract_lambda.py    # AWS Lambda function to extract data from weather API
                ├── weather_data_transform_lambda.py  # AWS Lambda function to transform data 
├── pipeline/
      ├── weather data pipeline project.ipynb     
├── README.md                                         # Project documentation
```

## ☁️ AWS Components
- Amazon CloudWatch: ⏰ Triggers the Lambda function to extract Spotify data on a schedule.
- AWS Lambda (Extraction): 🏗️ Fetches raw data from the weather API and stores it in S3.
- Amazon S3 (Raw Storage): 📦 Stores extracted JSON data.
- AWS Lambda (Transformation): 🔄 Processes and structures the data into tables.
- Amazon S3 (Processed Storage): 📂 Stores the transformed CSV data.
- AWS Glue Crawler: 🔍 Infers the schema of transformed data.
- AWS Glue Data Catalog: 📖 Stores metadata for querying in Athena.
- Amazon Athena: 📊 Enables SQL-based querying of processed Spotify data.

---

## ScreenShots

![Extract](/Architecture/lambda_extract.PNG)

![Transform](/Architecture/lambda_transform.PNG)

![Athena](/Architecture/lambda_athena.PNG)

![S3](/Architecture/s3.PNG)

![Athena](/Architecture/athena.png)
