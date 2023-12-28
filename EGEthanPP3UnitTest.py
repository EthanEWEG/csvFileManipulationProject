import unittest
from unittest.mock import patch
from EgertonGrahamEthanPP3 import read

class TestReadDataFromCSV(unittest.TestCase):
    @patch('builtins.input', side_effect=["data.csv", "100"])
    def test_read_data_from_csv(self, mock_input):
        records = []  # Initializes an empty list

        # Calls the read_data_from_csv function
        read.read_data_from_csv('data.csv', 100, records)

        # Checks if the records list is not empty
        self.assertNotEqual(len(records), 0)

if __name__ == "__main__":
    unittest.main()