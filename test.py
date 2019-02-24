import unittest
#IMPORT code file

class CoreTest(unittest.TestCase):
    
    #There should be two csv file (for now)
    #1. wheel_data
    #2. specific_data

    def setUp(self):
        with open('wheel_data.csv') as wheel_data, open('specific_data.csv') as specific_data:
            self.wheel_data = wheel_data.read().splitlines()
            self.specific_data = specific_data.read().splitlines()

    def test_wheel_data_headers(self):
        self.assertEqual(self.wheel_data[0].split(","),["pos","EffVel","effUPT","LeftVel","LeftUPT","RightVel","RightUPT"])
    
    def test_wheel_data_contents(self):
        self.assertEqual(len(self.wheel_data[1].split(",")), len(self.wheel_data[0].split(",")))
    
    def test_specific_data_headers(self):
        self.assertEqual(
            self.specific_data[1].split(","),
            ["Row#","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB","Position","MC","SG","X","dF","ddB"]
        )
    
    def test_specific_data_contents(self):
        self.assertEqual(len(self.specific_data[1].split(",")), len(self.specific_data[0].split(",")))
         
if __name__ == '__main__':
    unittest.main()