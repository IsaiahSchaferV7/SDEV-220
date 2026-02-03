class vehicle:
    def __init__(self, type):
        self.type: str = type
    def __str__(self):
        return self.type
class automobile(vehicle):
    def __init__(self, type, year, make, model, roof):
        super().__init__(type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.roof: str = roof
    def __str__(self):
        return self.type
if __name__ == "__main__":
    user_vehicle = vehicle(input("Please enter the type of vehicle: "))
    year = input("Please enter the year of the vehicle: ")
    make = input("Please enter the make of the vehicle: ")
    model = input("Please enter the model: ")
    roof = input("Please enter the roof type(Sun or no sun roof): ")

    vehicle_info = automobile(user_vehicle, year, make, model, roof)
    
    print(f"Vehicle type: {vehicle_info.type}")
    print(f"Year: {vehicle_info.year}")
    print(f"Make: {vehicle_info.make}")
    print(f"Model: {vehicle_info.model}")
    print(f"Type of roof: {vehicle_info.make}")