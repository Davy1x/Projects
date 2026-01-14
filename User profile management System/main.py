# Intermediate Level
# Build a user profile management system that:
# ⦁	Creates a dictionary to store user information (name, age, department, skills)
# ⦁	Uses a tuple to store system configuration (version, max_users, timeout)
# ⦁	Implements type conversion for user input validation
# ⦁	Uses slicing to extract subsets of user data (e.g., first 5 skills, last login date)
# ⦁	Creates parallel lists for user_ids, usernames, and last_login dates
# ⦁	Uses negative indexing to access most recent records
# ⦁	Demonstrates the difference between mutable and immutable operations
# ⦁	Shows proper variable reassignment techniques
# ⦁	Implements slicing-based data sampling (every Nth user)
# ⦁	Includes error handling for invalid type conversions


# Creates a dictionary to store user information (name, age, department, skills)
profile = {
    "profile1": {
        "name": "Alice Johnson",
        "age": 28,
        "department": "Marketing",
        "skills": ["SEO", "Content Writing", "Social Media"]
    },
    "profile2": {
        "name": "Brian Kim",
        "age": 34,
        "department": "Engineering",
        "skills": ["Python", "Machine Learning", "Data Analysis"]
    },
    "profile3": {
        "name": "Cynthia Lopez",
        "age": 26,
        "department": "Human Resources",
        "skills": ["Recruitment", "Communication", "Conflict Resolution"]
    },
    "profile4": {
        "name": "David Smith",
        "age": 41,
        "department": "Finance",
        "skills": ["Excel", "Budgeting", "Financial Modeling"]
    },
    "profile5": {
        "name": "Emma Brown",
        "age": 30,
        "department": "Design",
        "skills": ["UI/UX Design", "Adobe XD", "Prototyping"]
    }
}
# print(profile)

# Uses a tuple to store system configuration (version, max_users, timeout)
SYS_CONFIG = ({'version': '8.0.11'}, {'max_users': 5}, {'timeout': 30})
# print(SYS_CONFIG)

# Implements type conversion for user input validation
user_input = input('Enter an integer: ')
converted_input = int(user_input)
# print(converted_input)

# Uses slicing to extract subsets of user data (e.g., first 5 skills, last login date)
profile_slice = profile['profile2']['skills'][:2]
# print(profile_slice)

# Creates parallel lists for user_ids, usernames, and last_login dates
user = [
    ['florida', 'star-monkey', 'gorilla', 'monster'],
    ['jk6353', 'qf73864', 'gh3738d', 'yusj9dh'],
    ['23-04-1991', '11-07-2020', '27-03-2012', '12-12-2012']
]

# Uses negative indexing to access most recent records
recent_record = user[-1][0]
# print(recent_record)

# Demonstrates the difference between mutable and immutable operations

mutable_var = 'Hi i am mutable'
mutable_var = 'What!, i have been updated' #updates the value in memory

non_mutable_var = ('fred', 'john')
non_mutable_var.__add__(tuple(('james', 'lollipop'))) #does not update the value in memory
# print(non_mutable_var)

# Shows proper variable reassignment techniques
reasign = [56, 84, 84, 74, 94, 84]
new_reasign = [100, 600, 1000]
reasign = new_reasign
# print(reasign)

# Implements slicing-based data sampling (every Nth user)
nth_slicing = user[1][::2]
# print(nth_slicing)

# Includes error handling for invalid type conversions
try:
    user_input = input('Enter an integer: ')
    converted_input = int(user_input)
    print(converted_input)
except (TypeError, ValueError):
    print('An error was caught - err')





# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE