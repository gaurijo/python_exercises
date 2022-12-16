import sys #allows you to exit gracefully 

try:  
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError: 
  print("Error: Invalid input")
  sys.exit(1)

try:
  result = x /y 
except ZeroDivisionError: #exception handler so program won't crash
  print("Error: Cannot divide by 0.")
  sys.exit(1)

print(f"{x} / {y} = {result}")