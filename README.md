# Python instagram posting script

## Want to post to instagram but get distracted and stay on instagram more than you should?

#### I got bored with how distracting instagram can be and decided to try to create a script that would login to your gmail account download the subject and image you sent to yourself and then post it to your instagram so you never have to get on it in the first place

I like instagram. I just hate how easily I can get distracted with it and lose time. I like to post things to my instagram. My family likes to see pictures of my little one.

### First python project so still working on set up and ways to run it. Files are seperated currently for ease of testing for me. If you see anything I could improve let me know!

## Configuration

Gmail download/login info example:

```
import os
import downloadEmail

emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")

downloadEmail.downloadEmails(emailAddress, password, 'therealnicola@gmail.com')

Currently have it searching for my own email address. Change this to the email address you'd like to download the information from.
```

Selenium webDriver

```
Change webdriver executable path to your own location
driver = webdriver.Chrome(
    executable_path='/Users/tony/repos/chromedriver', options=chrome_options)
```

Instagram login info:

```
Currently have test information for instagram login, could do the same as the gmail password above and store it in your environment. But change these to instagram login information
browserUsername.send_keys('test')
browserPassword.send_keys('password')
```

##### _Still a wip_
