import requests
import json
import datetime
print("Creating a space or a room")
print ("Current date and time: ")
print(datetime.datetime.now())
#Get the personal access token at https://developer.webex.com/docs/api/v1/rooms/create-a-room
current_access_token = "ZmRjY2E0OTMtNmNkZS00N2E5LTk1MjMtZThmMDIzOGMwMWNhMDg0ZDg1NjctNmE3_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921"
access_token = current_access_token
url = 'https://api.ciscospark.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
#
payload={"title": "TalTech Scripting Languages"}
# body argument: "data= " or "json= " => "json= " is more specific than "data= "
res = requests.post(url, headers=headers, json=payload)
print('--------------------------------')
print("URL: " + url)
print('Header: ' + json.dumps(headers))
print("Return Code: " + str(res.status_code))
print('--------------------------------')
#print(res.json())
# Keeping SPACE_ID for later use
NEW_SPACE_ID = res.json()["id"]
print("NEW SPACE ID: " + NEW_SPACE_ID )
print('--------------------------------')
print(json.dumps(res.json(), indent=2))
print('--------------------------------')

room_id = NEW_SPACE_ID # Make sure you add the room ID value that was returned from the previous call you made
person_email = 'bbaheer@tlu.ee' # Add the email address of someone with a Webex Teams account
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
payload = {'roomId': room_id, 'personEmail': person_email}
# body argument: "data= " or "json= " => "json= " is more specific than "data= "
res = requests.post(url, headers=headers, json=payload)
print('--------------------------------')
print("URL: " + url)
print('Header: ' + json.dumps(headers))
print("Return Code: " + str(res.status_code))
MEMBER_ID = res.json()['id']
print("Member Id: " + MEMBER_ID)
# if user exists
# HTTP Status Code 409: The request could not be completed due to a conflict with the current state of the target resource.
print('--------------------------------')
#
#print("Displaying all returned information in text format")
#print("Return Text: " + str(res.text))
#print('--------------------------------')
#print("Displaying all returned information in raw JSON format")
#print(res.json())
#print('--------------------------------')
#
print(json.dumps(res.json(), indent=2))

## This is your Markdown message
message = '**First Homework Assignment**\n'
message += '**https://classroom.github.com/homework4**\n'
message += '**Please push your solutions to this repo.**\n'
#message = '**Alert**: Site under attack'
#message = '**Notification**: Attack averted'
#
#
url = 'https://api.ciscospark.com/v1/messages'
#
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
#
payload  = {'roomId': room_id, 'markdown': message}
# other example: body = { 'toPersonEmail': 'tofrench@webex.bot', 'text': 'Hello' }
#
# body argument: "data= " or "json= " => "json= " is more specific than "data= "
res = requests.post(url, headers=headers, json=payload)
print('--------------------------------')
#
print("URL: " + url)
print('Header: ' + json.dumps(headers))
print("Return Code: " + str(res.status_code))
#
#
#print("Displaying all returned information in text format")
#print("Return Text: " + str(res.text))
#print('--------------------------------')
#print("Displaying all returned information in raw JSON format")
#print(res.json())
#print('--------------------------------')
#
print(json.dumps(res.json(), indent=2))
