# Make a program to check whether an email address is valid or not.
# For instance, you could make sure that there are no spaces, that there
# is an @ symbol and a dot somewhere after it. Also check the length of the parts at the start,
# and that the end parts of the address are not blank.


main, arroba, dominium =  email.partition("@")
print(main, arroba,dominium)


if " " in email:
    print("The e-mail inserted has spaces in there,  please verify.")
elif "@" not in email:
    print("Looks like you dont insert the '@', please verify ")
elif "." not in dominium:
    print("Looks like you don't insert a correct dominium, there is no '.'")
else:
    "Email validated"


