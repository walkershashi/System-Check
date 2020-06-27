#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket
import os

SENDER = 'automation@example.com'
RECEIVER = 'username@example.com'
BODY = "Please check your system and resolve the issue as soon as possible."

cpu_usage = psutil.cpu_percent()
disk_usage = shutil.disk_usage("/")
# Check CPU Usage
if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(SENDER, RECEIVER, subject, BODY)
    emails.send_email(message)

# Check Disk Usage
if disk_usage[2] / disk_usage[0] < 0.2:
    subject = "Error - Available disk space is less than 20%" 
    message = emails.generate_error_report(SENDER, RECEIVER, subject, BODY)
    emails.send_email(message)

# Check Memory Availability
if disk_usage[2] / (10**6) < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(SENDER, RECEIVER, subject, BODY)
    emails.send_email(message)

# Check Host Name Resolvability
if socket.gethostbyname('localhost') != '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    message = emails.generate_error_report(SENDER, RECEIVER, subject, BODY)
    emails.send_email(message)