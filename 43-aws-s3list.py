#!/usr/bin/env python3
# Day 43

"""
Python script to list all S3 buckets in an AWS account:
"""

import boto3

def list_s3_buckets():
    # Create a Boto3 S3 client
    s3_client = boto3.client('s3')

    try:
        # Call the 'list_buckets' API to get the bucket list
        response = s3_client.list_buckets()

        # Extract bucket names from the response
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]

        return bucket_names

    except Exception as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    # Call the function to list S3 buckets
    bucket_list = list_s3_buckets()

    if bucket_list:
        print("List of S3 Buckets:")
        for bucket in bucket_list:
            print(bucket)
    else:
        print("No buckets found in the AWS account.")


