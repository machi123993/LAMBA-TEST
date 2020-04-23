import json
import boto3
import argparse

def list_instances_by_tag_value(tag1,val1,tag2,val2,region):
    # When passed a tag key, tag value this will return a list of InstanceIds that were found.
    ec2 = boto3.client('ec2',region)
    filters = [
         {
         'Name': 'tag:'+tag1,
         'Values': [val1]
            },
          {
         'Name': 'tag:'+tag2,
         'Values': [val2]
            }
]
    res = ec2.describe_instances(Filters=filters)
    instancelist = []
    for reservation in (res["Reservations"]):
        for instance in (reservation['Instances']):
            x = instance['InstanceId']
            instancelist.append(x)
    print(instancelist)
    for id in instancelist:
       print(id)
       ssm_client = boto3.client('ssm',region) # use region code in which you are working
       response = ssm_client.send_command(
                    InstanceIds=[ id ],
                    DocumentName="test")
       command_id = response['Command']['CommandId']
       print(command_id)
       time.sleep(2)
       output = ssm_client.get_command_invocation(
             CommandId=command_id,
             InstanceId=id,
           )
       print(output)

def list_instanceid(event, context):
    tag1 = event["tag1"]
    val1 = event["val1"]
    tag2 = event["tag2"]
    val2 = event["val2"]
    region = event["region"]
    list_instances_by_tag_value(tag1,val1,tag2,val2,region)

