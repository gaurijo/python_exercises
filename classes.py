# class Point():
#   def __init__(self, x, y): #initialize a point object that takes two values x, y. We need to indicate self to direct where the values are stored in the class object 
#     self.x = x 
#     self.y = y 

# p = Point(2, 8)
# print(p.x)
# print(p.y)

# Create a Flight class and methods to help an Airline keep track of booking passengers

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity # this is like @capacity = capacity in ruby
    self.passengers = [] #assign empty list of passengers

  def add_passenger(self, name): 
    if not self.open_seats(): #if there are no open seats
      return False
    self.passengers.append(name) #if flight is already at capacity should not allow more
    return True 

  def open_seats(self):
    return self.capacity - len(self.passengers) #function to account for how many open seats on a flight: the capacity minus the list of passengers; in ruby you would use .count or .length

flight = Flight(3)

people = ["Harry", "Ron", "Hermoine", "Ginny"]

for person in people: 
  success = flight.add_passenger(person)
  if success: 
    print(f"Added {person} to flight successfully.")
  else: 
    print(f"No available seats for {person}.")