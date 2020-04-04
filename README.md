# Python instagram posting script

## Want to post to instagram but get distracted and stay on instagram more than you should?

#### I got bored with how distracting instagram can be and decided to try to create a script that would login to your gmail account download the subject and image you sent to yourself and then post it to your instagram so you never have to get on it in the first place

I like instagram. I just hate how easily I can get distracted with it and lose time. I like to post things to my instagram. My family likes to see pictures of my little one.

## Configuration

Gmail login Info:

```
Change this information to your gmail login information
emailAddress = os.environ.get("python_email")
password = os.environ.get("python_password")
```

Gmail Search info:

```
Currently have it searching for my own email address, could remove all this and have it search through all emails. Or change it to the email you would send the image and text from
result, messageFromMe = mail.search(None, 'FROM', '"therealnicola@gmail.com"')
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
