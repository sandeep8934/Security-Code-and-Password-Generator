"""
This project is basically a security code generator as well as password generator.
"""

import string
import random

def security_code(code):
    a = "".join(code[0:6])
    print(f"Security Code is {a}")
    
code = list(string.digits)


def password_generator(code_length):
    b = "".join(password[0:code_length])
    print(f"Security Code is {b}")
    
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
password = []
password.extend(s1)
password.extend(s2)
password.extend(s3)
password.extend(s4)

if __name__ == "__main__":

    service = int(input("Which type of code you want to generate..?\n\nType (1) for Security Code & Type (2) for Password Generator: "))
    while True:
        
        if service == 1:
            random.shuffle(code)
            security_code(code)

        elif service == 2:
            code_length = int(input("Choose length of your Password: "))
            random.shuffle(password)
            password_generator(code_length)

        elif service != 1 and service != 2:
            print("Please enter either 1 or 2")

        print("\nYou want to try again..?")
        YN = input("\nPlease enter yes or no: ")

        YN = YN.lower()

        if YN == "yes":
            service = int(input("Which type of code you want to generate..?\n\nType (1) for Security Code & Type (2) for Password Generator: "))
        
        elif YN == "no":
            print("...Thanks for using Random Code Generator...")
            break

        else:
            print("I am not understanding your keyword. Please enter either Yes/No.")
            
        
            

