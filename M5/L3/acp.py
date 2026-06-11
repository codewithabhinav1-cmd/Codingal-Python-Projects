class Vehicle:
    def __init__(self, fare):
        self.fare = fare


class Bus(Vehicle):
    def total_fare(self):
        return self.fare + (0.10 * self.fare)


fare = float(input("Enter the vehicle fare: "))

b = Bus(fare)

print("Total Bus Fare =", b.total_fare())