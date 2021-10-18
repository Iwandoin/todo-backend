import requests
import sys
import os
import json

def lambda_handler(event, context):
	print('## EVENT')
	print(event)
	slack_message = {"channel": "#notifications", "text": "Something"}
	HOOK_URL = "https://hooks.slack.com/services/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"
	requests.post(HOOK_URL, json.dumps(slack_message))
	print("test")
	return requests.post(HOOK_URL, json.dumps(slack_message))
	
