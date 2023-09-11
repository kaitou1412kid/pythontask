import getpass
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'smtp-mail.outlook.com'
PORT = 587

FROM_EMAIL = "" #Enter your outlook email
TO_EMAIL = "" #enter receiver email
PASSWORD = getpass.getpass("Enter password: ")

message = MIMEMultipart("alternative")
message['Subject'] = "Mail send using python"
message["From"] = FROM_EMAIL
message["To"] = TO_EMAIL
message["Cc"] = FROM_EMAIL
message["Bcc"] = FROM_EMAIL

html = ""
with open("mail.html","r") as file:
    html = file.read()

html_part = MIMEText(html,'html')
message.attach(html_part)

smtp = smtplib.SMTP(HOST,PORT)

#ping the serer , check if server is up and running
#returns a tupple containing status code and resposne message
status_code, response = smtp.ehlo()
print("Echoing the server: ",status_code,response)

# Establish tls connection between system and server
status_code, response = smtp.starttls()
print("Starting TLS connection: ",status_code,response)

status_code, response = smtp.login(FROM_EMAIL,PASSWORD)
print("Logging in: ",status_code,response)

smtp.sendmail(FROM_EMAIL,TO_EMAIL,message.as_string())
smtp.quit()