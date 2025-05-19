import json, csv, os, re

contact_csv = "contacts.csv"
contact_json = "contacts.json"
header = ["name", "phone", "email", "address"]

def contact_rewriter(contacts):
    """Rewrite the contacts CSV file with the provided contacts list."""
    try:
        with open(contact_csv, "w", newline="") as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(contacts)
        return True
    except Exception as e:
        return False

def add_contact(name, phone, email, address_city):
    """Add a contact to the CSV file. Returns True if added, False if validation fails."""

    phone_pattern = r"^(0\d{10}|92\d{10}|\+92\d{10})$"
    if not re.fullmatch(phone_pattern, phone):
        return False
    
    email_pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

    if not re.fullmatch(email_pattern, email):
        return False
    
    contact_details ={"name": name, "phone": phone,"email": email, "address": address_city}

    file_exists = os.path.exists(contact_csv)
    try:
        with open(contact_csv, "a", newline="") as file:
            writer = csv.DictWriter(file, header)
            if not file_exists or os.path.getsize(contact_csv) == 0:
                writer.writeheader()
            writer.writerow(contact_details)
        return True
    except Exception as e:
        return False

def get_current_contacts():
    """Return a list of all contacts from the CSV file."""
    contacts = []
    try:
        with open(contact_csv, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append({
                    "name" : row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "address": row["address"]
                })
    except FileNotFoundError:
        pass
    return contacts

def view_contacts():
    """Return a sorted list of contacts by name."""

    contacts = get_current_contacts()
    return sorted(contacts, key=lambda contact: contact['name'])

def search_contact(search_by, search_value):
    """Search contacts by name or phone. Returns a list of matching contacts."""
    contacts = get_current_contacts()
    contact_found = []
    if search_by == 1:
        search_name = search_value.strip().lower()
        contact_found = [c for c in contacts if search_name in c['name'].lower()]
    elif search_by == 2:
        search_phone = search_value.strip()
        contact_found = [c for c in contacts if search_phone in c['phone']]
    return contact_found

def update_contact(current_details, new_name, new_phone, new_email, new_address):
    """Update a contact's details. Returns True if updated, False if not found or validation fails."""


    contacts = get_current_contacts()
    if new_name == "":
        new_name = current_details['name']
    if new_phone == "":
        new_phone = current_details['phone']
    if new_email == "":
        new_email = current_details['email']
    if new_address == "":
        new_address = current_details['address']


    phone_pattern = r"^(0\d{10}|92\d{10}|\+92\d{10})$"
    if not re.fullmatch(phone_pattern, new_phone):
        return False
    

    email_pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

    if not re.fullmatch(email_pattern, new_email):
        return False
    new_contact_details = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
    updated = False

    for i, contact in enumerate(contacts):
        if contact.get("name").lower() == current_details['name'].lower() and contact.get("phone") == current_details['phone']:
            contacts[i] = new_contact_details
            updated = True
            break
    if updated:
        contact_rewriter(contacts)
    return updated

def delete_contact(current_details):
    """Delete a contact. Returns True if deleted, False if not found."""

    
    contacts = get_current_contacts()
    deleted = False
    for i, contact in enumerate(contacts):
        if contact.get("name").lower() == current_details['name'].lower() and contact.get("phone") == current_details['phone']:
            del contacts[i]
            deleted = True
            break
    if deleted:
        contact_rewriter(contacts)
    return deleted

def export_to_json():
    """Export all contacts to a JSON file. Returns True if successful."""
    contacts = get_current_contacts()
    try:
        with open(contact_json, 'w') as file:
            json.dump(contacts, file, indent=4)
        return True
    except Exception as e:
        return False

def main():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter Name: ").strip().title()
            phone = input("Enter Phone: ").strip()
            email = input("Enter Email: ").strip()
            address_city = input("Enter Address City: ").strip().capitalize()
            if add_contact(name, phone, email, address_city):
                print("Contact added successfully! ✅")
            else:
                print("Invalid input or error adding contact.")
        elif choice == '2':
            contacts = view_contacts()
            print("==== Contact List ====")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
        elif choice == '3':
            try:
                search_by = int(input("Search by (1) Name or (2) Phone: "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue
            if search_by not in [1, 2]:
                print("Invalid option.")
                continue
            search_value = input("Enter Name: " if search_by == 1 else "Enter Phone: ")
            found = search_contact(search_by, search_value)
            if found:
                for i, contact in enumerate(found, start=1):
                    print(f"Found: {i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
            else:
                print("No contact found!")
        elif choice == '4':
            # Update contact
            try:
                search_by = int(input("Search by (1) Name or (2) Phone: "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue
            if search_by not in [1, 2]:
                print("Invalid option.")
                continue
            search_value = input("Enter Name: " if search_by == 1 else "Enter Phone: ")
            found = search_contact(search_by, search_value)
            if not found:
                print("No contacts to update.")
                continue
            for i, contact in enumerate(found, start=1):
                print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
            try:
                update_num = int(input("Enter the number which you want to update: ").strip())
                if update_num < 1 or update_num > len(found):
                    print("Invalid number.")
                    continue
            except Exception as e:
                print("Invalid input.")
                continue
            current_details = found[update_num-1]
            new_name = input("Enter new name (or press Enter to skip): ").strip()
            new_phone = input("Enter new phone (or press Enter to skip): ").strip()
            new_email = input("Enter new email (or press Enter to skip): ").strip()
            new_address = input("Enter new address (or press Enter to skip): ").strip()
            if update_contact(current_details, new_name, new_phone, new_email, new_address):
                print("Contact updated successfully! ✅")
            else:
                print("Invalid input or error updating contact.")
        elif choice == '5':
            # Delete contact
            try:
                search_by = int(input("Search by (1) Name or (2) Phone: "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue
            if search_by not in [1, 2]:
                print("Invalid option.")
                continue
            search_value = input("Enter Name: " if search_by == 1 else "Enter Phone: ")
            found = search_contact(search_by, search_value)
            if not found:
                print("No contacts to delete.")
                continue
            for i, contact in enumerate(found, start=1):
                print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
            try:
                delete_num = int(input("Enter the number which you want to delete: ").strip())
                if delete_num < 1 or delete_num > len(found):
                    print("Invalid number.")
                    continue
            except ValueError:
                print("Invalid input.")
                continue
            current_details = found[delete_num-1]
            if delete_contact(current_details):
                print("Contact deleted successfully! ✅")
            else:
                print("Contact not found in the contact list.")
        elif choice == '6':
            if export_to_json():
                print(f"Exported contacts to contacts.json ✅")
            else:
                print("Error! while converting to json ❌")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()