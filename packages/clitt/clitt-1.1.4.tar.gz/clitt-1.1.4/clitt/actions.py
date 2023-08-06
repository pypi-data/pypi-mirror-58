import os
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

def split_string(string, chunk_size):
    chunks = len(string)
    return [ string[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

def dm(arguments, api):
    username = arguments[2]
    username = username.replace('@', '')
    content = arguments[3]
    user = api.get_user(username)
    api.send_direct_message(user.id, content)

def post(arguments, api):
    content = arguments[2]
    api.update_status(content)

def chat(arguments, api):
    user = arguments[2]
    user = user.replace('@', '')
    user = api.get_user(user)
    me = api.me()
    messages = api.list_direct_messages(count=100)
    for message in sorted(messages, key=lambda message: int(message.created_timestamp)):
        if int(message.message_create["sender_id"]) == user.id:
            show_message(message, user)
        if int(message.message_create["sender_id"]) == me.id and int(message.message_create["target"]["recipient_id"]) == user.id:
            show_message(message, me, reverse=True)

def read(arguments, api):
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        show_tweet(tweet)

def show_tweet(tweet, reverse=False):
    rows, columns = os.popen('stty size', 'r').read().split()
    separator = '-'
    blank = ' '
    header = f'{tweet.user.name} - {Fore.CYAN}@{tweet.user.screen_name}{Style.RESET_ALL}'
    text = tweet.text
    line_size = int(columns)
    text = split_string(text, line_size - 4)
    print(f'+{separator * (line_size - 2)}+')
    print(f'| {header}{ blank * (line_size - len(header) + 6)}|')
    for line in text:
        print(f'| {line}{blank * (line_size - len(line) - 3)}|')
    print('+' + '-' * (line_size - 2) + '+')

def show_message(message, sender, reverse=False):
    rows, columns = os.popen('stty size', 'r').read().split()
    separator = '-'
    blank = ' '
    date = datetime.fromtimestamp(int(message.created_timestamp[0:10]))
    header = f'{sender.name} - {Fore.CYAN}@{sender.screen_name}{Style.RESET_ALL} - {date}'
    line_size = int(columns)
    text = split_string(message.message_create["message_data"]["text"], line_size - 4)
    
    print(f'+{separator * (line_size - 2)}+')
    if reverse:
        print(f'|{ blank * (line_size - len(header) + 6)}{header} |')
        for line in text:
            print(f'|{blank * (line_size - len(line) - 3)}{line} |')
    else:
        print(f'| {header}{ blank * (line_size - len(header) + 6)}|')
        for line in text:
            print(f'| {line}{blank * (line_size - len(line) - 3)}|')  
    print('+' + '-' * (line_size - 2) + '+')