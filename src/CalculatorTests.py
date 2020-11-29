import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    #def test_addition(self):
        #test_data = CsvReader('./src/addition.csv').data
        #for row in test_data:
            #self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
           # self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(row)

    #def test_subtraction(self):
        #sub_data = CsvReader('./src/subtraction.csv').data
        #for row in sub_data:
            #self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            #self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(self.calculator.result)

    #def test_multiplication(self):
        #test_data = CsvReader('./src/multiplication.csv').data
        #for row in test_data:
            #self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            #self.assertEqual(self.calculator.result, int(row['Result']))
            #pprint(self.calculator.result)

    def test_division(self):
        test_data = CsvReader('/src/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            pprint(self.calculator.result)

def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()