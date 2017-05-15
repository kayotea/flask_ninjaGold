from random import randrange
from flask import Flask, request, redirect, render_template, session
import datetime
app = Flask(__name__)
app.secret_key = "parseltongue"

@app.route('/')
def goldPage():
    if session.get('gold', None) == None:
        session['gold'] = 0
        session['statement'] = []
    return render_template('ninjaGold.html')

@app.route('/process_money', methods=['POST'])
def processMoney():
    cashType = request.form.get('building', None)
    earned = 0          #store gold earned from this harvest
    statement = ""      #store activity statement
    dt = ""             #store current date/time

    #if gold harvest is from farm:
    # add random amount between 10 - 20 gold
    # add suitable statement to array of statements
    if cashType == 'farm':
        earned = randrange(10, 21)
        session['gold'] += earned
        dt = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        statement = "Earned {} gold from the {}! ({})".format(earned, cashType, dt)
        session['statement'].append(statement)
    #if gold harvest is from caev:
    # add random amount between 5 - 10 gold
    # add suitable statement to array of statements
    elif cashType == 'cave':
        earned = randrange(5, 11)
        session['gold'] += earned
        dt = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        statement = "Earned {} gold from the {}! ({})".format(earned, cashType, dt)
        session['statement'].append(statement)
    #if gold harvest is from house:
    # add random amount between 2 - 5 gold
    # add suitable statement to array of statements
    elif cashType == 'house':
        earned = randrange(2, 6)
        session['gold'] += earned
        dt = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        statement = "Earned {} gold from the {}! ({})".format(earned, cashType, dt)
        session['statement'].append(statement)
    #if gold harvest is from casino:
    # add/subtract random amount between 0-50 gold
    # add suitable statement to array of statements
    elif cashType == 'casino':
        earned = randrange(-50, 51)
        session['gold'] += earned
        dt = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if earned < 0:
            statement = "Entered a {} and lost {} gold... ouch. ({})".format(cashType, abs(earned), dt)
        else:
            statement = "Entered a {} and won {} gold! ({})".format(cashType, earned, dt)
        session['statement'].append(statement)

    return redirect('/')


app.run(debug = True)