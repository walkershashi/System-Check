#!/usr/bin/env python3

import email.message
import mimetypes
import smtplib
import os

# When called with attachment 
def generate_email(sender, receiver, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, mime_subtype = mimetypes.guess_type(attachment_path)[0].split('/')
    
    with open(attachment_path, 'rb') as attach_file:
        message.add_attachment(
            attach_file.read(),
            maintype = mime_type,
            subtype = mime_subtype,
            filename = attachment_filename
        )
    
    return message

# When called without attachment
def generate_error_report(sender, receiver, subject, body):
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)
    
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()