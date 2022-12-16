#Modules
#from python module functions import square function 
#would need to specify {functions.square} if you use just import functions

from functions import square 
# import functions
for i in range(10):
      print(f"The square of {i} is {square(i)}") 
      # print(f"The square of {i} is {functions.square(i)}")

