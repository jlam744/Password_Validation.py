p= input("Input your password: ")
testPassword = p
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upperCaseTest = False 
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
lowerCaseTest = False
NUMBER = "0123456789"
numberTest = False
SPECIAL = "[!@#$%^*()_<>?]"
specialTest = False

for t in testPassword:
    if t in UPPERCASE:
        upperCaseTest = True
        break

if upperCaseTest == True:
    print('Your Password PASSED the Uppercase Test')
    
else:
    print ('Your Password FAILED the Test')
    

for t in testPassword:
     if t in LOWERCASE:   
        lowerCaseTest = True
        break

if lowerCaseTest == True: 
    print('Your Password PASSED the Lowercase Test')
    
else:
    print ('Your Password FAILED the Test')
    
    
for t in testPassword:    
    if t in NUMBER: 
        numberTest = True
        break
if numberTest == True:
    print ('Your Password PASSED the Number Test')
else:
    print ('Your Password FAILED the Test')
    

for t in testPassword:
    if t in SPECIAL:
        specialTest = True 
        break
if specialTest == True:
    print ('Your Password PASSED the special Test')
else:
    print ('Your Password FAILED the Test')
    
if len(testPassword)>=8:
    print ('Your Password Passed the length check')
else:
    print ('Your Password FAILED the Test')
