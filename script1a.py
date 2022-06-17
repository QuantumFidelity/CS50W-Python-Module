# ~ first 'program' one should write in any new programming language'
# ~ #print("Hello, world!")

# ~ making use of the input and the print functions in conjunction 

#name = input("Name: ")
#print("Hello, " + name)

# using formatted strings to turn the above program into a single-liner (one-liner)
# the one-liner that they provided actually thre an error in my version of python, so i'm sure there is a way to do this, but it doesn't work with this syntax
#print(f"Hello, {input("Name: ")}")

# writing a simple conditional statements
# this program will change the output depending on what the user types in. 

#num = int(input("Number: "))
#if num > 0: 
#	print("This is a positive number")
#elif num < 0:
#	print("This is a negative number")
#else:
#	print("Number is 0")

# Accessing specific elements within a string

# ~ a1 = "this is a string, what are it's elements?"
# ~ print(a1[0:])
# ~ print(a1[0:50:3])

# Creating and Manipulating Lists, Retrieving Elements, and Adding Elemnts and Sorting Elements

# ~ # This is a Python Comment
# ~ names = ["John", "Dick", "Harry"]
# ~ # Print the entire list
# ~ print(names)
# ~ # Print the second name in the list
# ~ print(names[1])
# ~ # Add a new name to the list
# ~ names.append('Drako')
# ~ print(names)
# ~ # Sort the list
# ~ names.sort()
# ~ print(names)

# Example of a Tuple 

# ~ graph_coordinate = (1.6, 5.5)
 
# Example of an empty set

# ~ eset = set()

# ~ # Now let's add some elements to the set
# ~ eset.add(1)
# ~ eset.add(2)
# ~ eset.add(3)
# ~ eset.add(4)
# ~ eset.add(3)
# ~ eset.add(2)
# ~ eset.add(1)

# ~ print(eset)

# ~ # make use of the remove function 

# ~ eset.remove(2)
# ~ print(eset)

# ~ # Find the size of the set

# ~ print(f"This list has {len(eset)} number of elements.")

# Define a dictionary 

# ~ houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# ~ print(houses)

# ~ # Print out Harry's House
# ~ print(houses["Harry"])

# ~ # Adding values to a dictionary
# ~ houses["Hermione"] = "Gryffindor"

# ~ # Print out Hermione's House:
# ~ print(houses["Hermione"])

# Introduction to Loops
# This code will print the numbers 0 to 5

# ~ for i in [0,1, 2, 3, 4, 5]:
	# ~ print(i)
	
# ~ # Using the range function instead

# ~ for i in range(6):
	# ~ print(i)

# Create a List
# ~ names = ["Harry", "Hermione", "Ron"]

# ~ # Using a for loop to  print each name
# ~ for name in names:
	# ~ print(name)
	
# ~ # using a for loop to loop through each character in each name
# ~ name = "Harry"
# ~ for char in name:
	# ~ print(char)
	
# this is an example of a programmer defined function 
# the function is going to take the argument (x) which will be an int, and it will square it	

# ~ def square(x):
	# ~ return x * x

# ~ print(square(8))

# ~ for i in range(10):
	# ~ print(f"The square of {i} is {square(i)}")

# here we are going to write that same function in a seperate file and then import that file as a module, thereby inheriting its functionality

# ~ import square

# ~ for i in range(10):
	# ~ print(f"The square of {i}, is {square.square(i)}")


# here we are going to define our first class that defines a two dimensional point

# ~ class Point():
	# ~ # A method defining how to create a point
	# ~ def __init__(self, x, y):
		# ~ self.x = x
		# ~ self.y = y
		
# ~ # now we are going to use the code above to create an object

# ~ p = Point(2, 4)
# ~ print(p.x)
# ~ print(p.y)

# ~ class Point():
	# ~ def __init__(self, x, y):
		# ~ self.x = x
		# ~ self.y = y

# ~ p = Point(2,8)
# ~ print(p.x)
# ~ print(p.y)


# more interesting example of using a class and creating objects "airline flight example"

# ~ class Flight():
	# ~ # Method to create new flight with given capacity
	# ~ def __init__(self, capacity):
		# ~ self.capacity = capacity
		# ~ self.passengers = []
		
	# ~ # Method to add a passenger to the flight
	# ~ def add_passengers(self, name):
		# ~ if not self.open_seats(): 
			# ~ return False
		# ~ self.passengers.append(name)
		# ~ return True
		
	# ~ # Method to return number of open seats
	# ~ def open_seats(self):
		# ~ return self.capacity - len(self.passengers)
		

# ~ class Flight():
	
	# ~ def __init__(self, capacity):
		# ~ self.capacity = capacity
		# ~ self.passengers = []
	
	# ~ def add_passenger(self, name):
		# ~ if not self.open_seats():
			# ~ return False
		# ~ self.passengers.append(name)
		# ~ return True
	
	# ~ def open_seats(self):
		# ~ return self.capacity - len(self.passengers)
		

# ~ flight = Flight(3)

# ~ people = ["Mike", "Juliette", "Romeo", "Shawn"]

# ~ for person in people:
	# ~ success = flight.add_passenger(person)
	# ~ if success:
		# ~ print(f"Added {person} to flight successfully.")
	# ~ else:
		# ~ print(f"No available seats for {person}")

# list of people and their houses, nested inside of a list as a seperate dictionaries
# this is a way without using a lambda expression
# ~ people = [
	# ~ {"name": "Harry", "house": "Gryffindor"},
	# ~ {"name": "Cho", "house": "Ravenclaw"},
	# ~ {"name": "Draco", "house": "Slytherin"}
# ~ ]

# ~ # here we are going to sort all of the people and then print them all out
# ~ def f(person):
	# ~ return person["name"]
	
# ~ people.sort(key=f)
# ~ print(people)

# this is a way using a lambda expression
# ~ people = [
	# ~ {"name": "Harry", "house": "Gryffindor"},
	# ~ {"name": "Cho", "house": "Ravenclaw"},
	# ~ {"name": "Draco", "house": "Slytherin"}
# ~ ]

# ~ # here we are going to sort all of the people and then print them all out
# ~ people.sort(key=lambda person: person["name"])
# ~ print(people)

# example of exception handling
# ~ x = int(input("x: "))
# ~ y = int(input("y: "))

# ~ result = x / y
# ~ print(f"{x}/{y} = {result}")

# here is the exception handling variant
# ~ import sys
# ~ try:
	# ~ x = int(input("x: "))
	# ~ y = int(input("y: "))
# ~ except ValueError:
	# ~ print("Use the correct data type, ya dig?")
	# ~ sys.exit(1)
# ~ except EOFError:
	# ~ print("Use the correct data type, ya dig?")
	# ~ sys.exit(1)
# ~ try:
	# ~ result = x / y
# ~ except ZeroDivisionError:
	# ~ print("Error: Cannot Divide by Zero")
	# ~ sys.exit(1)

# ~ print(f"{x}/{y} = {result}")

