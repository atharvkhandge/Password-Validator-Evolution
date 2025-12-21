

# line seperator function
def seperator (char,length):
    print(char*length)

# Welcome text
art =    r""" __  __            ___            __            __                  __               ______  __  __     
/\ \/\ \          /\_ \    __    /\ \          /\ \__              /\ \             /\  _  \/\ \/\ \    
\ \ \ \ \     __  \//\ \  /\_\   \_\ \     __  \ \ ,_\   ___   _ __\ \ \____  __  __\ \ \L\ \ \ \/'/'   
 \ \ \ \ \  /'__`\  \ \ \ \/\ \  /'_` \  /'__`\ \ \ \/  / __`\/\`'__\ \ '__`\/\ \/\ \\ \  __ \ \ , <    
  \ \ \_/ \/\ \L\.\_ \_\ \_\ \ \/\ \L\ \/\ \L\.\_\ \ \_/\ \L\ \ \ \/ \ \ \L\ \ \ \_\ \\ \ \/\ \ \ \\`\  
   \ `\___/\ \__/.\_\/\____\\ \_\ \___,_\ \__/.\_\\ \__\ \____/\ \_\  \ \_,__/\/`____ \\ \_\ \_\ \_\ \_\
    `\/__/  \/__/\/_/\/____/ \/_/\/__,_ /\/__/\/_/ \/__/\/___/  \/_/   \/___/  `/___/> \\/_/\/_/\/_/\/_/
                                                                                  /\___/                
                                                                                  \/__/                 
"""
print(art)

seperator('=',40)
print("Enter your password below for validation")
seperator('=',40)

# User input
password = "

while not password:
    password = input("Enter your password: ")
    if not password:
        print("Password cannot be blank")

# Password Validation using regex
import re

length = len(password)

# regex parameters and logic

rules = {
    "length":(length >= 10, "Required length validated","***ALERT*** Atleast 10 digits required"),
    "uppercase":(re.search(r'[A-Z]',password)," UPPERCASE validated","***ALERT*** Atleast 1 Uppercase required"),
    "lowercase":(re.search(r'[a-z]',password)," Lowercase validated","***ALERT*** Atleast 1 Lowercase required"),
    "digits" : (re.search(r'\d',password)," Numbers validated","***ALERT*** Atleast single Digit required"),
    "special_char" : (re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'<,>.?/`~]',password)," Special characters validated","***ALERT*** Atleast 1 speical character required"),
    "spaces": (' ' not in password," Spaces validated","***ALERT*** No Spaces allowed")
}

final_score = 0
for rule,validation,exception in rules.values():
    if rule:
        final_score = final_score + 1
        print(validation)
    else:
        print(exception)

print(f' Your final score is {final_score}/6')
