#!/usr/bin/env python3
from flask import Flask, request
import boto3

app = Flask("flask_app")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    sns = boto3.client('sns', region_name='us-east-1')
    msg = f"IP: {request.remote_addr} URL: {request.url} UA:{request.user_agent.string}"[:139]
    sns.publish(
            TopicArn='arn:aws:sns:us-east-1:795755361461:honeypot-tripped-notifications',
            Message=msg
            )
    return "Hello, world!"

app.run(host='0.0.0.0', port=8080)
