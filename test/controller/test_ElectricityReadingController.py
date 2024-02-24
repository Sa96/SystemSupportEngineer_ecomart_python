import unittest
from controller.setup_test_app import app

class TestElectricityReadingController(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_successfully_add_the_reading_against_new_smart_meter_id(self):
        reading_json = {
            'smartMeterID':'meter-11',
            'electricityReadings': [ {'time':1505825656,'reading':0.6} ]
        }

        response = self.client.post('/readings/store', json=reading_json)
        self.assertEqual(200, response.status_code)

    def test_successfully_add_the_reading_against_existing_smart_meter_id(self):
        reading_json_1 = {
            'smartMeterID':'meter-100',
            'electricityReadings': [ {'time':1505825838, 'reading':0.6}, {'time':1505885848, 'reading':0.65} ]
        }

        reading_json_2 = {
            'smartMeterID':'meter-100',
            'electricityReadings':[ { "time": 1605825849, "reading": 0.7 } ]
        }

        self.client.post('/readings/store', json=reading_json_1)
        self.client.post('/readings/store', json=reading_json_2)
        readings = self.client.get('/readings/read/meter-100').get_json()
        self.assertIn(reading_json_1['electricityReadings'][0], readings)
        self.assertIn(reading_json_1['electricityReadings'][1], readings)
        self.assertIn(reading_json_2['electricityReadings'][0], readings)

    
    def test_respond_with_error_if_smart_meter_id_not_self(self):
        reading_json = {
            'electricityReadings': [ { "time": 1505825838, "reading": 0.6 } ]
        }

        with self.assertRaises(Exception):
            self.client.post('/readings/store', json=reading_json)

    def test_respond_with_error_if_electricity_readings_not_self(self):
        reading_json = {
            'smartMeterID':'meter-11'
        }

        with self.assertRaises(Exception):
            self.client.post('/readings/store', json=reading_json)
        
    

