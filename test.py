import requests
import sys
import os
import json

def send_slack_message(message, url):
	
	#requests.post(url, json.dumps(message))
	return requests.post(url, json.dumps(message))


webhook = "https://hooks.slack.com/services/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"
SLACK_CHANNEL = "#notifications"
slack_message = {
    "channel": SLACK_CHANNEL,
    "text": "Some"
}



HOOK_URL = "https://hooks.slack.com/services/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"
send_slack_message(slack_message, webhook)

#requests.post(HOOK_URL, json.dumps(slack_message))
