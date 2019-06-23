with open('login.txt','r') as file:
    text = file.read().splitlines()
    username=""
    password=""
    while username!=text[0] and password!=text[1]:
        username=input("Enter the username: ")
        password = input("Enter the password: ")
        if(username==text[0] and password==text[1]):
            print("Login Success")
        else:
            print("Invalid username or password. Please try again.")
            username = ""
            password = ""