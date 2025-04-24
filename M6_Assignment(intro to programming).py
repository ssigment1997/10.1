# Get 20 numbers from the user, separated by spaces
numbers_input = input('Enter 20 numbers separated by spaces: ')

# Convert the input string into a list of integers
number_list = [int(num) for num in numbers_input.split()]

# Check if the user entered exactly 20 numbers
if len(number_list) != 20:
    print("Please enter exactly 20 numbers.")
else:
    print(f'The lowest is {min(number_list)}')
    print(f'The largest is {max(number_list)}')
    print(f'The sum is {sum(number_list)}')
    print(f'The average is {sum(number_list) / len(number_list)}')
