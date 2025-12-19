
# line seperator function
def seperator (char,length):
    print(char*length)

# special characters set
special_char= set('!@#$%^&*()<>?{}[]')

seperator('=',80)
print('Hey good user welcome to Password strength checker')
seperator('=',80)

password= input('Enter your password:')
print('\n')

# Checking the length
password_length = len(password)
if password_length < 10:
    print("kindly use longer password and try again")
else:
    print(f"Good you have a {len(password)} digit long password ")

# Checking for alphanumeric
if password.isdigit() == True:
    print("BUT \nAdd some alphabets to make it stronger")
elif password.isalpha() == True:
    print("BUT \nAdd some numbers to make it stronger")
else:
    print("Your password is also alpha numeric")

#checking Upper lower and special case.
has_special = False
upper = False
lower = False
for c in password:
    if c in special_char:
        has_special = True
    elif c.isupper():
        upper = True
    elif c.islower():
        lower = True

if has_special and upper and lower :
    print("congrats you have a strong password")
elif not(upper and lower):
    print("Include both UPPER and lower case characters")
elif has_special == False:
    print("Include special characters as well")

# Final Scoring system
score = 0
if password_length > 10: score +=1
if has_special: score +=1
if upper: score +=1
if lower: score +=1

print(f'your final score is {score}/4 ')
