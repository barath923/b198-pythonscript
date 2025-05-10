import boto3

client = boto3.client('ec2')

response = client.create_vpc(
    CidrBlock='10.10.0.0/16',
    TagSpecifications=[
        {
            'ResourceType':'vpc',
		      	'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'VPC-NEW'
                }
            ]
        }
    ]
)

print ("VPC ID: ", response['Vpc']['VpcId'])
