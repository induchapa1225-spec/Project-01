class Vehicle:
    company_name = "National Transport Service"

def __init__(self, vehicle_id, plate_number, capacity):
    self.vehicle_id = vehicle_id
    self.palte_number = plate_number
    self.capacity = capacity
    self._status = "Available"

def start(self):
    self._status = "On Trip"
    print(f"Vehicle {self.plate_number} started trip.")

def stop(self):
    self._status = "Available"
    print(f"Vehicle {self.plate_number} trip completed.")      

def get_status(self):
    return self._status  

class Bus(Vehicle):

    def __init__(self, vehicle_id, plate_number, capacity, route_number):
        super().__init__(vehicle_id, plate_number, capacity)
        self.route_number = route_number

    def calculate_fare(self, distance):
        return distance * 2.5


class Driver:
    def __init__(self, driver_id, name, license_number):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        self. assign_vehicle = vehicle
        print(f"{self.name} assigned to {vehicle.pale_number}")


class Route:
    def __init__(self, route_number, start_point, end_point, distance):
        self.route_number = route_number
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance

    def route_info(self):
        return f"Route {self.route_number}: {self.start_point} -> {self.end_point}"   
    
            
                    