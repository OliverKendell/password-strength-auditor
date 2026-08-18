import getpass

password = getpass.getpass("Input your password:\n")
password_length = len(password)
print (f"Password Length: ",password_length)
if password_length < 8:
    print("Password Strength: WEAK")
elif password_length <= 11:
    print ("Password Strength: MODERATE")
else:
    print("Password Strength: STRONG")

