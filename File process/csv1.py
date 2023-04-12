#LOAD AND SEARCH CONTACTS (CSV)

import csv

class PhoneContact:
    def __init__(self,name, phone):
        self.name = name
        self.phone = phone
    
class Phone:
    def __init__(self):
        self.contacts = []
    
    def load_contacts_from_csv(self):
        with open('contacts.csv', newline = '') as csvfile:
            file_reader = csv.DictReader(csvfile,delimiter = ',')
            for row in file_reader:
                ph_c = PhoneContact(row['Name'],row['Phone'])
                self.contacts.append(ph_c)
                
    def search_contacts(self):
        phrase = ""
        found = False
        while phrase == "":
            phrase = input("Search contacts: ").replace(" ","")
        for c in self.contacts:
            if phrase in c.name or phrase in c.phone:
                print(c.name,"(" + c.phone + ")")
                found = True
        if not found:
            print("No contacts found")
        

new_phone = Phone()
new_phone.load_contacts_from_csv()
new_phone.search_contacts()

