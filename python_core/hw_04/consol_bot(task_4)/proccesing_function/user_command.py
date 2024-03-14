def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct user name"
        except IndexError:
            return "Enter the correct number of arguments"

    return inner


@input_error
def add_username_phone(dictionaty, args):
    name, phone = args
    dictionaty[name] = phone
    return "Contact added"


@input_error
def change_username_phone(dictionary, args):
    name, phone = args
    dictionary.update({name : phone})
    return "Phone changed"


@input_error
def return_phone_username(dictionary, args):
    name = args[0]
    return dictionary[name]


@input_error
def return_all_phone(dictionary):
    for values, keys in dictionary.items():
        print(f"{values} : {keys}")


@input_error
def delete_user(dictionary, args):
    name = args[0]
    del dictionary[name]
    return "User deleted"
