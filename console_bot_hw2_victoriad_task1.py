def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        #ValueError used in cases when the user enters add, but not name and phone number, or only one of them
        except ValueError:
            return "Please give me both name and phone number."
        #KeyError used when the user asks for a phone number of a contact not added to the cotacts
        except KeyError:
            return "Contact not found for the requested name"
        #IndexError used when there are not enough arguments
        except IndexError:
            return "Please enter more arguments"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    #if the user introduces command "add" but not both name and phone number
    if len(args) != 2:
        raise ValueError("Please enter both name and phone to add the contact")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def update_contact(args, contacts):
    #if the user introduces command "add" but not both name and phone number
    if len(args) != 2:
        raise ValueError("Please enter both name and phone to add the contact.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact not found for the requested name.")
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found for the requested name.")
    return contacts[name]

@input_error
def show_all(contacts):
    return contacts

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
        elif command == "update":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
