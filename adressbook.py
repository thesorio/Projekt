import json
#import json wird benötigt da die Kontakte in der beiliegenden Datei abgespeichert werden
#hier wird die Klasse Contact erstellt
class Contact:
    def __init__(self, name, address, phone, age, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'age': self.age,
            'email': self.email
        }

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contacts(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower():
                found_contacts.append(contact)
        return found_contacts

    def list_contacts(self):
        for contact in self.contacts:
            print("Name:", contact.name)
            print("Address:", contact.address)
            print("Phone:", contact.phone)
            print("Age:", contact.age)
            print("Email:", contact.email)
            print()

    def save_to_file(self, filename):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        with open(filename, 'w') as file:
            json.dump(contacts_data, file)

    @classmethod
    def load_from_file(cls, filename):
        address_book = cls()
        with open(filename, 'r') as file:
            data = json.load(file)
            for contact_data in data:
                contact = Contact(**contact_data)
                address_book.add_contact(contact)
        return address_book

# Hauptprogramm
def main():
    address_book = AddressBook()

    # Hier wird das falls vorhandene Adressbuch geladen, falls eins nicht vorhanden ist wird ein neues erstellt
    try:
        address_book = AddressBook.load_from_file("address_book.json")
        print("Adressbuch erfolgreich geladen.")
    except FileNotFoundError:
        print("Kein vorhandenes Adressbuch gefunden. Es wird ein neues erstellt.")

    while True:
        print("Bitte wählen Sie eine Option:")
        print("1. Kontakt hinzufügen")
        print("2. Kontakt entfernen")
        print("3. Kontakte anzeigen")
        print("4. Kontakte suchen")
        print("5. Adressbuch speichern und beenden")
        choice = input("Auswahl: ")

        if choice == "1":
            name = input("Name: ")
            address = input("Adresse: ")
            phone = input("Telefonnummer: ")
            age = input("Alter: ")
            email = input("E-Mail: ")
            contact = Contact(name, address, phone, age, email)
            address_book.add_contact(contact)
            print("Kontakt erfolgreich hinzugefügt.")

        elif choice == "2":
            name = input("Name des Kontakts, den Sie entfernen möchten: ")
            found_contacts = address_book.search_contacts(name)
            if found_contacts:
                print("Gefundene Kontakte:")
                for index, contact in enumerate(found_contacts, start=1):
                    print(f"{index}. {contact.name}")
                selection = int(input("Geben Sie die Nummer des Kontakts ein, den Sie entfernen möchten: "))
                if selection > 0 and selection <= len(found_contacts):
                    contact_to_remove = found_contacts[selection - 1]
                    address_book.remove_contact(contact_to_remove)
                    print("Kontakt erfolgreich entfernt.")
                else:
                    print("Ungültige Auswahl.")
            else:
                print("Keine Kontakte gefunden.")

        elif choice == "3":
            address_book.list_contacts()

        elif choice == "4":
            search_term = input("Geben Sie einen Suchbegriff ein: ")
            found_contacts = address_book.search_contacts(search_term)
            if found_contacts:
                print("Gefundene Kontakte:")
                for contact in found_contacts:
                    print("Name:", contact.name)
                    print("Address:", contact.address)
                    print("Phone:", contact.phone)
                    print("Age:", contact.age)
                    print("Email:", contact.email)
                    print()
            else:
                print("Keine Kontakte gefunden.")

        elif choice == "5":
            address_book.save_to_file("address_book.json")
            print("Adressbuch erfolgreich gespeichert. Programm wird beendet.")
            break

        else:
            print("Ungültige Auswahl. Bitte wählen Sie erneut.")

if __name__ == '__main__':
    main()

