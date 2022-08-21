import os
from twilio.rest import Client

os.system("./run.sh 03_clustering/test_set 256 LSE1 128 1 0.001 0.05 128")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = 'ACfa5d43a548a154b8640d6b03dbc99f5b'

auth_token = '470a3a3971948a412258d10111895622'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Python twilio trial is successful",
                     from_='+13392158533',
                     to='+821048279723'
                 )

print(message.sid)
