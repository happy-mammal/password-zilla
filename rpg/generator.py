import random

class RandomPasswordGenerator:
    res = []
    length  = 0
    isUnique = False

    def definedGeneration(self,strength):
        picks=[]
        uniques=set()
        password=""
        
        if(self.isUnique):
            
            while(len(uniques)!=self.length):
                uniques.add(random.choice(strength))

            password = "".join(x for x in uniques)
          
            return password

            
        else:
            
            while(len(picks)!=self.length):
                picks.append(random.choice(strength))

            password = "".join(x for x in picks)
         
            return password

    def generatePassword(self,hasChar,hasDigit,hasSymbol,case,results):
    
        lowAlpha ="abcdefghijklmnopqrstuvwxyz"
        upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numDigi = "0123456789"
        specSymb = "!@#$%^&*()"
        security = ""

        if(hasChar==True and hasDigit == True and hasSymbol==True):
            security = "high"
        elif(hasChar==True and hasDigit == True and hasSymbol==False):
            security = "moderate"
        elif(hasChar==True and hasDigit == False and hasSymbol==False):
            security = "low"
        else:
            security = "moderate"

        if(security=="low" and case =="lower"):
            return self.definedGeneration(lowAlpha)
        elif(security=="low"and case =="upper"):
            return self.definedGeneration(upAlpha)
        elif(security=="low" and case =="mixed"):
            return self.definedGeneration(upAlpha+lowAlpha)
        
        elif(security=="moderate" and case =="lower"):
            return self.definedGeneration(numDigi+lowAlpha+numDigi)
        elif(security=="moderate" and case =="upper"):
            return self.definedGeneration(numDigi+upAlpha+numDigi)
        elif(security=="moderate" and case =="mixed"):
            return self.definedGeneration(numDigi+upAlpha+lowAlpha+numDigi)

        elif(security=="high" and case =="lower"):
            return self.definedGeneration(specSymb+numDigi+lowAlpha+numDigi+specSymb)
        elif(security=="high" and case =="upper"):
            return self.definedGeneration(specSymb+numDigi+upAlpha+numDigi+specSymb)
        elif(security=="high"  and case =="mixed"):
            return self.definedGeneration(specSymb+upAlpha[0:13]+specSymb+numDigi+lowAlpha[14:26])

        else:
            pass

    def onGeneratePressed(self,length,hasChar,hasDigit,hasSymbol,case,results,isUnique):
        self.res = []
        self.length = length
        self.isUnique = isUnique
        for i in range(results):    
            
            password = self.generatePassword(hasChar,hasDigit,hasSymbol,case,results)
           
            self.res.append(password)
            
        return self.res
