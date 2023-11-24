import boto3

def get_elastic_ips_all_regions():
    ec2 = boto3.client('ec2')
    
    # Get all AWS regions
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

    elastic_ips = []

    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        
        # Describe Elastic IP addresses in the current region
        addresses = ec2.describe_addresses()

        for address in addresses['Addresses']:
            if 'PublicIp' in address:
                elastic_ips.append(address['PublicIp'])

    return elastic_ips

if __name__ == "__main__":
    elastic_ips = get_elastic_ips_all_regions()
    
    if elastic_ips:
        print("Elastic IP addresses in all AWS regions:")
        for ip in elastic_ips:
            print(ip)
    else:
        print("No Elastic IP addresses found in any AWS region.")

