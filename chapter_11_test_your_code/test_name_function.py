import unittest
from name_function import get_fomanted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Adam Adams" working?"""
        formated_name = get_fomanted_name('adam', 'adams')
        self.assertEqual(formated_name, 'Adam Adams')
    
    def test_first_middle_last_name(self):
        """Do names like 'Adam Konj Adams' working?"""
        formated_name = get_fomanted_name('adam', 'adams', 'konj')
        self.assertEqual(formated_name, 'Adam Konj Adams')
        

if __name__ == '__main__':
    unittest.main()
