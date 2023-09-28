import unittest
import json
import os
from your_password_manager_module import is_strong_password, generate_password, add_password, get_password, save_passwords, load_passwords

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        # Create a temporary passwords.json file for testing
        self.test_passwords_file = "test_passwords.json"
        self.test_passwords = {"example.com": {"username": "user123", "password": "P@ssw0rd"}}
        with open(self.test_passwords_file, "w") as f:
            json.dump(self.test_passwords, f)

    def tearDown(self):
        # Remove the temporary passwords.json file after testing
        os.remove(self.test_passwords_file)

    def test_is_strong_password(self):
        # Test a strong password
        strong_password = "Str0ngP@ssw0rd"
        self.assertTrue(is_strong_password(strong_password))

        # Test a weak password (doesn't meet minimum length)
        weak_password = "Weak123"
        self.assertFalse(is_strong_password(weak_password))

        # Test a weak password (missing uppercase)
        weak_password = "weakpassword123!"
        self.assertFalse(is_strong_password(weak_password))

        # Test a weak password (missing special character)
        weak_password = "Weakpassword123"
        self.assertFalse(is_strong_password(weak_password))

    def test_generate_password(self):
        # Test generating a password of the specified length
        length = 12
        password = generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(is_strong_password(password))

        # Test generating a password of different length
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(is_strong_password(password))

    def test_add_password(self):
        # Test adding a password
        website = "example.net"
        username = "user456"
        password = "StrongP@ssw0rd"
        add_password(website, username, password)

        # Check if the added password is in the dictionary
        self.assertEqual(passwords[website]["username"], username)
        self.assertTrue(is_strong_password(passwords[website]["password"]))

    def test_get_password(self):
        # Test retrieving an existing password
        website = "example.com"
        username, password = get_password(website)
        self.assertEqual(username, self.test_passwords[website]["username"])
        self.assertEqual(password, self.test_passwords[website]["password"])

        # Test retrieving a non-existent password
        website = "nonexistent.com"
        username, password = get_password(website)
        self.assertIsNone(username)
        self.assertIsNone(password)

    def test_save_passwords(self):
        # Save passwords to a temporary file
        save_passwords(self.test_passwords, self.test_passwords_file)

        # Check if the saved passwords match the original passwords
        with open(self.test_passwords_file, "r") as f:
            saved_passwords = json.load(f)
        self.assertEqual(saved_passwords, self.test_passwords)

    def test_load_passwords(self):
        # Test loading passwords from an existing file
        loaded_passwords = load_passwords(self.test_passwords_file)
        self.assertEqual(loaded_passwords, self.test_passwords)

        # Test loading passwords from a non-existent file
        nonexistent_file = "nonexistent.json"
        loaded_passwords = load_passwords(nonexistent_file)
        self.assertEqual(loaded_passwords, {})

if __name__ == '__main__':
    unittest.main()
