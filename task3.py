import re
#Password must be atleast 8 characters long
password=input("enter your password:")
if len(password)<8:
    print("password must be atleast of 8 characters long")
#password must contain atleast one uppercase letter
elif not re.search("[A-Z]",password):
    print("password must contain atleast one uppercase letter")
#password must contain atleast one lowercase letters
elif not re.search("[a-z]",password):
    print("password must contain atleast one lowercase letter")
#password must contain atleast one number 
elif not re.search("[0-9]",password):
    print("password must contain atleast one number")
    #password must contain atleast one special character 
elif not re.search("[@,?,!]",password):
    print("password must contain atleast one special character")
else:
    print("password os strong")    



