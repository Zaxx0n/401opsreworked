#!/usr/bin/env python3
# Script: Ops 401 Class 11 Network Security Tools Part 1 of 3
# Author: Zachary Derrick                    
# Date of latest revision:  1/30/23    
# Purpose:  Begin development of my own network scanning tool.

# import libraries 
import random, sys
from scapy.all import sr1, sr, IP, ICMP, TCP

host = "10.0.0.24" 
# sport, scan port range...yeah, sport
sport = (20, 21, 22, 80)
src_port = 22
for port in sport:
    response=sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0,) 

    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
        print("Hey," + str(sport) +": is open")
    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x14:
        print("Oh my," + str(sport) +": is closed")
    else:
        print(str(port) +" is filtered and silently dropped")

