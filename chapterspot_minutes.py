import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys

IMPLICIT_WAIT_TIME = 10  # seconds

assert len(sys.argv) == 2  # filename, file url
minutes_url = sys.argv[1]

# Load in config settings.
with open('config.json') as config_file:
    config = json.load(config_file)

driver = webdriver.Firefox()
driver.implicitly_wait(IMPLICIT_WAIT_TIME)
driver.get('https://app.chapterspot.com/login')

# Sign in to ChapterSpot
assert 'Login - ChapterSpot' in driver.title
user = driver.find_element_by_id('username')
user.send_keys(config["chapterspot"]["username"])
password = driver.find_element_by_id('password')
password.send_keys(config["chapterspot"]["password"])
login = driver.find_element_by_xpath("//*[contains(text(), 'Sign-In')]")
login.click()

MESSAGE = "Here are the minutes from today's chapter: {0}".format(minutes_url)
assert 'Messages - ChapterSpot' in driver.title
driver.find_element_by_class_name('dropdown-toggle_msgtype').click()
driver.find_element_by_class_name('set-email').click()
driver.find_element_by_id('mainContent').send_keys(MESSAGE)
driver.find_element_by_id('messagePost').click()

exit_code = 0
try:
    driver.find_element_by_class_name('newMessage')
except NoSuchElementException:
    exit_code = 1
finally:
    driver.quit()
    sys.exit(exit_code)
