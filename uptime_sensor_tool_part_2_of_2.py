#!/usr/bin/env python3
# Script:   Ops 401 Class 02 Uptime Sensor Tool Part 2 of 2
# Author:   Zachary Derrick                    
#           Date of latest revision:  2023-01-17    
# Purpose:  Review and improve (when possible) previous
#           code that was to write an uptime sensor tool that 
#           checks systems are responding. Added a logging feature.
#           Part 2 adds an email notification functionality.
# Props to: Watched this tutorial for logging https://www.youtube.com/watch?v=urrfJgHwIJA&ab_channel=TechWithTim


# import libraries

import time, datetime
import os
import logging
import smtplib, ssl
from email.message import EmailMessage
# from getpass import getpass
from decouple import config


# welcome screen
print("Welcome to Uptime Sensor Tool v3\n")
hostname = input("Enter an IP address to monitor: \n") or "10.0.0.24"

# declares variables 
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%-H_%M_%S_%p")
last_ping = None
ping_results = None
status = "start"
subject = None
body = None


#email variables
email_sender = config("email", default='') 
email_password = config("password", default='')
email_receiver = input("Please enter a valid email to recieve status updates:") or "recyclops1970@gmail.com"
#  email message
# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()


# declare functions

# the function "updog" checks if a host is currently up(reachable) or down(unreachable)
def updog(ping_results, status):
    status = os.system("ping -c 1 " + hostname)  
    if status == 0:
            ping_results = f"host {hostname} is reachable"
            print("The host", hostname, "is reachable:", timestamp)
            return ping_results, status
    else: 
            ping_results = f"host {hostname} is unreachable"
            print("The host", hostname, "is unreachable:", timestamp)
            return ping_results, status


# sending the emails
# def sendmail():
   
#  email message
 

def initiate_message():
    if ping_results == None:
        subject = f"You've started a new monitoring session."
        body = f"""Monitoring of {hostname} has started. """ + timestamp
        
    elif status == 0:
        subject = "ALERT: Host is available."
        body = f"""The host: {hostname} is now up. """ + timestamp
      
    elif status == 1:
        subject = "ALERT: Host is unavailable."
        body = f"""The host: {hostname} is now down. """ + timestamp
   
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
  

def add_to_log():
      if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO, filename="uptime_status.log", filemode="a",
                        format="%(asctime)s -%(levelname)s -%(message)s")
        logging.info(f"Target status: {status}")

# main


while True:
    if status == "start":
        initiate_message()
    updog(ping_results, status)
    if status != last_ping:
        initiate_message()
        # sendmail()
    last_ping = status
    add_to_log()
    time.sleep(10)

# end


# def statuscheck():
#     if ping_status != True & last_ping == False:
#         sendmail()
#     if ping_status == False & last_ping == True:
#         sendmail()


# def getlastping():
#     if ping_status == True:
#         last_ping = "up"
#     else : 
#         last_ping = "down"
# def start_message_mail():
#     message = f"You have started the Uptime Sensor to monitor: {hostname}"
#     sendmail()
     







