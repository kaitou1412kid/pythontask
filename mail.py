import smtplib

port = 1025
smtp_server = "localhost"
sender_email = "my@mail.com"
receiver_mail = "your@mail.com"

message = '''
From : Person <my@mail.com>
To: Person <your@mail.com>
Subject: SMTP e-mail test

This is a test email message.
'''

try:
    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(sender_email,receiver_mail,message)
    print("Email sent succesfully")
except smtplib.SMTPException:
    print("Error:unable to send email")

