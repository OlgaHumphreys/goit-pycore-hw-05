
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name."
        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) is None:
        return "contact not found"
    else:
        contacts[name] = phone
        return "contact has been changed"


@input_error   
def get_phone(args, contacts):
    name = args[0]  
    return contacts[name]
 
    
def find_all(contacts):
    if len(contacts) == 0:
        return "contact's book is empty"
    else:
        info = "contact book:"
        for name, phone in contacts.items():
            info += f"\nname {name} phone {phone}"
        return info


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(find_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()