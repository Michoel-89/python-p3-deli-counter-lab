def line(line):
    currentPlace = []
    i = 1
    for person in line:
        currentPlace.append(f'{i}. {person}')
        i += 1
    if(len(line) < 1):
        print("The line is currently empty.")
    elif(len(line) >= 1):
        print(f"The line is currently: {' '.join(currentPlace)}")

def take_a_number(line, name):
    line.append(f'{name}')
    num = len(line)
    print(f'Welcome, {name}. You are number {num} in line.')
    return line

def now_serving(line):
    if(len(line) < 1):
        print("There is nobody waiting to be served!")
    elif(len(line) >= 1):
        print(f'Currently serving {line[0]}.')
        del line[0]

# take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
# take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
# take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.

# line(katz_deli)

# now_serving(katz_deli) #=> "Currently serving Ada."

# line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"

# take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.

# line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"

# now_serving(katz_deli) #=> "Currently serving Grace."

# line(katz_deli) #=> "The line is currently: 1. Kent 2. Matz"

