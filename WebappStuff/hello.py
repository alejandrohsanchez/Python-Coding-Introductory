from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/printText', methods = ['POST', 'GET'])
def printSomething():
    if (request.method == "POST"):
        # request.form will take the value from elements named 'submitButton' and assign it to buttonValue
        buttonValue = request.form['submitButton']
        
        
        if (buttonValue == 'credentials'):
            text1 = request.form['firstName']
            text2 = request.form['lastName']
            return f"""{text1} {text2}"""
        
        elif (buttonValue == 'firstLast'):
            textTyped = request.form['textField'] # Anything that was typed in 'textField' will be assigned to textTyped
            return f"""{textTyped}"""
        

@app.route('/') # At this URL
def hello_world(): # Do this:
    a = 1
    b = 2
    # f"""{a}""" means we are printing the value of a on the webpage.
    #return f"""{a}"""
    return render_template("index.html")