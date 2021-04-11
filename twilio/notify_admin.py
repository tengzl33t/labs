import os
from twilio.rest import Client

# Login to Twilio and get your account_sid and authentication token
account_sid = '<Add your SID>'
auth_token = '<Add the Authenticaiton Token>'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    # Add the phone numbers
    to="",
    from_="",
    body="Greetings from a server!")