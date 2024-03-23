
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    #Name does not have aditional requirements 

class Phone(Field):
    def __init__(self, value):
        #Phone number must contain 10 characters and all of them digits
        if not len(value) != 10 and not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_number, new_phone_number):
        #the user introduces the old number and the new number which will replace the old one
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return "Contact not found"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return self.data.get(name)
    
    def delete_record(self, name):
        if name in self.data:
            return self.data.pop(name)
        return "Contact does not exist"
    
      # Creation of a new address book 
if __name__ == "__main__":
    book = AddressBook()

    # Creation of an entry for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add a John entry to the address book
    book.add_record(john_record)

    # Creating and adding a new entry for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all entries in the contact list
    for name, record in book.data.items():
        print(record)

    # Find and edit a phone number for John
    john = book.find_record("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
    print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

    # Searching for a specific phone number in John's entry
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"{john.name}: {found_phone}") 
    else:
        print("Contact not found") 

    # Deletion Jane's entry
    book.delete_record("Jane")
