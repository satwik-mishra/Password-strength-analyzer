# password-strength-analyzer
import re
# checking conditions : 
# min 8 characters,digits,uppercase,lowercase,special characters
def check_password_strength(password):
    if len(password)<8: # checking length of the password
        return "Weak:password must be of 8 characters"
    if not any(char.isdigit()for char in password):
        return "Weak:password must contain a digits"
    if not any(char.isupper() for char in password):
        return "Weak:password must contain an uppercase character"
    if not any(char.islower() for char in password):
        return "Weak:password must contain a lowercase character"
    if not re.search(r"[@#$%&!^()<>.?]",password):
        return "Medium:password must contain a special character"
    return "Strong:Your password is strong"
def password_checker():
    print("welcome to password-strength-analyzer")
    while(True):
        password=input("please enter your password(or type 'exit' to quit):\n")
        if password.lower()=='exit':
            print("Thank you for using this tool\n")
            break
        result=check_password_strength(password)
        print(result)
# Running the password-analyzer tool
if __name__=="__main__": 
    password_checker()
