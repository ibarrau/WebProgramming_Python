class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
def main():
    f = Flight(origin="Jujuy", destination="Cordoba", duration=120)
    f.duration+=10
    print(f.origin)
    print(f.destination)
    print(f.duration)
if __name__== "__main__":
    main()