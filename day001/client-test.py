#!/usr/bin/python
import boto3 

aws_man_con=boto3.session.Session(profile_name="default")
iam_con=aws_man_con.client(service_name='iam', region_name='us-east-1')

for each_user in iam_con.list_users()['Users']:
    print(each_user['UserName'])
