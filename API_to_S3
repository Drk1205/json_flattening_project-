--1.Create S3 Bucket - - - – -> s3api-call
--2.Create an AWS Lambda function
--Step-by-Step Setup in Console
-- Go to AWS Console --> Lambda.
-- Click “Create function”
-- Choose:
--Function name: apitos3
-- Runtime: Python 3.11
 --Architecture: x86_64
--Permissions:
 --Go to IAM - - - –>  Role - - - ->  create role- - - > lambda-s3-uploader-role
--Attach Permission Policies AmazonS3FullAccess
--Create Role
--Attach Role To lambda Function:
--3. Put the Python code in the source code of our lambda function

import json
import urllib.request
import boto3
from datetime import datetime

# Create an S3 client
s3 = boto3.client('s3')

# >>> CHANGE THIS to your bucket name <<<
BUCKET_NAME = "s3api-call"

def lambda_handler(event, context):
    """
    Fetch jobs from Arbeitnow API and save them as a timestamped JSON file in S3.
    Returns a simple statusCode/body response for CloudWatch logs / testing.
    """
    url = "https://www.arbeitnow.com/api/job-board-api"

    try:
        # Call the public API and parse JSON
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        # Extract the 'data' list from the API response
        job_data = data.get("data", [])

        if not job_data:
            return {
                "statusCode": 404,
                "body": "No jobs found"
            }

        # Pretty JSON string
        json_str = json.dumps(job_data, indent=4)

        # Timestamped filename under a 'job/' prefix
        timestamp_str = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"job/arbeitnow_jobs_{timestamp_str}.json"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=json_str.encode("utf-8"),
            ContentType="application/json"
        )

        # Return success message
        return {
            "statusCode": 200,
            "body": f"Uploaded file to S3 as {filename}"
        }

    except Exception as e:
        # Correct indentation for except block
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }


