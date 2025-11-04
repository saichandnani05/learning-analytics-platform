import boto3
import pandas as pd
from pymongo import MongoClient
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'hackwhat-quiz-data'
    key = 'sample_quiz_data.csv'
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])

    summary = df.groupby(['student_id', 'course_id'])['score'].mean().reset_index()

    MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/learning_analytics"
    client = MongoClient(MONGO_URI)
    db = client.learning_analytics
    collection = db.quiz_summary

    records = summary.to_dict(orient='records')
    collection.insert_many(records)

    return {'statusCode': 200, 'body': 'ETL job completed successfully'}
