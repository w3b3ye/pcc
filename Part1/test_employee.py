import unittest
from employee import Employee

class TestEmpIncr(unittest.TestCase):
    """Test for give_raise function."""
    def setUp(self):
        self.first = "AAA"
        self.last = "BBB"
        self.salary = 5000
        self.emp = Employee(self.first, self.last, self.salary)

    def test_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary,10000)
    
    def test_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.salary,15000)

if __name__ == '__main__':
    unittest.main()