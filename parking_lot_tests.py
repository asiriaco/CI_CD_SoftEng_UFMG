from parking_lot import ParkingLot

class ParkingLotTests:
    def test_park_car(self):
        print("Testing park car")
        parking_lot = ParkingLot(5)
        parking_lot.park_car("ABC123")
        assert parking_lot.is_car_parked("ABC123"), "Car should be parked"
        assert not parking_lot.is_full(), "Parking lot should not be full"

    def test_remove_car(self):
        print("Testing remove car")
        parking_lot = ParkingLot(5)
        parking_lot.park_car("ABC123")
        parking_lot.remove_car("ABC123")
        assert not parking_lot.is_car_parked("ABC123"), "Car should not be parked"
        assert not parking_lot.is_full(), "Parking lot should not be full"

    def test_full_parking_lot(self):
        print("Testing full parking lot")
        parking_lot = ParkingLot(1)
        parking_lot.park_car("ABC123")
        assert parking_lot.is_full(), "Parking lot should be full"

    def test_duplicate_parking(self):
        print("Testing duplicate parking")
        parking_lot = ParkingLot(5)
        parking_lot.park_car("ABC123")
        try:
            parking_lot.park_car("ABC123")
        except Exception as e:
            assert str(e) == "Car is already parked", "Car should not be parked twice"

    def run_tests(self):
        self.test_park_car()
        self.test_remove_car()
        self.test_full_parking_lot()
        self.test_duplicate_parking()

# Run the tests
tests = ParkingLotTests()
tests.run_tests()