from collections import UserDict

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

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
    

    # реалізація класу
    def add_phone(self, phone):
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
        


class AddressBook(UserDict):

    def add_record(self, record : Record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        del self.data[name]
        