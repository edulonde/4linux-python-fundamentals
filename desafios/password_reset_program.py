password = ""

def ask_for_pswd():
    passrod_is_set = 0

    while not passrod_is_set:
        password = input("Enter your password: ")
        password_confirm = input("Confirm your password: ")

        if password_confirm != password:
            print("password not equal to confirm password!")
            ask_for_pswd()
        elif len(password) < 8 :
            print("password less than 8 char")
            ask_for_pswd()
        minusculas = 0
        maiusculas = 0
        for c in password:
            if c.islower():
                minusculas = minusculas + 1
            elif c.isupper():
                maiusculas = maiusculas + 1

        if minusculas == 0:
            print("doesnt have any lowe char")
            ask_for_pswd()
        elif maiusculas == 0:
            print("doesnt have any upper char")
            ask_for_pswd()
        else:
            print("Passowrd is set!")
            passrod_is_set = 1
            break



ask_for_pswd()

