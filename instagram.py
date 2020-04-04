#! /user/bin/env python3
import imaplib
import email
import base64
import os
import sys
import mimetypes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(emailAddress, password)

mail.select("INBOX")

# finding emails sent from myself
result, messageFromMe = mail.search(None, 'FROM', '"therealnicola@gmail.com"')
mailList = messageFromMe[0].split()

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
            filename = 'msg-part-%08d%s' % (counter, ext)
        counter += 1
    # saving the file
    savePath = os.path.join(os.getcwd(), "emails", date_, )
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    with open(os.path.join(savePath, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))
    # saving the subject as a text file
    with open(os.path.join(savePath, 'text.txt'), 'w') as fp:
        fp.write(subject_)

    # Change the flag to deleted and delete
    typ, response = mail.store(item, '+FLAGS', r'(\Deleted)')
    mail.expunge()


mobile_emulation = {
    "deviceName": "Pixel 2"
}
# Define a variable to hold all the configurations we want
chrome_options = webdriver.ChromeOptions()
# Add the mobile emulation to the chrome options variable
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# Create driver, pass it the path to the chromedriver file and the special configurations you want to run
driver = webdriver.Chrome(
    executable_path='/Users/tony/repos/chromedriver', options=chrome_options)
driver.get('http://www.instagram.com')

# login Button
loginButton = driver.find_elements_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')[0]
loginButton.click()

# username/password
browserUsername = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input')
browserPassword = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input')
browserUsername.send_keys('test')
browserPassword.send_keys('password')
instagramLogin = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button/div')
instagramLogin.click()
