from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
def validate(body):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = body.get('email')
    name = body.get('name')
    age = (body.get('age'))
    print(email , name , age)
    msg ={}
    msg['ok']= True
    if len(email.strip())  == 0:
        print("ha email 0")
        msg['ok'] = False
        msg['email'] = "Enter your email"

    elif(re.fullmatch(regex, email) is False):
        msg['ok'] = False
        msg['email']="Invalid Email"
        print("ha email galat")

    if len(name.strip()) is 0:
        msg['ok'] = False
        msg['name'] = "Enter your name"
        print("ha name 0")

    if len(age.strip()) is 0:
        msg['ok'] = False
        msg['age'] = "Enter your age"
        print("ha age 0")

    
    if  (len(age.strip()) is not 0):
        age = int(age)
        if age<18 or age>65:
            print("ha age galat")
            msg['ok'] = False
            msg['age'] = "Enter valid age"

    return msg
    


    

