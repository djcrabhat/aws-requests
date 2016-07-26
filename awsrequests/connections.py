#!/usr/bin/env python

from botocore.exceptions import ClientError
import boto3

class AWSConnections(object):
    def __init__(self, **kwargs):
        self.args = kwargs
        if 'client' in self.args['resource']:
            self.client = self.setClient()
        else:
            self.client = self.setResource()

    def setClient(self):
        self.client = boto3.client(self.args['aws_asset'], region_name=self.args['region'])
        return self.client

    def setResource(self):
        self.client = boto3.resource(self.args['aws_asset'], region_name=self.args['region'])
        return self.client

    def setArn(self):
        self.arn = "arn:aws:iam::{0}:role/{1}".format(
                self.args['aws_account'],
                self.args['role']
                )
        return self.arn

    def assumeAccount(self):
        client = boto3.client('sts')
        self.temp_creds = client.assume_role(
                RoleArn=self.setArn(),
                RoleSessionName=self.args['role_name']
                )
        self.client = boto3.client(
                self.args['aws_asset'],
                aws_access_key_id=self.temp_creds["Credentials"]["AccessKeyId"],
                aws_secret_access_key=self.temp_creds["Credentials"]
                                                     ['SecretAccessKey'],
                aws_session_token=self.temp_creds["Credentials"]["SessionToken"],
                region_name=self.args['region']
                )
        return self.client
