import logging 

from flask import Flask
from flask_ask import (Ask, statement)

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.INFO)

@ask.intent('AddGoalIntent')
def addGoalIntent(GOAL):
  return statement(f'Added Goal {GOAL}')

@ask.session_ended
@ask.launch
@ask.intent('Unhandled')
def launchRequest():
  return statement('Welcome to goal tracker!')


#if __name__ == '__main__':
app.run(debug=True)