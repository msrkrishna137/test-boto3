#!/usr/bin/python

import boto3 
aws_man_con=boto3.session.Session(profile_name="default")
iam_con=aws_man_con.resourse('iam')

for each_user in iam_con.users.all():
    print(each_user.name)