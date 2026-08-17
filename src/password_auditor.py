import getpass

password = getpass.getpass("Input your password:\n")
password_length = len(password)
print(password_length)
if password_length < 8:
    print("WEAK")
elif password_length <= 11:
    print ("MODERATE")
elif password_length >= 12:
    print("STRONG")
else:
    quit()
