import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests the employee module."""

    def setUp(self):
        """Make one employee to complete test."""
        self.tony = Employee('tony', 'gutierrez', 85_000)

    def test_give_default_raise(self):
        """Test that the default raise works correctly."""
        self.tony.give_raise()
        self.assertEqual(self.tony.salary, 90000)
    
    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.tony.give_raise(20000)


if __name__ == '__main__':
    unittest.main()