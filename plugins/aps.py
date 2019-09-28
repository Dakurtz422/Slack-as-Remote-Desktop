# This is a file where you can write your codes that will be executed when the Bot
# makes a word-match in "first_word.py" based on regex
# I have includes here 3 sample functions, which can:
    # 1. Login into slack with specific account
    # 2. Make google search and send result url back
    # 3. Execute a terminal commands from Slack Chat (Works with Ubuntu 19.04)

# Btw. For the 1,2 you will need a webdriver for your Browser to execute(selenium).
# Or you can write your own functions for (for example):
    # - Sending Files
    # - Moving Files
    # - Execute some other Python codes
    # - Install something
    # - And so on... Possibilities are infinitive here

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import subprocess
from time import sleep

# Get slack login info from os.enviroment variable (bashrc - Ubuntu)
# Please delete this lines if you will not use it, otherwise
# it throws an error.
u_name = os.environ.get('SLACK_NAME')
u_pass = os.environ.get('SLACK_PASS')
ws = os.environ.get('SLACK_WS')

# 1.
def writeslc():
    driver = webdriver.Firefox()
    driver.get("https://slack.com/intl/ja-jp/signin")
    driver.find_element_by_id("domain").send_keys(ws)
    driver.find_element_by_id("submit_team_domain").click()
    driver.find_element_by_id("email").send_keys(u_name)
    driver.find_element_by_id("password").send_keys(u_pass)
    driver.find_element_by_id("signin_btn").click()

# 2.
def writegog(text):
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input").send_keys(text)
    driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input").send_keys(u'\ue007')
    sleep(3)
    url = driver.current_url
    return url

# 3.
def com(cm):
    process = subprocess.run(cm, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        return(process.stderr)
    else:
        out = process.stdout
        return(out)
