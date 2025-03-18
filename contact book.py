
import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)



def add_contact(contacts):
    name = input("Enter Full Name: ").strip().title()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if name in contacts:
        print("❌ Contact with this name already exists!")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\n📂 No contacts found!")
        return

    print("\n📒 Contact List:")
    print("=" * 40)
    for name, info in contacts.items():
        print(f"👤 {name} | 📞 {info['Phone']}")
    print("=" * 40)



def search_contact(contacts):
    keyword = input("🔍 Enter Name or Phone Number to search: ").strip().lower()
    found = False

    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info['Phone']:
            print("\n✅ Contact Found:")
            print("=" * 40)
            print(f"👤 Name: {name}")
            print(f"📞 Phone: {info['Phone']}")
            print(f"📧 Email: {info['Email']}")
            print(f"🏠 Address: {info['Address']}")
            print("=" * 40)
            found = True

    if not found:
        print("❌ No matching contact found.")



def update_contact(contacts):
    name = input("✏️ Enter the name of the contact to update: ").strip().title()

    if name not in contacts:
        print("❌ Contact not found!")
        return

    print("\n🔹 Leave blank to keep existing value.")
    phone = input(f"Enter new Phone [{contacts[name]['Phone']}]: ").strip() or contacts[name]['Phone']
    email = input(f"Enter new Email [{contacts[name]['Email']}]: ").strip() or contacts[name]['Email']
    address = input(f"Enter new Address [{contacts[name]['Address']}]: ").strip() or contacts[name]['Address']

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts(contacts)
    print(f"✅ Contact '{name}' updated successfully!")



def delete_contact(contacts):
    name = input("🗑️ Enter the name of the contact to delete: ").strip().title()

    if name not in contacts:
        print("❌ Contact not found!")
        return

    confirm = input(f"⚠️ Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        del contacts[name]
        save_contacts(contacts)
        print(f"✅ Contact '{name}' deleted successfully!")
    else:
        print("❌ Deletion cancelled.")

def main():
    contacts = load_contacts()

    while True:
        print("\n📖 CONTACT BOOK MENU")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contact List")
        print("3️⃣ Search Contact")
        print("4️⃣ Update Contact")
        print("5️⃣ Delete Contact")
        print("6️⃣ Exit")

        choice = input("\n🔷 Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\n👋 Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
