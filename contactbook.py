from tabulate import tabulate

class contact():
    def __init__(self, name , address, phone , email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

diary = []
with open('contactbookdata.txt', 'r') as data:
    diary = []
    addtodiary = data.readlines()
    for line in addtodiary:
        attribute = line.split("^")
        contactname = attribute[0]
        contactaddress = attribute[1]
        contactphone = attribute[2]
        contactemail = attribute[3]
        diary.append(contact(contactname,contactaddress,contactphone,contactemail))

def addnewcontact():
    name = input("Enter contact's name: ")
    address = input("Enter contact's address: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contacts email: ")
    email = email + '\n'
    newcontact = contact(name,address,phone,email)
    diary.append(newcontact)
    print()
    print("The contact has been added.")

def findcont(fname):
    print()
    found = []
    cff = None
    req = input(f"Enter the name, address, phone or email of the contact you want to {fname}: ").lower()
    for contact in diary:
        cont = ''
        name = contact.name
        add = contact.address
        ph = contact.phone
        em = contact.email
        cont = name.lower() +add.lower() +ph.lower() +em.lower()
        if req in cont:
            found.append(contact)
    if len(found) == 1:
        cff = found[0]
        return cff
    elif len(found) == 0:
        print("No contact found.")
    elif len(found) > 1:
        contname = None
        for contact in found:
            print()
            print(f"Name: {contact.name}")
            print(f"Address: {contact.address}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print()
        reqnum = input(f"Enter the phone of the contact you want to {fname}: ").lower()
        for contact in found:
            if reqnum == contact.phone:
                cff = contact
                return cff
            else:
                continue
    if cff == None:
        print("No contact found.")

def findcontact():
    print()
    foundcontacts = []
    required = input("Write the name, address, phone or email of the contact you want to find: ").lower()
    for contact in diary:
        cont = ''
        naam = contact.name
        add = contact.address
        fone = contact.phone
        emal = contact.email
        cont = naam.lower() + add.lower() + fone.lower() + emal.lower()
        if required in cont:
            foundcontacts.append(contact)
    if foundcontacts == [None]:
        print("No contacts found linking with " + required + ".")
        print("Search by a different requirement.")
    else:
        print('Found ' + str(len(foundcontacts)) + ' contact(s).')
        print()
        for contact in foundcontacts:
            print('Name: ', contact.name)
            print('Address: ', contact.address)
            print('Phone: ', contact.phone)
            print('Email: ', contact.email)
            print()

def readcontactbook():
    newset = []
    for contact in diary:
        tempset = []
        tempset.append(contact.name)
        tempset.append(contact.address)
        tempset.append(contact.phone)
        tempset.append(contact.email)
        newset.append(tempset)
    print(tabulate(newset, headers=['Name','Address','Phone','Email']))
    print()

def editcontact():
    #gets the contact the user wants to edit
    print()
    editingcontact = findcont("edit")
    index = diary.index(editingcontact)
    if editingcontact is None:
        return
    print()
    print('Name: ', editingcontact.name)
    print('Address: ', editingcontact.address)
    print('Phone: ', editingcontact.phone)
    print('Email: ', editingcontact.email)
    print()
    print("Enter '1' if you want to edit the contact's name.")
    print("Enter '2' if you want to edit the contact's address.")
    print("Enter '3' if you want to edit the contact's phone.")
    print("Enter '4' if you want to edit the contact's email.")
    done = ''
    while done.lower() != 'yes':
        num = int(input("Enter a number: "))
        if num == 1:
            editingcontact.name = input("Enter contact's new name: ")
        elif num == 2:
            editingcontact.address = input("Enter contact's new address: ")
        elif num == 3:
            editingcontact.phone = input("Enter contact's new phone number: ")
        elif num == 4:
            editingcontact.email = input("Enter contact's new email: " + '\n')
        else:
            num = input("Enter a valid number: ")
        done = input("Are you done? ")
    diary[index] = editingcontact
    print("The contact has been edited!")

def deletecontact():
    print()
    delingcontact = findcont("delete")
    if delingcontact == None:
        return
    print()
    print("Found:")
    print()
    print('Name: ', delingcontact.name)
    print('Address: ', delingcontact.address)
    print('Phone: ', delingcontact.phone)
    print('Email: ', delingcontact.email)
    print()
    surity = ''
    surity = input("Are you sure you want to delete this contact? ")
    if surity.lower() == 'yes':
        diary.remove(delingcontact)
        print()
        print("The contact was deleted.")
    else:
        print("The contact was not deleted.")

def updatediary():
    with open('contactbookdata.txt', 'w') as writeincontactbook:
        for contact in diary:
            writeindiary = ''
            name = contact.name
            add = contact.address
            phone = contact.phone
            email = contact.email
            writeindiary = name + '^' + add + '^' + phone + '^' + email
            writeincontactbook.write(writeindiary)

print()
print("            My Contactbook            ")
print()
execution = True
while execution:
    print()
    print("Enter '1' to view your contactbook.")
    print("Enter '2' to add a new contact.")
    print("Enter '3' to edit a contact.")
    print("Enter '4' to find a contact.")
    print("Enter '5' to delete a contact.")
    print("Enter '6' to close the program.")
    print()
    action = int(input("What action do you want to perform? "))
    print()
    if action == 1:
        readcontactbook()
    elif action == 2:
        addnewcontact()
    elif action == 3:
        editcontact()
    elif action == 4:
        findcontact()
    elif action == 5:
        deletecontact()
    elif action == 6:
        execution = False
    else:
        print("Enter a valid number.")
    updatediary()
