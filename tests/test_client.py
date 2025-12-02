"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Matt Kenyon"
__version__ = "1.2.0"

from unittest import TestCase
from client.client import Client

class client_tests(TestCase):
    """Used to contain the tests for the Client class."""

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        client_number = 314159
        first_name = "Steve"
        last_name = "Jobs"
        email_address = "sjobs@gmail.com"

        self.client = Client(client_number, first_name, last_name, email_address)

    # __init__ tests
    def test_init_valid_parameters(self):
        self.assertEqual(314159, self.client._Client__client_number)
        self.assertEqual("Steve", self.client._Client__first_name)
        self.assertEqual("Jobs", self.client._Client__last_name)
        self.assertEqual("sjobs@gmail.com", self.client._Client__email_address)

    def test_init_invalid_client_number(self):
        # Arrange
        client_id = 3.14159
        first_name = "Steve"
        last_name = "Jobs"
        email_address = "sjobs@gmail.com"

        with self.assertRaises(ValueError) as context:
            client = Client(client_id, first_name, last_name, email_address)

        # Assert
        expected = "Client Number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_blank_first_name_raises_exception(self):
        # Arrange
        client_id = 314159
        first_name = "    "
        last_name = "Jobs"
        email_address = "sjobs@gmail.com"

        # Act
        with self.assertRaises(ValueError) as context:
            client = Client(client_id, first_name, last_name, email_address)

        # Assert
        expected = "First Name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_blank_last_name_raises_exception(self):
        # Arrange
        client_id = 314159
        first_name = "Steve"
        last_name = "    "
        email_address = "sjobs@gmail.com"

        # Act
        with self.assertRaises(ValueError) as context:
            client = Client(client_id, first_name, last_name, email_address)

        # Assert
        expected = "Last Name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_email_address_sets_default_value(self):
        # Arrange
        client_id = 314159
        first_name = "Steve"
        last_name = "Jobs"
        email_address = "email"
        invalid_email_address = "email@pixel-river.com"

        # Act
        client = Client(client_id, first_name, last_name, invalid_email_address)

        # Assert
        self.assertEqual(client.email_address, invalid_email_address)

    # Property Method Tests
    def test_client_number_returns_correct_state(self):
        # Act
        actual = self.client.client_number

        # Assert
        self.assertEqual(314159, actual)

    def test_first_name_returns_correct_state(self):
        # Act
        actual = self.client.first_name

        # Assert
        self.assertEqual("Steve", actual)

    def test_last_name_returns_correct_state(self):
        # Act
        actual = self.client.last_name

        # Assert
        self.assertEqual("Jobs", actual)

    def test_email_address_returns_correct_state(self):
        # Act
        actual = self.client.email_address

        # Assert
        self.assertEqual("sjobs@gmail.com", actual)

    # __str__ Tests
    def test_str_returns_correct_string_representation(self):
        # Act
        actual = self.client.__str__()

        # Assert
        expected = ("Jobs, Steve [314159] - sjobs@gmail.com")
        self.assertEqual(expected, actual)
        