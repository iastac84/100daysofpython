#!/usr/bin/env python3
# Day 51

"""
Python script to list all enabled regions in your AWS account and, for each region, it will list the availability zones along with their status
"""

import boto3

def list_regions_and_azs():
    # Create a Boto3 client for EC2
    ec2_client = boto3.client('ec2')
    
    # List all regions
    regions = ec2_client.describe_regions()['Regions']
    
    for region in regions:
        region_name = region['RegionName']
        print(f"Region: {region_name}")
        
        # Create a Boto3 client for the specific region
        ec2_region_client = boto3.client('ec2', region_name=region_name)
        
        # List availability zones in the region
        azs = ec2_region_client.describe_availability_zones()['AvailabilityZones']
        
        for az in azs:
            print(f"  Availability Zone: {az['ZoneName']} ({az['State']})")

if __name__ == "__main__":
    list_regions_and_azs()

