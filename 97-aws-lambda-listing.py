import boto3
import os

def list_lambda_functions():
    # Set the AWS profile using the environment variable
    aws_profile = os.environ.get('AWS_PROFILE')

    # Create a Boto3 session using the specified profile
    session = boto3.Session(profile_name=aws_profile)
    
    # Get AWS account ID
    sts_client = session.client('sts')
    account_id = sts_client.get_caller_identity()['Account']
    
    # Get all AWS regions
    ec2 = session.client('ec2')
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    
    # Iterate through each region and list Lambda functions
    for region in regions:
        print(f"Lambda functions in {region} (Account ID: {account_id}):")
        lambda_client = session.client('lambda', region_name=region)
        response = lambda_client.list_functions()
        
        functions = response.get('Functions', [])
        for func in functions:
            function_name = func['FunctionName']
            runtime = func['Runtime']
            print(f"  {function_name} - Runtime: {runtime}")

if __name__ == "__main__":
    list_lambda_functions()

