def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

#Example of the error
my_list = []
result = calculate_average(my_list) #ZeroDivisionError: division by zero
print(f"The average is: {result}")