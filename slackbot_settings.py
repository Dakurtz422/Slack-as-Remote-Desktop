import os

# Get Slack API_TOKEN from enviroment (or hardcode here)
api_key = os.environ.get('BOT_API')

API_TOKEN = api_key

# Default message when Bot can't find an appropriate answer
DEFAULT_REPLY = "Excuse me"

# Name of a directory where we will store our Bot settings
PLUGINS = ['plugins']
