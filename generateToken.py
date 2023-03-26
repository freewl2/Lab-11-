import requests
import json
from getpass import getpass
from requests.auth.auth import HTTPBasicAuth

USER = input('Enter your username: ')
PASS = getpass('Enter your password: ')

post_url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

resp = requests.post(post_url,
auth=HTTPBasicAuth(USER, PASS), 
headers=headers, verify=False)

response_json = resp.json()

print("\The token is:\n", resp.text)
