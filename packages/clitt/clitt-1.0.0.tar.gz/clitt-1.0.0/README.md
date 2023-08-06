# Clitt

Ever wanted to tweet straight from your terminal? Wait, is it just me?

## How to install it?

I'm still working on deploying Clitt in a more friendly way but for now you can clone this repository, install all the dependencies (personally i recommend you use [Poetry](https://github.com/python-poetry/poetry) to handle this) and start using it.

## How to use it?

Clitt is meant to be simple (or at least as simple as a command line client for Twitter can be), so you just need to execute the main script, `__init__.py`, choose an action and pass the required parameters to perform the action. 

Running `__init__.py` for the first time will open a new tab on your browser with an authorization consent from Twitter, hit the authorize button, copy the code that will pop-up and paste it into the terminal. After the first time, your authorization token will be saved on your computer (and only there) for further uses.

## What can i do with Clitt?

#### Read your timeline

`$ python __init__.py read`

#### Write a Tweet

`$ python __init__.py post "Hey, i'm using Clitt to write this!"`

#### DM someone

`$ python __init__.py dm @target "Hey, i'm using Clitt to send you this DM!"`

#### Read your chat with another user

`$ python __init__.py chat @target`