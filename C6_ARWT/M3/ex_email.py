from email.message import EmailMessage

message = EmailMessage()
#print(message)

sender = "me@example.com"
recipient = "you@example.com"
body = """Hey there!

I'm learning to send emails using Python!"""

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content(body)


print(message)