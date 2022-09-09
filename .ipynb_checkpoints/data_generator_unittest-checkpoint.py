import unittest
from synthetic_data import generate_dataset
import datetime

class SyntheticDataGeneratorTestCase(unittest.TestCase):
    
    def test_end_after_start(self):
        """
        Testing if the end datetimes are after the start. We run this for about 10000 samples
        to ensure there is a low probability that the end times are all ahead of the start by
        randomness.
        """
        
        plays = generate_dataset(n=10000)
        comparison = [0 if play["end"] > play["start"] else 1 for play in plays]
        
        self.assertEqual(sum(comparison), 0)
        
    
    def test_generating_correct_amount_of_samples(self):
        """
        The generate_dataset function takes one parameter n. In this test we check if the function
        returns n samples in the dataset.
        """
        
        n = 5
        plays = generate_dataset(n)
        
        self.assertEqual(len(plays), n)
        
    
    def test_correct_datatypes(self):
        """
        This function should return a list of dictionaries which contain datetime objects for the start
        and end time instances. This test checks if all the datatypes are correct.
        """
        
        plays = generate_dataset(1)
        
        self.assertEqual(type(plays), list)
        self.assertEqual(type(plays[0]), dict)
        self.assertEqual(type(plays[0]["start"]), datetime.datetime)
        self.assertEqual(type(plays[0]["end"]), datetime.datetime)
    
    
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)