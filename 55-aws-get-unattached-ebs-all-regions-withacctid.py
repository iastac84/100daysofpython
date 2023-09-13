#!/usr/bin/env python3
# Day 55

"""
Python script to list all unattached EBS volumes in an AWS account, all regions
Export/set AWS credentials before running
Also set AWS_REGION and AWS_DEFAULT_REGION
Updated to include AWS account ID
"""

import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Get the AWS account ID
account_id = boto3.client('sts').get_caller_identity()['Account']
print(f"AWS Account ID: {account_id}")

# Get a list of all regions
all_regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

# Loop through all regions
for region in all_regions:
    print(f"Region: {region}")
    
    # Initialize a client for the current region
    ec2 = boto3.client('ec2', region_name=region)
    
    # Get all the volumes in the current region
    volumes = ec2.describe_volumes()
    
    # Filter for unattached volumes
    unattached_volumes = [v for v in volumes['Volumes'] if v['State'] == 'available']
    
    # Print the tags for each unattached volume
    for volume in unattached_volumes:
        if 'Tags' in volume:
            tags = [f"{t['Key']}={t['Value']}" for t in volume['Tags']]
            tag_string = ', '.join(tags)
            print(f"Volume ID: {volume['VolumeId']} : Size (GiB): {volume['Size']} : AZ: {volume['AvailabilityZone']} : Type: {volume['VolumeType']} : Created: {volume['CreateTime']} : AWS Account ID: {account_id} : Tags: {tag_string}")

        else:
            print(f"Volume ID: {volume['VolumeId']} : Size (GiB): {volume['Size']} : AZ: {volume['AvailabilityZone']} : Type: {volume['VolumeType']} : Created: {volume['CreateTime']} : AWS Account ID: {account_id} : Tags: None")

