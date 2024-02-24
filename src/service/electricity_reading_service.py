from domain.electricity_reading import ElectricityReading

class ElectricityReadingService:
    def __init__(self, repository) -> None:
        self.electricity_reading_repository = repository
        pass

    def store_reading(self, json):
        readings = list(map(lambda x: ElectricityReading(x), json['ElectricityReadings']))
        return self.electricity_reading_repository.store(json['smartMeterID'], readings)
    
    def retrieve_readings_for(self, smart_meter_id):
        return self.electricity_reading_repository.find("smart-meter-2")