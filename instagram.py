#! /user/bin/env python3
import imaplib
import email
import base64
import os
import sys
import mimetypes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#log in information
emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")
# instagramAddress = os.environ.get('instagram_email')
# instagramPW = os.environ.get('instagram_password')
SMTP_SERVER = "imap.gmail.com"
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(emailAddress, password)
time.sleep(1)
# select inbox
mail.select("INBOX")
# finding emails sent from myself
result, messageFromMe = mail.search(None, 'FROM', '"therealnicola@gmail.com"')
mailList = messageFromMe[0].split()
# reading each item
for item in mailList:
    result, data = mail.fetch(item, '(RFC822)')
    rawEmail = data[0][1].decode("utf-8")
    emailMessage = email.message_from_string(rawEmail)
    to_ = emailMessage['To']
    from_ = emailMessage['From']
    subject_ = emailMessage['Subject']
    date_ = emailMessage['Date']
    counter = 0
    for part in emailMessage.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename()
        contentType = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(contentType)
            if not ext:
                ext = '.bin'
            filename = 'msg-part-%08d%s' % (counter, ext)
        counter += 1
    # saving the file
    savePath = os.path.join(os.getcwd(), "emails/uploads", )
    if not os.path.exists(savePath):
        # make path if it doesnt exist
        os.makedirs(savePath)
    with open(os.path.join(savePath, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))
    # saving the subject as a text file
    with open(os.path.join(savePath, 'text.txt'), 'w') as fp:
        fp.write(subject_)
    # Change the flag to deleted and delete
    typ, response = mail.store(item, '+FLAGS', r'(\Deleted)')
    mail.expunge()
