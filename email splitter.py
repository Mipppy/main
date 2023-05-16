email = input("Enter the person's email address: \n")


if email.find("@") == -1:
    print("Please enter a valid email address")
else:
    email = email.split("@") 
    print(f"Name:  {email[0]}")
    print(f"Domain:  {email[1]}")