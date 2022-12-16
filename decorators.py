#takes function as input and returns modified version of function as output: functional programming paradigm 
#is this like a helper method??

def announce(f):
  def wrapper(): 
    print("About to run the function...")
    f()
    print("Done with the function.")
  return wrapper

@announce #this calls on the above function
def hello():
  print("Hello World")

hello()