
import os

import downloadEmail

emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")

downloadEmail.downloadEmails(emailAddress, password, 'therealnicola@gmail.com')
