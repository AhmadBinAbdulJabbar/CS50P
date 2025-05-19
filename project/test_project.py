import os
import csv
import json
from project import add_contact, get_current_contacts, search_contact, update_contact, delete_contact, export_to_json, contact_rewriter

TEST_NAME = "Test User"
TEST_PHONE = "03001234567"
TEST_EMAIL = "testuser@example.com"
TEST_ADDRESS = "Lahore"

def test_add_contact():
    # Remove contact if it exists
    contacts = get_current_contacts()
    contacts = [c for c in contacts if c['phone'] != TEST_PHONE]
    contact_rewriter(contacts)
    # Add contact
    result = add_contact(TEST_NAME, TEST_PHONE, TEST_EMAIL, TEST_ADDRESS)
    assert result is True
    # Check if contact exists
    contacts = get_current_contacts()
    assert any(c['phone'] == TEST_PHONE for c in contacts)

def test_search_contact():
    add_contact(TEST_NAME, TEST_PHONE, TEST_EMAIL, TEST_ADDRESS)
    # Search by name
    found = search_contact(1, TEST_NAME)
    assert any(c['name'] == TEST_NAME for c in found)
    # Search by phone
    found = search_contact(2, TEST_PHONE)
    assert any(c['phone'] == TEST_PHONE for c in found)

def test_update_contact():
    add_contact(TEST_NAME, TEST_PHONE, TEST_EMAIL, TEST_ADDRESS)
    contacts = get_current_contacts()
    contact = next(c for c in contacts if c['phone'] == TEST_PHONE)
    new_email = "updated@example.com"
    result = update_contact(contact, TEST_NAME, TEST_PHONE, new_email, TEST_ADDRESS)
    assert result is True
    contacts = get_current_contacts()
    assert any(c['email'] == new_email for c in contacts if c['phone'] == TEST_PHONE)

def test_delete_contact():
    add_contact(TEST_NAME, TEST_PHONE, TEST_EMAIL, TEST_ADDRESS)
    contacts = get_current_contacts()
    contact = next(c for c in contacts if c['phone'] == TEST_PHONE)
    result = delete_contact(contact)
    assert result is True
    contacts = get_current_contacts()
    assert not any(c['phone'] == TEST_PHONE for c in contacts)

def test_export_to_json():
    add_contact(TEST_NAME, TEST_PHONE, TEST_EMAIL, TEST_ADDRESS)
    result = export_to_json()
    assert result is True
    assert os.path.exists('contacts.json')
    with open('contacts.json') as f:
        data = json.load(f)
        assert any(c['phone'] == TEST_PHONE for c in data)
