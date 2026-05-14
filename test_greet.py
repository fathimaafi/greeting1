"""Unit tests for the greet function in the greeter module."""
import unittest
from greeter import greet

class TestGreet(unittest.TestCase):
    """Class which includes test cases for the greet function."""

    def test_greet_with_valid_name(self):
        """Test that the greet function returns the correct greeting for a valid name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Charlie"), "Hello, Charlie!")

    def test_greet_with_empty_string(self):
        """Test that the greet function returns the correct greeting for an empty string."""
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
