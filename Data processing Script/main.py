# Beginner Level
# Create a data processing script that:
# ⦁	Initializes a list called data_entries with ten string values (e.g., filenames)
# ⦁	Uses slicing to extract the first 3, last 3, and middle 4 elements
# ⦁	Creates a string and reverses it using slicing
# ⦁	Samples every 3rd element from the list
# ⦁	Uses input() to get a number from the user (as string)
# ⦁	Converts the string to an integer and multiplies by 2
# ⦁	Adds the result as a new entry to the list
# ⦁	Prints both the updated list and calculation result
# ⦁	Use descriptive variable names and add comments explaining each step

# Initializes a list called data_entries with ten string values (e.g., filenames)
data_entries = [
    '/cars/Toyota.json',
    '/cars/Honda.json',
    '/cars/Ford.json',
    '/cars/Tesla.json',
    '/cars/Chevrolet.json',
    '/cars/BMW.json',
    '/cars/Audi.json',
    '/cars/Mercedes-Benz.json',
    '/cars/Porsche.json',
    '/cars/Lamborghini.json',
]

# Uses slicing to extract the first 3, last 3, and middle 4 elements
first_three = data_entries[0:3]
last_three = data_entries[7:10]
middle_four = data_entries[3:7]
print(middle_four)

# Creates a string and reverses it using slicing
text = 'Javascript_V8'
reversed_str = text[::-1]
print(reversed_str)

# Samples every 3rd element from the list
list_sample_3rd = data_entries[::2]
# print(list_sample_3rd)

try:
    user_num = input('Enter a number: ') #Uses input() to get a number from the user (as string)
    user_num_converted = int(user_num) * 2 #Converts the string to an integer and multiplies by 2
    data_entries.append(user_num_converted) #Adds the result as a new entry to the list
    print(data_entries) #Prints both the updated list and calculation result
    print(user_num_converted) #Prints both the updated list and calculation result
except (ValueError, TypeError):
    print('Only Integral Values Allowed')






# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE