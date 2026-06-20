import hashlib

print("1. Register")
print("2. Login")

choice = input("Enter Choice: ")

if choice == "1":

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    with open("users.txt", "a") as file:
        file.write(username + "," + hashed_password + "\n")

    print("User Registered Successfully!")

elif choice == "2":

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    entered_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    found = False

    with open("users.txt", "r") as file:

        for line in file:

            stored_username, stored_hash = line.strip().split(",")

            if username == stored_username:

                found = True

                if entered_hash == stored_hash:
                    print("Login Successful")
                else:
                    print("Wrong Password")

    if not found:
        print("User Not Found")