import unittest
from concurrent_play_calculator import maximum_plays

class EventsInProgressTestCase(unittest.TestCase):
    def test_empty_dataset(self):
        """
        Testing with an empty dataset
        """
        
        plays = []
        
        result = maximum_plays(plays)
        
        self.assertEqual(result, 0)
        
    
    def test_single_sample(self):
        """
        Testing for a dataset consisting of one sample
        """
        
        plays = [{"start": datetime.datetime(2022, 1, 1, 0, 30, 0),
                    "end": datetime.datetime(2022, 1, 1, 1, 0, 0)}]

        result = maximum_plays(plays)

        self.assertEqual(result, 1)
        
        
    def test_overlapping_month(self):
        """
        Testing for samples which extend across to the next month
        """
        
        plays = [{"start": datetime.datetime(2022, 1, 31, 23, 30, 0),
                    "end": datetime.datetime(2022, 2, 1, 4, 30, 0)},
                 {"start": datetime.datetime(2022, 1, 31, 20, 0, 0),
                    "end": datetime.datetime(2022, 2, 1, 2, 30, 0)},
                 {"start": datetime.datetime(2022, 2, 3, 0, 0, 0),
                    "end": datetime.datetime(2022, 2, 3, 3, 0, 30)}]
        
        result = maximum_plays(plays)
        
        self.assertEqual(result, 2)
    
    
    def test_overlapping_year(self):
        """
        Testing for samples which extend across to the next year
        """
        
        plays = [{"start": datetime.datetime(2021, 12, 31, 23, 30, 0),
                    "end": datetime.datetime(2022, 1, 1, 4, 30, 0)},
                 {"start": datetime.datetime(2021, 12, 31, 20, 0, 0),
                    "end": datetime.datetime(2022, 1, 1, 2, 30, 0)},
                 {"start": datetime.datetime(2022, 1, 3, 22, 30, 0),
                    "end": datetime.datetime(2022, 1, 4, 2, 0, 0)}]
        
        result = maximum_plays(plays)
        
        self.assertEqual(result, 2)
        

if __name__ == "__main__":
    unittest.main(verbosity = 2)