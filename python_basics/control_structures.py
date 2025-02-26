# Function to classify even or odd
def classify_number(num):
    return "Even" if num % 2 == 0 else "Odd"

# user for input
user_input = int(input("Enter an integer: "))
print(f"The number {user_input} is {classify_number(user_input)}.")

# Generating a list of even numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

# A while loop that prints numbers from 10 to 1 in reverse
count = 10
while count >= 1:
    print(count)
    count -= 1
