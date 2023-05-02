class Password(object):
    def isNull(self,password):
        if(len(password)==0):
            return None
        else:
            return not None
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
            if (i.isspace()):
                return 0
        return 1
