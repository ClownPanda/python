def login_auth(userNAme,password):
    userNameAuth=input("Enter your user name: ")
    passwordAuth=input("Enter your password: ")

    if userNameAuth==userNAme and passwordAuth==password:
        print("Login is succesfull")
    else:
        print("Login is fail")


print("-------Sign Up a new account-------")
userNAme=input("Enter new user name: ")
password=input("Enter new password: ")

print("--------Sign in:-------")
login_auth(userNAme,password)

    