# This is a file where you can write your "commands" for the Bot.
# When the Bot will see the following text it will execute an appropriate
# command from "aps.py" file

from slackbot.bot import respond_to
from . import aps
import json
import re
import os

# Just a global var for sample purpose
text =""

# Some nice graphic for the Bot answers
attachments = [
{
    'fallback': 'Fallback text',
    'author_name': 'Slack Bot',
    'author_link': 'http://www.google.com',
    'text':'None',
    'color': '#59afe1'
}]


# ---------------------------- Samples below-------------------------------

# Open Slack command (execute "writeslc" function)
# Send as "Open slack as Marcel" (For example)
@respond_to('(Open slack as )(.*)')
def reply_hello(message, arg1, arg2, arg3):
    global attachments
    if arg1 == "Open slack as " and arg2 == "Marcel": # Some name here
        aps.writeslc()
        for item in attachments:
            item.update({'text':f'Opening Slack as {arg2}'})
        message.send_webapi('', json.dumps(attachments))
    else:
        for item in attachments:
            item.update({'text':"I can't recognize a user"})
            item.update({'color':'#DC143C'})
        message.send_webapi('', json.dumps(attachments))



# Google search
# Send as "Write apple to Google" (For example)
@respond_to('(Write )(.*)( to Google)')
def reply_next(message, arg1, arg2, arg3):
    global text
    if arg1 == "Write " and arg3 == " to Google" :
        text = str(arg2)
        url = aps.writegog(text)
        for item in attachments:
            item.update({'text':f'Wrote "{text}" to Google'})
        message.send_webapi('', json.dumps(attachments))
        message.reply(f"Here is an result{url}")


# Send File to Slack
# Send as "file get" (For example)
@respond_to('(.*)( get)')
def reply_hellon(message, arg1, arg2):
    message.channel.upload_file(fname="VeryImportantFile.txt", fpath="files/daiji.txt", initial_comment="Download Link")

# Print list of usable commands
# Send as "help"
@respond_to('(help)')
def reply_help(message, arg1):
    for item in attachments:
        item.update({'text':'Usable commands：'})
    message.send_webapi('', json.dumps(attachments))
    message.channel.upload_file(fname="comands.txt", fpath="files/comands.txt", initial_comment="コマンド一覧")


# Execute Commands in Ubuntu terminal
# Send as "cmd ls" (For example)
@respond_to('(cmd) (.*)')
def reply_next(message, arg1, arg2):
    global text
    if arg1 == "cmd":
        text = str(arg2)
        comand = aps.com(arg2)
        message.reply(comand)
