password = input("Input your password")
passLength = len(password)
print(passLength)
if passLength < 8:
    print("Weak Password")
elif passLength < 11:
    print ("Moderate Password")
elif passLength > 12:
    print("Strong Password")
else:
    quit()
