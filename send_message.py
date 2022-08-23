import os
from twilio.rest import Client
import sys

input_message = sys.argv[1]



account_sid = 'ACfa5d43a548a154b8640d6b03dbc99f5b'

auth_token = '03d255ad98d9a25b9c5f09c3e9fd419e'

client = Client(account_sid, auth_token)

message = client.messages.create(
                     body=input_message,
                     from_='+13392158533',
                     to='+821048279723'
                 )

print(message.sid)
