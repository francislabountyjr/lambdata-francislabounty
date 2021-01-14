"""
Using unittest standard library to conduct  unit
tests on files in lambdata-francislabounty
"""

from helper_functions import DfHelper
import pandas as pd
import unittest

class TestDfMethods(unittest.TestCase):
    """Class used to unit test the DfMethods class in helper_functions"""

    def setUp(self):
        """Instantiate an instance of the DfHelper class"""
        self.df = DfHelper(pd.DataFrame({'numbers': [1, 2, float("NaN")], 'colors': ['red', 'white', 'blue']}))

    def test_initialize(self):
        """Test that the class initializes correctly."""
        self.assertIsInstance(self.df, DfHelper)

    def test_null_count(self):
        """Test to see if the null_count function works correctly.
        Should return the null_count from each column"""
        self.assertEqual(self.df.null_count().any(), 1)

    def test_randomize(self):
        """Test to see if the randomize function works correctly.
        Should return a shuffled df that does not equal the original."""
        self.assertFalse(self.df.randomize(8).equals(self.df))

if __name__ == '__main__':
    unittest.main() #only runs if file is called like 'python test.py'