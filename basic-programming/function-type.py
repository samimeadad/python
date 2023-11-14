# there are 2 types of functions
# 1 - that performs a task
# 2 - that returns a value

# function that returns a value

def greet(name):
    return f"Welcome {name}!"


message = greet("Sami")
file = open("content.txt", "w")
file.write(message + "\n")
message = greet("Ammapakhi")
file = open("content.txt", "a")
file.write(message + "\n")
