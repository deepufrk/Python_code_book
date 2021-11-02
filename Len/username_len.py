#Username Length of User

username = input("Enter a Username([4-10 characters]")

if 4 <= len(username) <= 10:
    print("successfuly Registered") 
else:
    print("The Username character Length must be minimum 4 characters and maximum 10")