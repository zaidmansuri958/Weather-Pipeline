import boto3
import json
import time


athena_client = boto3.client('athena')

DATABASE = 'wather_data_db'
TABLE = 'forecast_data'
s3_OUTPUT = 's3://zaid-weather-etl-project/athena-query-result/'


def get_query_results(query_execution_id):
    while True:
        response = athena_client.get_query_execution(
            QueryExecutionId=query_execution_id)
        state = response['QueryExecution']['Status']['State']

        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(2)

    if state == "SUCCEEDED":
        result_response = athena_client.get_query_results(
            QueryExecutionId=query_execution_id)
        rows = result_response["ResultSet"]["Rows"]

        results = []

        for row in rows[1:]:
            results.append({
                "date": row["Data"][0]["VarCharValue"],
                "max_temp": row["Data"][1]["VarCharValue"],
                "min_temp": row["Data"][2]["VarCharValue"],
                "weather_condition": row["Data"][3]["VarCharValues"],
            })
        return results

    else:
        return {"error": f"Query failed with state: {state}"}


def lambda_handler(event, context):
    query = f"SELECT date,max_temp,min_temp,weather_condition FROM {DATABASE}.{TABLE} ORDER BY date desc LIMIT 7 ;"

    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": s3_OUTPUT}
    )

    query_execution_id = response["QueryExecutionId"]

    weather_data = get_query_results(query_execution_id)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
        "body": json.dumps(weather_data),
    }
