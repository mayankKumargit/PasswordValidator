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
    def checkSpace(self,password):
        for i in password:
            if (i == ' '):
                return 0
        return 1
    def checkRepeat(self,password):
        for i in range(0,len(password)-1):
            count=1
            j=i+1
            while j<len(password) and password[j]==password[i]:
                count+=1
                j+=1
            if count>=3:
                return 0
        return 1
    def checkOther(self,password):
        legal="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*_"
        for i in password:
            if(i not in legal):
                return 0
        return 1

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

    if request.method == 'POST':
        password=request.form["password"]
        pswd=Password()

        if(not pswd.isNotNull(password)):
            result="The password is Empty...Enter a non-empty password"
            return render_template("response.html",result=result)

        if(not pswd.checkLength(password)):
            result="The password is not of specified length...Enter a password with 8<=length<=15"
            return render_template("response.html",result=result)
        if(not pswd.checkUppercase(password)):
            result="The password does not have Uppercase Character...Enter a password with atleast 1 Uppercase Letter"
            return render_template("response.html",result=result)

        if(not pswd.checkLowercase(password)):
            result="The password does not have Lowercase Character...Enter a password with atleast 1 Lowercase Letter"
            return render_template("response.html",result=result)

        if(not pswd.checkDigit(password)):
            result="The password does not have Digit...Enter a password with atleast 1 Digit"
            return render_template("response.html",result=result)

        if(not pswd.checkSpecialChar(password)):
            result="The password does not have Special Character...Enter a password with atleast 1 Special Character"
            return render_template("response.html",result=result)

        if(not pswd.checkSpace(password)):
            result="The password has White Space...Enter a password with no White Space"
            return render_template("response.html",result=result)

        if(not pswd.checkRepeat(password)):
            result="The password has Repeating Characters...Enter a password which has no more than 2 Repeating Characters"
            return render_template("response.html",result=result)

        if(not pswd.checkOther(password)):
            result="The password has characters other than (!,@,#,$,%,&,*,_). Enter a password which has no other characters"
            return render_template("response.html",result=result)

        result="Your password is Perfect!!!"
        return render_template("response.html",result=result)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
