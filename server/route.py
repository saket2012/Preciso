from flask import Flask , url_for
from app import app
from flask import request
from flask import render_template
from flask.templating import render_template
import basic_sentiment_analysis 
import enchantspell
import summarization123

@app.route('/')
def temp():
    return render_template("homepage.html")

@app.route("/register")
def register():
    return render_template("homepage.html")
    
@app.route("/spell")
def spell():
    return render_template("spell.html")

@app.route('/spell1/',methods =["POST"] )
def spell1():
    global user
    user = request.values.get('param')
    print(user)
    wrongwords=enchantspell.wrongwords(user)
    enchantoutput=enchantspell.spellenchant(user)
    if len(wrongwords)==0:
        nomistake = "No errors"
        return render_template("spell_output.html",sugg1=nomistake)
    else:
        return render_template("spell_output.html",sugg=enchantoutput,wrongwords=wrongwords)

@app.route("/tone")
def tone():
    return render_template("tone.html")

@app.route('/tone_output/',methods =["POST"] )
def tone1():
    textvar = request.values.get('param')
    toneoutput = basic_sentiment_analysis.output(textvar)
    return render_template("tone_output.html",user = toneoutput)

@app.route('/summarization')
def summarization():
    return render_template("summarization.html")

@app.route('/summarization_output',methods =['POST'])
def summarization1():
    summvar="'''" + request.values.get('param') + "'''"
    summoutput=summarization.summarization(summvar)
    return render_template("summ_output.html",summoutput=summoutput)


          
          
