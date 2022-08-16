# import unittest
# Create class TestAbs(unittest.TestCase) that is ingerited from TestCase class
# turn test functions into methods adding a link to an instance of the class self as the first argument of the function def test_abs1(self)
# change assert into self.assertEqual()
# change the starting code into unittest.main()

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
