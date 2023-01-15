#!/usr/bin/env python3

class Addressable:
    def __init__(self, address):
        self.address = address

class Nameable:
    def __init__(self, name):
        self.name = name

class HasFriend:
    def __init__(self):
        self.friends = []
    
    def add_friend(self, friend):
        self.friends.append(friend)

class Contact(Addressable, Nameable, HasFriend):
    def __init__(self, address, name):
        Addressable.__init__(self, address)
        Nameable.__init__(self, name)
        HasFriend.__init__(self)



# contact1 = Contact("romain casu", "paris")
# contact2 = Contact("lucie spe", "montpellier")
# contact3 = Contact("john b", "miami")
# contact1.add_friend(contact2)
# contact1.add_friend(contact3)
# contact2.add_friend(contact1)
# contact2.add_friend(contact3)
# print(contact1.name)   
# print(contact1.address)
# print(contact1.friends) 

