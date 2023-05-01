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
