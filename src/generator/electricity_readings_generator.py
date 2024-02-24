from service.time_converter import iso_format_to_unix_time

import math
import random
import datetime

def random_int_between(minimum_value, maximum_value):
    return round(random.randrange(minimum_value,maximum_value),2)

def get_timedelta(sec=60):
    return datetime.timedelta(seconds=sec)

def generate_electricity_readings(num):
    readings = [
        {
            'time':iso_format_to_unix_time(((datetime.datetime.now() - get_timedelta(i*60)).isoformat())),
            'reading': math.floor(random.random()*1000)/1000
         } 
                for i in range(num)
                ]
    return readings
    