
import os

import downloadEmail

emailAddress = os.environ.get("python_email")
emailPw = os.environ.get("python_password")

downloadEmail.downloadEmails(emailAddress, emailPw, 'therealnicola@gmail.com')
