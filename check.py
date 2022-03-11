
class contact():
    def __init__(self, name ,phone, address = None, email = None ):
        self.name = name
        self.phone = phone

        self.address = address
        self.email = email

    def __str__(self):
        if self.email is None and self.address is None:
            return f'\nName: {self.name}\nPhone: {self.phone}'
        elif self.email == None:
            return f'\nName: {self.name}\nPhone: {self.phone}\nAddress: {self.address}'
        elif self.address == None:
            return f'\nName: {self.name}\nPhone: {self.phone}\nEmail: {self.email}'
        else:
            return f'\nName: {self.name}\nPhone: {self.phone}\nAddress: {self.address}\nEmail: {self.email}'


person1 = contact('zaigham','02342424234245')
person2 = contact('sanawar','20938403492', email='sanawar@gmail.com')
person3 = contact('bilal', '030202020', address='nsnsncancoac')
person4 = contact('xxx', '69696969696', email='ph.com', address = 'asdjhvaishvjasv')

print(person1,person2,person3,person4)