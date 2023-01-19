#!/usr/bin/env python3
# Script:   Ops 401 Class 02 Uptime Sensor Tool Part 1 of 2
# Author:   Zachary Derrick                    
#           Date of latest revision:  2023-01-17    
# Purpose:  Review and improve (when possible) previous
#           code that was to write an uptime sensor tool that 
#           checks systems are responding. Added a logging feature.
# Props to: Watched this tutorial for logging https://www.youtube.com/watch?v=urrfJgHwIJA&ab_channel=TechWithTim


# import libraries

import time, datetime, os, logging, sys


# declares variables 
hostname = input("Enter an IP address to check: ") or "8.8.8.8"
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%-H_%M_%S_%p")
# this variable needed to be added for the log, but also it's important to declare it before the main
ping_results = ()
 
# declare functions
# the function "updog" checks if a host is currently up(reachable) or down(unreachable)
def updog(ping_results):
    status = os.system("ping -c 1 " + hostname)  
    if status == 0:
            ping_results = f"host {hostname} is reachable"
            print("The host", hostname, "is reachable:", timestamp)
            return ping_results
    else: 
            ping_results = f"host {hostname} is unreachable"
            print("The host", hostname, "is unreachable:", timestamp)
            return ping_results
               
# main
while True:
    updog(ping_results)
    time.sleep(2)
    status_of_host = updog(ping_results)
    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO, filename="uptime_status.log", filemode="a",
                        format="%(asctime)s -%(levelname)s -%(message)s")
        logging.info(f"Target status: {status_of_host}")
# end
