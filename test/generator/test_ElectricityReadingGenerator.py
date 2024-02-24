import unittest
from datetime import datetime
from unittest.mock import patch

from src.generator.electricity_readings_generator import generate_electricity_readings, random_int_between

class TestElectricityReadingGenerator(unittest.TestCase):
    def test_generate_electricity_readings(self):
        generated = generate_electricity_readings(10)
        self.assertEqual(len(generated), 10)
        for i in generated:
            self.assertEqual(datetime.fromtimestamp(i['time']).year,  datetime.now().year)
            self.assertGreaterEqual(i['reading'], 0)
            self.assertLessEqual(i['reading'], 1)

    def test_return_two_digit_number_for_single_digit_number(self):
        with patch('random.randrange', return_value=9):
            self.assertEqual(random_int_between(0, 1), '09')

    def test_return_two_digit_number_for_two_digit_number(self):
        with patch('random.randrange', return_value=11):
            self.assertEqual(random_int_between(0, 1), '11')
