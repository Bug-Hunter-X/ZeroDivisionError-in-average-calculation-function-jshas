def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Demonstrates the error handling
my_list = []
try:
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ZeroDivisionError:
    print("Error: Cannot calculate average of an empty list")