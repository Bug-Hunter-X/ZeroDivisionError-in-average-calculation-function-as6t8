def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with an empty list and non empty list
my_list = []
result = calculate_average(my_list) #This will return 0
print(f"The average of empty list is: {result}")
my_list = [10, 20, 30]
result = calculate_average(my_list) #This will return 20.0
print(f"The average of non-empty list is: {result}") 