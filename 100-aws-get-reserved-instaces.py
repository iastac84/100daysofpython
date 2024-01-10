#!/usr/bin/env python3

# Day 100 - aws-get-reserved-instaces

import boto3

def list_reserved_instances():
    # Get AWS account ID
    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity()['Account']

    # Get a list of all AWS regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Iterate through each region and list reserved instances
    for region in regions:
        ec2_client = boto3.client('ec2', region_name=region)

        reserved_instances = ec2_client.describe_reserved_instances()
        if reserved_instances['ReservedInstances']:
            for reserved_instance in reserved_instances['ReservedInstances']:
                output = (f"AWS Account ID: {account_id}, "
                          f"Region: {region}, "
                          f"Reserved Instance ID: {reserved_instance['ReservedInstancesId']}, "
                          f"Instance Type: {reserved_instance['InstanceType']}, "
                          f"Instance Count: {reserved_instance['InstanceCount']}, "
                          f"State: {reserved_instance['State']}, "
                          f"End Date: {reserved_instance['End']}")
                print(output)
        else:
            print(f"No reserved instances found in {region}.")

if __name__ == "__main__":
    list_reserved_instances()

