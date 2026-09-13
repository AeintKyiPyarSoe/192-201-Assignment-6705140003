class Vehicle:
    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False
        
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            return f"{self.make} {self.model} {self.plate} has been rented."
        else:
            return f"{self.make} {self.model} {self.plate} is already rented."
        
    def return_vehicle(self):
        if self.is_rented:
            self.is_rented = False
            return f"{self.make} {self.model} {self.plate} has been returned."
        else:
            return f"{self.make} {self.model} { self.plate} was not rented."
        
    def __str__(self):
        return f"{self.make} {self.model} ({self.plate}) - [{'Rented' if self.is_rented else 'Available'}]"
    
    
    
class Renter:
    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no
        self.rented = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value
        
    @property
    def license_no(self):
        return self._license_no
    
    @license_no.setter
    def license_no(self, value):
        if not value:
            raise ValueError("License number cannot be empty.")
        if value < 0:
            raise ValueError("License number cannot be negative.")
        self._license_no = value
        
        
class ElectricCar(Vehicle):
    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh
        
    def __str__(self):
        return f"{self.make} {self.model} ({self.plate}) - Battery: {self.battery_kwh} kWh - [{'Rented' if self.is_rented else 'Available'}]"
   
    
class Motorbike(Vehicle):
    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc
        
    def __str__(self):
        return f"{self.make} {self.model} ({self.plate}) - Engine: {self.engine_cc} cc - [{'Rented' if self.is_rented else 'Available'}]"