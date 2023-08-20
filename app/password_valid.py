from flask import Flask, request, render_template
app=Flask(__name__, template_folder='templates',static_folder='static')
class Password(object):
    def isNotNull(self,password):
        if(len(password)==0):
            return 0
        else:
            return 1
    def checkLength(self,password):
        if(len(password)<8 or len(password)>15):
            return 0
        else:
            return 1
    def checkUppercase(self,password):
        for i in password:
            if (i.isupper()):
                return 1
        return 0
    def checkLowercase(self,password):
        for i in password:
            if (i.islower()):
                return 1
    def checkDigit(self,password):
        for i in password:
            if (i.isdigit()):
                return 1
        return 0
    def checkSpecialChar(self,password):
        for i in password:
            if (i in ['!','@','#','$','%','&','*','_']):
                return 1
        return 0
    
@app.route('/')
def homepage():
    return render_template('password.html')

@app.route('/response',methods=['GET','POST'])
def checkPassword():
    
    if request.method == 'POST':
        password=request.form["password"]
        pswd=Password()
        if(pswd.isNotNull(password)):
            pass
        else:
            result="The password is Empty...Enter a non-empty password"
            return render_template("response.html",result=result)
        if(pswd.checkLength(password)):
            pass
        else:
            result="The password is not of specified length...Enter a password with length=>8 and length<=15"
            return render_template("response.html",result=result)
        if(pswd.checkUppercase(password)):
            pass
        else:
            result="The password does not have Uppercase Character...Enter a password with atleast 1 Uppercase Letter"
            return render_template("response.html",result=result)
        if(pswd.checkLowercase(password)):
            pass
        else:
            result="The password does not have Lowercase Character...Enter a password with atleast 1 Lowercase Letter"
            return render_template("response.html",result=result)
        if(pswd.checkDigit(password)):
            pass
        else:
            result="The password does not have Digit...Enter a password with atleast 1 Digit"
            return render_template("response.html",result=result)
        if(pswd.checkSpecialChar(password)):
            pass
        else:
            result="The password does not have Special Character...Enter a password with atleast 1 Special Character"
            return render_template("response.html",result=result)
        result="Your password is Perfect!!!"
        return render_template("response.html",result=result)
if __name__ == "__main__":
    app.run(debug=True)
