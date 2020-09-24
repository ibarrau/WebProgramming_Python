class Flight:    
    counter = 1

    def __init__(self, origin, destination, duration):
        # Keep track of id count
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers
        self.passengers = []

        # Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print()
        print("Passengers: ")
        for pa in self.passengers:
            print(pa.name)

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passengers:
    def __init__(self, name):
        self.name = name
        # self.flight_id = flight_id

def main():
    f = Flight(origin="Jujuy", destination="Cordoba", duration=120)    
    # Create passengers
    alice = Passengers("Alice")
    bob = Passengers("bob")
    # Add passengers to flight
    f.add_passenger(alice)
    f.add_passenger(Bob)

    f.print_info()

if __name__== "__main__":
    main()