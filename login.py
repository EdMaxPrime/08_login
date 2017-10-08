from flask import Flask, render_template, request, session, redirect, url_for

app=Flask(__name__)
app.secret_key="THIS IS NOT SECURE"

@app.route("/", methods = ["POST", "GET"])
def root():
    if 'Name' in session:
        return redirect(url_for("welcome")) #logged in
    elif request.method == "POST" and request.form["Name"]!= "" and request.form["Password"]!="": #if user clicks submit and enters both the username and password, check if username and password are valid
        print request.form
        # Trying to login
        username = request.form["Name"]
        password = request.form["Password"]
        status = validate(username, password) #checking: is this combo good?
        # correct username and password
        if status == 0:
            session["Name"] = username
            return redirect(url_for("welcome")) #goes to welcome function
        # wrong password, try again
        elif status == 1:
            return render_template("form.html", message="Wrong Password")
        # wrong username, try again
        else:
            return render_template("form.html", message="Wrong Username")
    elif request.method == "POST" and request.form["Name"]=="" and request.form["Password"]!="": #if username is not entered, print error message
        return render_template("form.html",message="Username not entered")
    elif request.method == "POST" and request.form["Password"]=="" and request.form["Name"]!="": #if password is not entered, print error message
        return render_template("form.html",message="Password not entered")
    else:
        return render_template("form.html") # not logged in

@app.route("/welcome")
def welcome():
    if 'Name' in session:
        return render_template("response.html", name = session['Name'])
    else:
        return redirect(url_for("root"))
    

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
    return redirect(url_for("root")) #goes back to root function

if __name__=="__main__":
    app.debug=True
    app.run()
