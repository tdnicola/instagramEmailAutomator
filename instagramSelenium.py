from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import pyautogui

instagramAddress = os.environ.get('instagram_email')
instagramPW = os.environ.get('instagram_password')

mobile_emulation = {
    "deviceName": "iPhone 5/SE"
}
# Define a variable to hold all the configurations we want
chrome_options = webdriver.ChromeOptions()
# Add the mobile emulation to the chrome options variable
# Create driver, pass it the path to the chromedriver file and the special configurations you want to run
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(
    executable_path='/Users/tony/repos/chromedriver', options=chrome_options)
driver.get('http://www.instagram.com')
time.sleep(3)
# login Button
loginButton = driver.find_elements_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')[0]
loginButton.click()
time.sleep(2)

# username/password
browserUsername = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input')
browserPassword = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input')
browserUsername.send_keys(instagramAddress)
time.sleep(1)
browserPassword.send_keys(instagramPW)
instagramLogin = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button/div')
instagramLogin.click()
time.sleep(3)
# navigation through all the popups of adding homescreen and saving information
try:
    saveInfoPopup = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div/button')
    saveInfoPopup.click()
    time.sleep(3)
    try:
        instagramHomeScreen = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]')
        instagramHomeScreen.click()
        time.sleep(1)
        postNewPicture = driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        postNewPicture.click()
    except:
        postNewPicture = driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        postNewPicture.click()
except:
    postNewPicture = driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]')
    postNewPicture.click()


time.sleep(1)

# file type upload information
dirListing = os.listdir('emails/uploads')
for item in dirListing:
    # if m.lower().endswith(('.png', '.jpg', '.jpeg')
    # ...
    # elif m.endswith('.txt'):
    # ...
    # os.path.join(os.getcwd(), "emails/uploads", item)
    os.rename(os.path.join(os.getcwd(), "emails/uploads", item),
              os.path.join(os.getcwd(), "emails/old", item))


# working around that stupid upload button that I can't figure out. Though I think this makes you have to have the automation actually pop up vs headless mode.
def uploadImage():
    pyautogui.click(479, 126)
    pyautogui.click(479, 126)
    pyautogui.keyDown('command')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('g')
    pyautogui.keyUp('command')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('g')
