# line seperator function
def seperator (char,length):
    print(char*length)

try:
    from zxcvbn import zxcvbn
except:
    zxcvbn_available= False
else:
    zxcvbn_available = True

if zxcvbn_available:
    print('')
else:
    seperator('=',80)
    print("\n[***WARNING***)] The 'zxcvbn' library is not installed.")
    print("Install it with: 'pip install zxcvbn' to enable modern heuristic analysis.")
    seperator('=', 80)
    exit()

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

seperator('=',80)
print("              🔒 Python Password Strength Checker CLI Tool 🔒")
print("   Analyzes passwords using traditional complexity rules and zxcvbn heuristics.")
seperator('=',80)

# User input
password = ""

while not password:
    password = input("Enter your password: ")
    if not password:
        print("Password cannot be blank")

# Password Validation using regex
import re

length = len(password)

# regex Rule Check

rules = {
    "length":(length >= 10, "- Required length validated","***ALERT*** Atleast 10 digits required"),
    "uppercase":(re.search(r'[A-Z]',password),"- UPPERCASE validated","***ALERT*** Atleast 1 Uppercase required"),
    "lowercase":(re.search(r'[a-z]',password),"- Lowercase validated","***ALERT*** Atleast 1 Lowercase required"),
    "digits" : (re.search(r'\d',password),"- Numbers validated","***ALERT*** Atleast single Digit required"),
    "special_char" : (re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'<,>.?/`~]',password),"- Special characters validated","***ALERT*** Atleast 1 speical character required"),
    "spaces": (' ' not in password,"- Spaces validated","***ALERT*** No Spaces allowed")
}

regex_score = 0
for rule,validation,exception in rules.values():
    if rule:
        regex_score = regex_score + 1
        print(validation)
    else:
        print(exception)
seperator('-',57)
print(f'Score for regex: {regex_score}/6')

#======================================================Importing ZXCVBN library======================================================
from zxcvbn import zxcvbn

# Score and Crack time
result = zxcvbn(password)
zxcvbn_score = result['score']
crack_time = result["crack_times_display"]['offline_fast_hashing_1e10_per_second']

# Output for Score and Crack time
print(f'Score for zxcvbn is {zxcvbn_score}/4')
print(f'Time required to crack your password: {crack_time}')
seperator('-',57)

# Output for Suggestions and feedback
print('**SUGGESTIONS**')
feedback = result['feedback']

if not feedback['warning'] and not feedback['suggestions']:
    print('No Suggestions YOU HAVE A STRONG PASSWORD')
else:
    for key,value in feedback.items():
        if isinstance(value,list):
            for a in value:
                print(a)
        elif isinstance(value, str):
            print(value)

#======================================================Final Score Calculation======================================================
regex_pect = (regex_score/6)*100
zxcvbn_pect = (zxcvbn_score/4)*100

final_score= (regex_pect + zxcvbn_pect)/2
seperator('=',50)
print(f'YOUR FINAL SCORE: {final_score}%')
seperator('=',50)
