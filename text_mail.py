import getpass
import smtplib

HOST = 'smtp-mail.outlook.com'
PORT = 587

FROM_EMAIL = "" #Enter your outlook email
TO_EMAIL = "" #Enter receiver email
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE  = """Subject: Mail sent using python

Hi kritagya,

This is a email send using smtp from python.

Thanks,
Kritagya"""

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

smtp.sendmail(FROM_EMAIL,TO_EMAIL,MESSAGE)
smtp.quit()