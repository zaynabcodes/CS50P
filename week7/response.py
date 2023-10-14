import validators

email =  input("What's your email address?: ")

response = validators.email(email)

if response == True:
    print("Valid")
else:
    print("Invalid")