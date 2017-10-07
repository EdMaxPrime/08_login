from flask import Flask, render_template, request, session

app=Flask(__name__)
app.secret_key="THIS IS NOT SECURE"

@app.route("/")
def root():
    if 'Name' in session:
        return  render_template("response.html", name=session['Name'], message="WELCOME!") ##User is already logged in, so shows Welcome page
    else:
        return render_template("form.html") ##User is not logged in

@app.route("/response", methods=["POST","GET"])
def response():
    print request.method
    print request.headers
    print request.form
    username=request.form["Name"]
    password=request.form["Password"]
    status=validate(username,password) ##Checks if username and password are correct
    if status == 0:
        session['Name'] = username
        print "Session: "+session['Name']
        return render_template("response.html", name=username, message="WELCOME!") #username and password are correct, so shows Welcome page
    elif status==1:
        return render_template("form.html",message="Wrong Password") #redirects to login page and shows message saying that password entered is wrong
    else:
        return render_template("form.html",message="Wrong Username") #redirects to login page and shows message saying that username is wrong
    

def validate(username, password):
    if username == "DW": #correct username
        if password == "kittens": ##correct password
            return 0 #everything correct
        return 1 #wrong password
    return 2 # wrong username

@app.route("/logout", methods=["POST","GET"])
def logout():
    if 'Name' in session:
        session.pop('Name') #remove user who was just logged in from session
    return render_template("logout.html") 

if __name__=="__main__":
    app.debug=True
    app.run()
