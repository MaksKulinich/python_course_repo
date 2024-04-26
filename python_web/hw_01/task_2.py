from collections import UserDict
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import pickle


class Field(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def __getitem__(self):
        pass

    def __str__(self):
        return self

class Name(Field):
    def __init__(self, name):
        self.value = name

    def __getitem__(self):
        return self.value

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self.value = str(phone)
        else:
            raise ValueError("Phone must have 10 digits")
        
    def __getitem__(self):
        return self.value

    def __str__(self):
        return self.value


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __getitem__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone : Phone):
        if str(phone) not in self.phones:
            self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        self.phones.remove(phone)


    def edit_phone(self, old_phone, new_phone : Phone):
        try:
            index_old_phone = self.phones.index(old_phone)
            self.phones[index_old_phone] = Phone(new_phone)
        except ValueError:
              return f"{old_phone} is not found"

    
    def find_phone(self, phone_to_find):
        if phone_to_find in self.phones:
            return phone_to_find
        

    def add_birthday(self, value):
        self.birthday = Birthday(value)


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {str(self.birthday) if self.birthday else 'not found'}"    


class AddressBook(UserDict):

    def add_record(self, record : Record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data[name]

    
    def delete(self, name):
        del self.data[name]


    def get_upcoming_birthdays(self):
        now_date = datetime.today().date()
        congratulations_list = []
        for record in self.data.values():

            if record.birthday:
                datetime_birthday = datetime.strptime(str(record.birthday), "%d.%m.%Y").date()
                birthday_date_this_year = datetime_birthday.replace(year = now_date.year)

                if birthday_date_this_year < now_date:
                    birthday_date_this_year += timedelta(days=birthday_date_this_year.day + 1)

                days_to_birthday = (birthday_date_this_year - now_date).days


                if 0 <= days_to_birthday <= 7:
                    if birthday_date_this_year.weekday() >= 5:
                        days_to_birthday += 7 - birthday_date_this_year.weekday()
                    
                    congratulation_date = now_date + timedelta(days=days_to_birthday)
                    final_congratulation_date = datetime.strftime(congratulation_date, "%Y.%m.%d")

                    congratulations_list.append({
                        "name" : record.name.value,
                        "congratulation_date" : final_congratulation_date
                    })

        return congratulations_list
    

def parse_user(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter correct user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the correct number of arguments"

    return inner


@input_error
def add_username_phone(dictionary : AddressBook, args):
    name, phone, *_ = args
    try:
        record = dictionary.find(name)
    except:
        record = None
    
    message = "Contact updated."
    if record is None:
        record = Record(name)
        dictionary.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)

    return message


@input_error
def change_username_phone(dictionary : AddressBook, args):
    name, old_phone, new_phone,  *_ = args
    record = dictionary.find(name)
    if record and old_phone and new_phone:
        record.edit_phone(old_phone, new_phone)
        return "Phone changed"
    
    return "Phone not found"


@input_error
def return_phone_username(dictionary : AddressBook, args):
    name, *_ = args
    record = dictionary.find(name)
    if record:
        return record.__str__()



@input_error
def return_all_phone(dictionary : AddressBook):
    for values, keys in dictionary.items():
        print(f"{values} : {keys}")


@input_error
def delete_user(dictionary : AddressBook, args):
    name, *_ = args
    del dictionary[name]
    return "User deleted"


@input_error
def add_birthday(dictionary : AddressBook, args):
    name, birthday_str = args
    record = dictionary.find(name)
    if record:
        try:
            birthday = Birthday(birthday_str)
            record.birthday = birthday
            print("Birthday added")
        except ValueError as e:
                print(e)


@input_error
def show_birthday(dictionary : AddressBook, args):
    name = args[0]
    record = dictionary.find(name)
    if record and record.birthday:
        return str(record.birthday)
    else:
        return "Birthday not found."


@input_error
def birthdays(dictionary : AddressBook):
    upcoming_birthdays = dictionary.get_upcoming_birthdays()
    if upcoming_birthdays:
        for item in upcoming_birthdays:
            print(f"{item['name']} has a birthday on {item['congratulation_date']}")
    else:
        print("No upcoming birthdays.")


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


def main():
    
    print("Welcome to the consol bot!")
    print("""
Here are all the commands:
          
hello --- returns question
add --- adds the username and the userphone
change --- changes the userphone
return --- returns the userphone by username 
all --- returns all contacts
delete --- delete the contact
add-birthday --- add birthday to the contact
show-birthday --- show contact's birthday
birthday --- show upcoming birthdays
          """)
    user_file = input("What file do you want to save the data to? ")
    if user_file:
        book = load_data(user_file)
    else:
        book = load_data()

    while True:
        user_input = input("Input your command : ")

        command, *args = parse_user(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            if user_file:
                book = save_data(book, user_file)
            else:
                save_data(book)
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
        elif command == "add-birthday":
            add_birthday(book, args)
        elif command == "show-birthday":
            print(show_birthday(book, args))
        elif command == "birthday":
            print(birthdays(book))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
