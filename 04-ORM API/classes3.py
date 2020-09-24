class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    def delay(self, amount):
        self.duration += amount

def main():
    f = Flight(origin="Jujuy", destination="Cordoba", duration=120)    
    f.delay(15)
    f.print_info()

if __name__== "__main__":
    main()