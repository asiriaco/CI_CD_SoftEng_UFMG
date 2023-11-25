class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity
        self.parked_cars = set()

    def park_car(self, car):
        if self.is_full():
            raise Exception("Parking lot is full")
        if car in self.parked_cars:
            raise Exception("Car is already parked")
        self.parked_cars.add(car)
        self.available_spaces -= 1

    def remove_car(self, car):
        if car not in self.parked_cars:
            raise Exception("Car is not parked")
        self.parked_cars.remove(car)
        self.available_spaces += 1

    def is_full(self):
        return self.available_spaces == 0

    def is_car_parked(self, car):
        return car in self.parked_cars






