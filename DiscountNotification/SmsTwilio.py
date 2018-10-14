from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5c7c97ed198be162ed13c2d4eb2d0bce"
# Your Auth Token from twilio.com/console
auth_token  = "f67580d4bb72a771920859febe6b1e35"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918185039662",
    from_="+18649000628", 
    body="hie")

print(message.sid)