from time import sleep
from tabulate import tabulate

class DuplicateContactError(Exception): pass
class ContactNotFoundError(Exception): pass

class Contact:
  def __init__(self, name: str, phone: str) -> None:
      self.name = name
      self.phone = phone
  def show(self, _print: bool = True) -> str:
    if _print:
      print(f"Name: {self.name}\nPhone: {self.phone}")    
    return f"Name: {self.name}\nPhone: {self.phone}"
  def edit(self, new_name: str = None, new_phone: str = None) -> None:
    self.name = new_name
    self.phone = new_phone
  def __str__(self):
    return f"{self.name}{self.phone}"
  def __eq__(self, other: object) -> bool:
      return True if self.name == other.name and self.phone == other.phone else False

class ContactList:
  __separator = '@#$%$#*&^'
  def __init__(self, data_file: str) -> None:
    """
    data_file: str = 'path/to/file.txt'
    """
    self.data_file = data_file
    self.contact_list: list[Contact] = []
  def add_contact(self, contact: Contact) -> None:
    if contact in self.contact_list:
      raise DuplicateContactError
    else:
      self.contact_list.append(contact)
  def del_contact(self, contact: Contact) -> None:
    if contact not in self.contact_list:
      raise ContactNotFoundError
    else:
      self.contact_list.remove(contact)
  def save(self) -> None:
    with open(self.data_file, 'w') as file:
      for contact in self.contact_list:
        file.write(f"{contact.name}{self.__separator}{contact.phone}\n")
  def read_file(self) -> None:
    try:
      with open(self.data_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
          line = line.strip()
          name, phone = line.split(self.__separator)
          self.contact_list.append(Contact(name, phone))
    except FileNotFoundError:
      with open(self.data_file, 'w'): pass
  def find_contacts(self, to_find: str) -> tuple[Contact]:
    found = []
    for contact in self.contact_list:
      if to_find in str(contact):
        found.append(contact)
    return tuple(found)
  def print_to_console(self, _print: bool = True) -> str:
    table = [[c.name, c.phone] for c in self.contact_list]
    if _print:
      print(tabulate(table, headers=['Name','Phone']))
    return tabulate(table, headers=['Name','Phone'])

def main(contacts: ContactList):
  print("Contact Book")
  while True:
    sleep(1)
    print()
    print("Enter '1' to view your contactbook.")
    print("Enter '2' to add a new contact.")
    print("Enter '3' to edit a contact.")
    print("Enter '4' to find a contact.")
    print("Enter '5' to delete a contact.")
    print("Enter '6' to clear contactbook.")
    print("Enter '7' to close the program.")
    print()
    action = int(input("What action do you want to perform? "))
    print()
    if action == 1:
      contacts.print_to_console()
    elif action == 2:
      print()
      name = input("Enter name of new contact: ")
      phone = input("Enter phone of new contact: ")
      try:
        contacts.add_contact(Contact(name,phone))
      except DuplicateContactError:
        print('This contact already exists.')
        contacts.find_contacts(phone)[0].show()
    elif action == 3:
      print()
      name = input("Enter name or phone of the contact you want to edit: ")
      founds = contacts.find_contacts(name)
      if len(founds) == 0:
        print("No contact found.")
        edit_contact = None
      elif len(founds) > 1:
        print()
        print("Found: ")
        print()
        x = 1 
        for found in founds:
          print(f"Serial: {x}")
          found.show()
          print()
          x+=1
        try:
          serial = int(input("Enter the serial of contact you want to edit: "))
          edit_contact = founds[serial-1]
        except:
          print("Invalid Serial.")
          edit_contact = None
      elif len(founds) == 1:
        edit_contact = founds[0]
        if not(edit_contact is None):  
          print()
          edit_contact.show()
          name = input("Enter the new name of contact (leave blank to not change): ")
          phone = input("Enter the new phone of contact (leave blank to not change): ")
          if name == '' and phone == '':
            print("No edit placed.")
          elif name == '':
            edit_contact.edit(new_phone=phone)
          elif phone == '':
            edit_contact.edit(new_name=name)
          else:
            edit_contact.edit(name,phone)
          print("Contact edited.")
    elif action == 4:
      print()
      to_find = input("Enter the phone or name you want to find: ")
      founds = contacts.find_contacts(to_find)
      print("Found:")
      print()
      for found in founds:
        found.show()
        print()
    elif action == 5:
      print()
      to_find = input("Enter name or phone of the contact you want to delete: ")
      founds = contacts.find_contacts(to_find)
      if len(founds) == 0:
        print("No contact found.")
        del_contact = None
      elif len(founds) > 1:
        print()
        print("Found: ")
        x = 1
        for found in founds:
          print(f"Serial: {x}")
          found.show()
          print()
          x+=1
        try:
          serial = int(input("Enter the serial of contact you want to edit: "))
          del_contact = founds[serial-1]
        except:
          print("Invalid Serial")
          del_contact = None
        if not(del_contact is None):
          del_contact.show()
          contacts.del_contact(del_contact)
          print(f'{del_contact.name} deleted.')
    elif action == 6:
      print("Are you sure you want to delete all contacts?")
      yn = input()
      if yn == 'y':
        for contact in contacts.contact_list:
          contacts.del_contact(contact)
      sleep(1)
      print("Done")
    elif action == 7:
      print("Closing...")
      sleep(1.5)
      break
    else:
      print("Enter a valid number.")
  contacts.save()

if __name__ == '__main__':
  contacts = ContactList('data.txt')
  contacts.read_file()
  main(contacts)
