class TaxiRide:
    def __init__(self, rate_per_km, distance):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = distance
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare

    def print_receipt(self):
        print(f'Rate: {self.rate_per_km}')
        print(f'Distance: {self.distance}')
        print(f'Fare: {self.calculate_fare(self.distance)}')
        return ''


def main():
    ride1 = TaxiRide(15, 10)
    ride2 = TaxiRide(17, 9)

    print(ride1.print_receipt())
    print(ride2.print_receipt())

if __name__ == "__main__":
    main()
