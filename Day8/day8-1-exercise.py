# Create a function called greet()

def greet():
    print("Hello!")
    print("How is it going?")
    print("See you again!")

# Create a function called greet_with_name() 

def greet_with_name(name):
    print(f"\nHello {name}!")
    print("How is it going?")
    print(f"See you again, {name}!")

def greet_with(name, location):
    print(f"\nHello {name}, how is it going?")
    print(f"Did you go to {location} last week?")

greet()
greet_with_name("Robert")
greet_with("Jack", "New York")