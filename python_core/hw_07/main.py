from proccesing_function.user_command import add_username_phone, change_username_phone, return_all_phone, return_phone_username, delete_user
from collections import UserDict
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, name):
          super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            return "Phone must has 10 digits"


class Birthday:
    def __init__(self, value):
        try:
            true_data = re.find("d{2}.d{2}.d{4}", value)
            if true_data:
                date_value = datetime.strptime(value, "%d.%m.%Y")
                self.value = date_value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


    def add_phone(self, phone : Phone):
        self.phones.append(phone)


    def remove_phone(self, phone):
        self.phones.remove(phone)


    def edit_phone(self, old_phone, new_phone):
        try:
            index_old_phone = self.phones.index(old_phone)
            self.phones[index_old_phone] = new_phone
        except ValueError:
              return f"{old_phone} is not found"

    
    def find_phone(self, phone_to_find):
        if phone_to_find in self.phones:
            return phone_to_find
        
    def add_birthday(self, value, name):
        if name in AddressBook.data:
            pass
        


class AddressBook(UserDict):

    def add_record(self, record : Record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        del self.data[name]


    def get_upcoming_birthdays(users:list) -> list:
        now_date = datetime.today().date()
        congratulations_list = []
        for user in users:
            birthday_date = datetime.strptime(user["birthday"],"%Y.%m.%d").date()

            birthday_date_this_year = datetime.strptime(f"{now_date.year}-{birthday_date.month}-{birthday_date.day}","%Y-%m-%d").date()

            if birthday_date_this_year < now_date:
                birthday_date_this_year += timedelta(days=birthday_date_this_year.day + 1)

            days_to_birthday = (birthday_date_this_year - now_date).days


            if 0 <= days_to_birthday <= 7:
                if birthday_date_this_year.weekday() >= 5:
                    days_to_birthday += 7 - birthday_date_this_year.weekday()
                
                congratulation_date = now_date + timedelta(days=days_to_birthday)
                final_congratulation_date = datetime.strftime(congratulation_date, "%Y.%m.%d")

                congratulations_list.append({
                    "name" : user["name"],
                    "congratulation_date" : final_congratulation_date
                })

        return congratulations_list
        




def parse_user(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the consol bot!")
    print("""
Here are all the commands:
          
hello --- returns question
add --- adds the username and the userphone
change --- changes the userphone
return --- returns the userphone by username 
all --- returns all contacts
delete --- delete the contact
          """)
    while True:
        user_input = input("Input your command : ")

        command, *args = parse_user(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(book, args))
        elif command == "change":
            print(change_username_phone(book, args))
        elif command == "return":
            print(return_phone_username(book, args))
        elif command == "all":
            return_all_phone(book)
        elif command == "delete":
            print(delete_user(book, args))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()