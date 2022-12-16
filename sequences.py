names = ["Harry", "Ron", "Hermoine"]
# list - mutable
print(names[0])

coordinate = (10.0, 20.0)
# tuple  - not mutable

# set - collection of unique
# dict - hash 

#Define a list of names

names = ["Harry", "Ron", "Hermoine", "Ginny"]

names.append("Draco")

names.sort()

print(names)

# Create empty set 
s = set()

# Add elements to set ALWAYS unique

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.remove(2)


print(s)
print(f"The set has {len(s)} elements.")
