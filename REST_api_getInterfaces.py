import requests
import json
import urllib3
urllib3.disable_warnings()
HOST = 'ios-xe-mgmt.cisco.com'
USER = 'developer'
PASS = 'C1sco12345'
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
# print(response.content)
interfaces = response.json()
#print(json.dumps(response.json(), indent=2))
print(interfaces['ietf-interfaces:interfaces']['interface'][0]['name'])
print(interfaces['ietf-interfaces:interfaces']['interface'][0]['ietf-ip:ipv4']['address'][0]['ip'])