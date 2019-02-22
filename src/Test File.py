pip install twilio
python send_sms.py
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15017122661',
         to='+15558675310'
     )

print(message.sid)
"subresource_uris": {"media": "/2010-04 01/Accounts/ACxxxxxxxx/Messages/SMxxxxxxxxxxxxx/Media.json"}
print(message.media._uri)
python send_mms.py
