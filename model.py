from flask import Flask
from flask import request


def pizza(number):
    if request.form['pizza'] > str(1):
        return 'You have requested ' + request.form['pizza'] + ' slices of pizza.'
    elif request.form['pizza'] == str(1):
        return 'You have requested 1 slice of pizza.'
    else:
        return ''

def burger(number):
    if request.form['burger'] > str(1):
        return 'You have requested ' + request.form['burger'] + ' orders of burgers and fries.'
    elif request.form['burger'] == str(1):
        return 'You have requested 1 order of burgers and fries.'
    else:
        return ''
def chicken(number):
    if request.form['chicken'] > str(1):
        return 'You have requested ' + request.form['chicken'] + ' orders of three piece fried chickens.'
    elif request.form['chicken'] == str(1):
        return 'You have requested 1 three piece chicken.'
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
    if request.form['pizza'] > str(1):
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

