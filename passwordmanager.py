# Tuyen Huynh, Spring 2022
# tu399150

# Introductions and reading existing files
name = input("What is the name of the storage file?\t")
file = open(name, "r")
contents = file.readlines()
file.close

# Create new file
new_file = open("logins.txt", "w")
print("File created!")

option = ""

# Used to seperate lines into list
for index in range(len(contents)):
    contents[index] = contents[index].split()

# Function for registering new user  
def register_user():
    username = input("Username:\t")

    # Used to read each list
    for list in contents:

        # Checking if the username already exists
        if str(username) in list[0]:
            print("That username is already in use. Try again.")
            return register_user()
        
        # Checking if username fits requirements
        elif not username.isalpha():
            print("That username does not meet the requirements:\t")
            print("\t- usernames must only contain alpha characters")
            return register_user()

        # Checking if username fits requirements  
        elif len(username) >= 16 or len(username) <= 5:
            print("That username does not meet the requirements:\t")
            print("\t- usernames must be between 6 and 15 characters")
            return register_user()

        else:
            password = input("Password:\t")

            # Checking if password fits requirements
            if not password.isalpha():
                print("That password does not meet the requirements:\t")
                print("\t- passwords must only contain alpha characters")
                return password

            # Checking if password fits requirements
            if password.isdigit(0):
                print("That password does not meet the requirements:\t")
                print("\t- passwords must contain at least one numerical digit")
                return password

            # Checking if password fits requirements
            if password.isupper(0):
                print("That password does not meet the requirements:\t")
                print("\t- passwords must contain at least one uppercase letter")
                return password
            
            else:
                print("\tAccount registered!")
                contents.append(username, password)

# Function for verifying existing users       
def verify_user():
    username = input("Username:\t")
    for list in contents:
        if str(username) not in list[0]:
            print("\tThat user is not registered.")
            return verify_user()
        else:
            password = ("Password:\t")
            if password in list[username, 1]:
                print("\tSign in verified")
            else:
                valid = input("Invalid password. Try again? (y/n)")
                if valid == "y":
                    return password
                elif valid == "n":
                    return
                
# Function for changing username
def update_user():
    username = input("Username:\t")
    if username not in list[0]:
        print("\tThat user is not registered")

    else:
        password = input("Password:\t")
        if password in list[username, 1]:
            print("What do you want to change the username to?")
            new_username = ("Username:\t")
            username.replace(username, new_username)

        else:
            print("Invalid password. Try again? (y/n)")
            if valid == "y":
                return password
            elif valid == "n":
                return
            
# Function for changing password
def update_password():
    username = input("Username:\t")
    password = input("Password:\t")
    if password in contents[username, 1]:
        new_password = input("What do you want to change the password to?")
        password.replace(password, new_password)
    else:
        print("Invalid password")
            
# Function for deleting account
def delete_user():
    username = input("Username:\t")
    password = input("Password:\t")
    if password in contents[username, 1]:
        decision = input("Are you sure you want to delete this account? (y/n)")
        if decision == "y":
            contents.delete(username, password)
            print("Deletion completed.")
        elif decision == "n":
            print("\tOperation abanonded.")


# Loop for operation menu
while option != "6":
    print("\nWhich operation do you want to perform?\n"
          "1. Register new user\n"
          "2. Verify user sign in\n"
          "3. Update username\n"
          "4. Update password\n"
          "5. Delete account\n"
          "6. Exit system")
    option = input("Selection:\t")

    if option == "6":
        print("Exiting system")
        break

    elif option == "1":
        print()
        register_user()

        # Writing in the new file
        for item in list:
            new_file.write(item)
            new_file.write("\t")
        new_file.write("\n")

    elif option == "2":
        print()
        verify_user()

        # Writing in the new file
        for item in list:
            new_file.write(item)
            new_file.write("\t")
        new_file.write("\n")
            
    elif option == "3":
        update_user()

        # Writing in the new file
        for item in list:
            new_file.write(item)
            new_file.write("\t")
        new_file.write("\n")
            
    elif option == "4":
        update_password()

        # Writing in the new file
        for item in list:
            new_file.write(item)
            new_file.write("\t")
        new_file.write("\n")

    elif option == "5":
        delete_user()

        # Writing in the new file
        for item in list:
            new_file.write(item)
            new_file.write("\t")
        new_file.write("\n")
