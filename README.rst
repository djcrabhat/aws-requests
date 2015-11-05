
aws-requests
================
making AWS4-HMAC-SHA256 signed HTTP calls with requests 


python::

    from awsrequests import AwsRequester
        
    req = AwsRequester("us-west-2")
    req.get("http://myapigateway.whatever.com/")
    req.post("http://myapigateway.whatever.com/",json=dict(my="data")

Credentials
------
AwsRequester can either have a key and secret passed in, or it will try to find creds in the same way boto3 would.