from flask import Flask
from flask import request


def onion(number):
    if request.form['onion'] > str(1):
        return 'You have requested ' + request.form['onion'] + ' pounds of onions.'
    elif request.form['onion'] == str(1):
        return 'You have requested 1 pound of onions.'
    else:
        return ''

def sprout(number):
    if request.form['kale'] > str(1):
        return 'You have requested ' + request.form['sprout'] + ' pounds of brussel sprouts.'
    elif request.form['kale'] == str(1):
        return 'You have requested 1 pound of brussel sprouts.'
    else:
        return ''
def kale(number):
    if request.form['sprout'] > str(1):
        return 'You have requested ' + request.form['kale'] + ' pounds of kale.'
    elif request.form['sprout'] == str(1):
        return 'You have requested 1 pound of kale.'
    else:
        return ''
def apple(number):
    if request.form['apple'] > str(1):
        return 'You have requested ' + request.form['apple'] + ' pounds of apples.'
    elif request.form['apple'] == str(1):
        return 'You have requested 1 pound of apples.' 
    else:
        return
def orange(number):
    if request.form['orange'] > str(1):
        return 'You have requested ' + request.form['orange'] + ' pounds of oranges.'
    elif request.form['orange'] == str(1):
        return 'You have requested 1 pound of oranges.' 
    else:
        return ''
def bannana(number):
    if request.form['bannana'] > str(1):
        return 'You have requested ' +  request.form['bannana'] +  ' pounds of bannanas.'
    elif request.form['bannana'] == str(1):
        return 'You have requested 1 pound of bannanas.' 
    else:
        return ''
def carrot(number):
    if request.form['carrot'] > str(1):
        return 'You have requested ' + request.form['carrot'] + ' pounds of carrots.'
    elif request.form['carrot'] == str(1):
        return 'You have requested 1 pound of carrots.'
    else:
        return ''
def potato(number):
    if request.form['potato'] > str(1):
        return 'You have requested ' + request.form['potato'] + ' pounds of potatoes.' 
    elif request.form['potato'] == str(1):
        return 'You have requested 1 pound of potatoes.'
    else:
        return ''
def broccoli(number):
    if request.form['broccoli'] > str(1):
        return 'You have requested ' + request.form['broccoli'] + ' pounds of broccoli.'
    elif request.form['broccoli'] == str(1):
        return 'You have requested 1 pound of broccoli.' 
    else:
        return ''

