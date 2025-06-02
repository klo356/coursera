import os.path
import mimetypes
import smtplib
from email.message import EmailMessage

message = EmailMessage()
#print(message)

sender = "example@gmail.com"
recipient = "example@msn.com"
body = """Hey there!

I'm learning to send emails using Python!"""

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content(body)

#print(message)


attachment_path = os.path.expanduser("~/coursera/C6_ARWT/M3/sample.png")
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

print(mime_type)
print(mime_subtype)

with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
 
print(message)
exit(0)


app_password = "xxx"  # Use Gmail App Password

# Email content
subject = "Test Email from Python"
body = "Hello, this is a test email sent from Python using smtplib."

# Connect to Gmail SMTP server
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.set_debuglevel(1)
        server.login(sender, app_password)
        server.send_message(message)
        print("Email sent successfully!")
        server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
