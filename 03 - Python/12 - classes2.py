class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.pasanger = []
    
    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.pasanger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.pasanger)
    

flight = Flight(3)

people = ["Harry", "Ron", "Hermanie", "Ginny"]

for person in people:
    sucess = flight.add_passanger(person)
    if sucess:
        print(f"Added {person} to flight sucessfully!" )
    else:
        print(f"No available seats for {person}!")