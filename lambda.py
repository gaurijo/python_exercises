people = [
  {"name": "Harry", "house": "Gryffindor"}, 
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]

# def f(person): 
#   return person["house"]

# people.sort(key=f)
people.sort(key=lambda person: person["name"]) #this tells python how to sort the list of people

print(people)