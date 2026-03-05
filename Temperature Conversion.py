def userinputprocess(): #Input Process
    userinput = ''
    while userinput != 'cf' and userinput != 'fc': #Validates the input is what we want
        userinput = input('Do you want to convert C -> F or F -> C? Input CF / FC ').lower().strip()
    if userinput == 'cf':
        CFInputOut()
   
    if userinput == 'fc':
        FCInputOut()
    
def CF(x):
    x =float(x)
    x = (x*1.8)+32 #Basic Calculation process
    return x
        
def FC(x):
    x = float(x)
    x = (x-32)/1.8 #Basic Calculation process
    return x

def CFInputOut(): 
    IsValidInput = False
    while IsValidInput == False: #This essentially says 'if there is a value error, it asks again until theres not'
        userinput2 = input('Input the Degrees in Celsius ')
        try:
            float(userinput2)
            IsValidInput = True
        except ValueError:
            IsValidInput = False
    userinput2=CF(userinput2)
    print('The converted value in farenheit is '+str(userinput2))

def FCInputOut():
    IsValidInput
    while IsValidInput == False: #This essentially says 'if there is a value error, it asks again until theres not'
        userinput2 = input('Input the Degrees in Farenheit ')
        try:
            float(userinput2)
            IsValidInput = True
        except ValueError:
            IsValidInput = False
    userinput2=FC(userinput2)
    print('The converted value in celsius is '+str(userinput2))
    

userinputprocess()
