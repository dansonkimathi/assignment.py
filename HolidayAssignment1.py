def get_numbers_from_user():
    input_numbers=input("Enter a list of numbers separated by spaces:")
    number_strings=input_numbers.split()
    numbers=[float(num)for num in number_strings]
    return numbers
def calculate_sum(numbers):
    return sum(numbers)
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)
def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)
def find_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)
def filter_even_numbers(numbers):
    return[num for num in numbers if num % 2 ==0]
# Main program
user_numbers=get_numbers_from_user()
# Calculate and dsplay results
print("List of numbers:", user_numbers)
print("Sum:",calculate_sum(user_numbers))
print("Average:",calculate_average(user_numbers))
print("Maximum:",find_maximum(user_numbers))
print("Minimum:",find_minimum(user_numbers))
# Filter out evennumbers and display the result
even_numbers = filter_even_numbers(user_numbers)
print("Even numbers:",even_numbers)