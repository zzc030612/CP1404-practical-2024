# Task 1: Ask the user for their name and write it to a file called 'name.txt'
name = input("Enter your name: ")
out_file = open("name.txt", "w")  # Open the file in write mode
out_file.write(name)  # Write the name to the file
out_file.close()  # Close the file

# Task 2: Read the name from 'name.txt' and print a greeting
in_file = open("name.txt", "r")  # Open the file in read mode
name = in_file.read().strip()  # Read the name from the file and remove any extra spaces or newlines
in_file.close()  # Close the file

print(f"Hi {name}!")  # Print the greeting with the name from the file

# Task 3: Open 'numbers.txt', read the first two numbers and print their sum
with open("numbers.txt", "r") as in_file:  # Use 'with' to automatically handle closing the file
    number1 = int(in_file.readline())  # Read the first number
    number2 = int(in_file.readline())  # Read the second number
    result = number1 + number2  # Add the two numbers together

print(f"The sum of the first two numbers is: {result}")

# Task 4: Open 'numbers.txt' and calculate the total of all the numbers
total = 0
with open("numbers.txt", "r") as in_file:  # Use 'with' to open the file
    for line in in_file:  # Iterate through each line in the file
        total += int(line.strip())  # Convert each line to an integer and add it to the total

print(f"The total of all numbers is: {total}")