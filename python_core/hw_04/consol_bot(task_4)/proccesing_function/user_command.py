
def add_username_phone(dictionaty, name, phone):
    dictionaty[name] = phone
    return "Contact added"


def change_username_phone(dictionary, name, phone):
    dictionary.update({name : phone})
    return "Phone changed"


def return_phone_username(dictionary, name):
    return dictionary[name]


def return_all_phone(dictionary):
    for values, keys in dictionary.items():
        print(f"{values} : {keys}")


def delete_user(dictionary, name):
    del dictionary[name]
    return "User deleted"
