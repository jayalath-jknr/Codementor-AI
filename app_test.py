import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

body = {
	"parameters": {
		"decoding_method": "greedy",
		"max_new_tokens": 200,
		"repetition_penalty": 1
	},
	"model_id": "ibm/granite-20b-code-instruct",
	"project_id": "8719a597-19da-440a-8a0b-e7738acef74d"
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer OVb53rKYk7sfOLWeC2F0RGZj3YrxKGKg9W5YiVZM8xhp"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()