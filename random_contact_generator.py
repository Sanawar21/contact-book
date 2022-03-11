class contact():
    def __init__(self, name , address, phone , email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


from random import randint


def randomname():
    firstname = ['Muhammad', 'Syed']
    lastname = ['Sanawar','Anas','Hamza','Ayan','Ahmed','Asad','Arsalan',
                'Yusuf','Ali','Sarim','Ramiz','Javed','Shahzeb','Shahzaman',
                'Hannan']

    firstind = randint(0,len(firstname)-1)
    lastind = randint(0,len(lastname)-1)

    name = firstname[firstind] + ' ' + lastname[lastind]
    return name

def randomadd():
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = []
    for num in range(100):
        number.append(num)

    neighbourhood = [
        'Gulshan-e-Ghazi','Islam Nagar','Ittehad Town','Muhajir Camp','Muslim Mujahid Colony','Nai Abadi','Naval Colony',
        'Rasheedabad','Saeedabad','Al-Falah Society','Drigh Colony','Moria Khan Goth','Natha Khan Goth','Pak Sadat Colony',
        'Rafa-e-Aam Society','Raita Plot'
    ]
    address = f"{alphabets[randint(0,len(alphabets) - 1)]}-{number[randint(0,100) - 1]},{neighbourhood[randint(0,len(neighbourhood)-1)]}"
    return address


def randomph():
    phone = '03'
    for num in range(9):
        phone = phone + str(randint(0,9))
    return phone


def randemail(name):
    name = name.lower()
    name = name.split(' ')
    num = randint(0,99)
    email = f'{name[0]}{name[1]}{num}@gmail.com'
    return email

def randomcontact():
    name = randomname()
    add = randomadd()
    ph = randomph()
    email = randemail(name)

    randomcontact = contact(name,add,ph,email)
    return randomcontact


print("-----Random Contact Generator------")
amount = input("Enter how many contacts you want to generate: ")
overwrite = input("Do you wish to over-write existing contact book or do you wist to add to it? (o/a) ").lower()

contactlist = []

if int(amount) <= 100000:
    if overwrite == 'a' or overwrite == 'o':
        for num in range(int(amount)):
            cont = randomcontact()
            contactlist.append(cont)

if overwrite == 'o':
    with open("contactbookdata.txt", 'w') as writing:
        for contact in contactlist:
            n = contact.name
            a = contact.address
            p = contact.phone
            e = contact.email + '\n'


            writing.write(f'{n}^{a}^{p}^{e}')
        print("Over-writing done.")

elif overwrite == 'a':
    with open('contactbookdata.txt', 'a') as adding:
        for contact in contactlist:
            n = contact.name
            a = contact.address
            p = contact.phone
            e = contact.email + '\n'

            adding.write(f'{n}^{a}^{p}^{e}')
        print("Adding done.")

else:
    print("Nothing was done.")