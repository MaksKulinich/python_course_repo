from proccesing_function.user_command import add_username_phone, change_username_phone, return_all_phone, return_phone_username, delete_user

def parse_user(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the consol bot!")
    print("""
Here is all commands:
          
hello --- returns question
add --- adds the username and the userphone
change --- changes the userphone
return --- returns the userphone by username 
all --- returns all contacts
delete --- deletes the contact
          """)
    while True:
        user_input = input("Input your command : ")

        command, *args = parse_user(user_input)
        if len(args) == 2:
            user_name = args[0]
            user_phone = args[1]
        elif len(args) == 1:
            user_name = args[0]

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(contacts, user_name, user_phone))
        elif command == "change":
            print(change_username_phone(contacts, user_name, user_phone))
        elif command == "return":
            print(return_phone_username(contacts, user_name))
        elif command == "all":
            return_all_phone(contacts)
        elif command == "delete":
            print(delete_user(contacts, user_name))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()