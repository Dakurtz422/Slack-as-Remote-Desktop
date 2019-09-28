# Slack-as-Remote-Desktop
# This code works with Python 3.6 and Ubuntu 19.04 OS
 I'm using here a python's Slack module to create a program that will execute python codes(functions) based on slack's bot matches (Regex).
You can use a python now to make a "commands" for Slack Bot. Slack Bot will execute a python's functions based on the commands match.
For example you register a word "hello" to the script "first_word.py" and bind it with appreciate function in "aps.py" and when you write this "hello" word to the Slack Bot's room, Bot will react on this and execute the appreciate function from "aps.py". For example creating a file, or as you can see in sample code in "aps.py" executing a Linux's terminal codes, etc... 
Before you start: Please take a look how you can set up a Python's bot on Slack using API. You will need this API code to enable Python Bot for the Slack.
When you have the API code from the Slack, please register it to "slackbot_settings.py" file before you run "run.py"
