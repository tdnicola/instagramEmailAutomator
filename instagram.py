#! /user/bin/env python3
import imaplib, email, base64, os, sys, mimetypes


emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(emailAddress, password)

mail.select("INBOX")


result, data = mail.search(None, 'ALL')
mailList = data[0].split()

for item in mailList:
    result, data = mail.fetch(item, '(RFC822)')
    rawEmail = data[0][1].decode("utf-8")
    emailMessage = email.message_from_string(rawEmail)
    to_ = emailMessage['To']
    from_ = emailMessage['From']
    subject_ = emailMessage['Subject']
    date_ = emailMessage['Date']
    counter = 1
    for part in emailMessage.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename()
        contentType = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(contentType)
            if not ext:
                ext = '.bin'
            filename = 'msg-part-%08d%s' %(counter, ext)
        counter += 1
    
    #saving the file
    savePath = os.path.join(os.getcwd(),"emails", date_, subject_)
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    with open(os.path.join(savePath, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))


    print(subject_)
    print(contentType)
    if "plain" in contentType: 
        print(part.get_payload())
    else:
        print(contentType)
