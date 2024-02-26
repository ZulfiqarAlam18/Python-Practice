import getpass

u_name = "Zulfiqar"
u_pass = "123"



while True:    
    username =input("Enter User Name:")
    userpass = getpass.getpass("Enter user Password ")

    if username == u_name and userpass == u_pass:
        print("Log In Successful")
    else:
        print("Incorrect Password or User Name")
  