#!/usr/bin/env python3

# import time, datetime
# import os
# import logging
import smtplib, ssl
from email.message import EmailMessage
# from getpass import getpass
from decouple import config


#email variables
email_sender = config("email", default='') 
email_password = config("password", default='')
email_receiver = input("Please enter a valid email to recieve status updates:") or "recyclops1970@gmail.com"
subject = "This is a test"
body = """Did you get this?"""
#  email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

