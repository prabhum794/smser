from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC10124c1df24da21a6b0c0d273ba1d39d"
auth_token  = "348faa4aff3333050cd346f6f4dbdfb1"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+919962940636",    # Replace with your phone number
    from_="+19172439254") # Replace with your Twilio number
print(message.sid)