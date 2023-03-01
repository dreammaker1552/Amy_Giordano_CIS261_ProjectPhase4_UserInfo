def add_user():
    # Open the file in append mode
    with open("user_info.txt", "a") as f:
        # Read current records and save the user IDs in a list
        f.seek(0) # move the file pointer to the beginning
        user_ids = []
        for line in f:
            fields = line.strip().split("|")
            user_ids.append(fields[0])
        
        # Get user input until terminated by the user typing "End"
        while True:
            user_id = input("Enter user ID (type 'End' to finish): ")
            if user_id == "End":
                break
            elif user_id in user_ids:
                print("User ID already exists. Please choose another ID.")
                continue
            password = input("Enter password: ")
            auth_code = input("Enter authorization code (Admin/User): ")
            if auth_code not in ["Admin", "User"]:
                print("Invalid authorization code. Please enter either 'Admin' or 'User'.")
                continue
            # Write user information to file
            f.write(f"{user_id}|{password}|{auth_code}\n")
            # Add user ID to list
            user_ids.append(user_id)

def display_users():
    # Open file and print user information
    with open("user_info.txt", "r") as f:
        print("User ID | Password | Authorization Code")
        for line in f:
            fields = line.strip().split("|")
            print(f"{fields[0]} | {fields[1]} | {fields[2]}")

# Call the functions
add_user()
display_users()

