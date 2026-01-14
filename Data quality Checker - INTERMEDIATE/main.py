# # Intermediate Level
# # Build a data quality checker that:
# # • Processes a list of user records (dictionaries with name, age, email fields) 
# # • Uses nested conditionals to validate each field (age between 0-120, email contains @) 
# # • Uses while loop with retry logic for "corrupted" records 
# # • Implements break condition when too many invalid records found 
# # • Uses logical operators (and, or) for complex validation rules 
# # • Generates summary report of data quality issues

# # Processes a list of user records (dictionaries with name, age, email fields)
import time

PROSESS_START_TIME = time.time()

USER_RECORDS = [
    {'name' : 'Jago', 'age' : 34, 'email' : 'jagolita34@gmail.com'},
    {'name' : 'Pala', 'age' : -74, 'email' : 'palabota74@gmail.io'},
    {'name' : 'Nana', 'age' : 73, 'email' : 'nanafaco73@gmail.outlook'},
    {'name' : 'Mani', 'age' : 24, 'email' : 'unavailable'},
    {'name' : 'Boka', 'age' : 82, 'email' : 'bokala82@gmail.com'}
]

print('\nRAW DATASET\n')
for _ in USER_RECORDS:
    print(_)

VALID_DATA = []
INVALID_DATA = []
TERMINATE_PROCESS = False


def TERMINATOR():
    global TERMINATE_PROCESS
    # TERMINATE RETRY LOGIC / PROCESS
    # print(round(time.time() - PROSESS_START_TIME))
    if round(time.time() - PROSESS_START_TIME) >= 10: TERMINATE_PROCESS = True
    else: return

# Uses nested conditionals to validate each field (age between 0-120, email contains @) 
for index in range(len(USER_RECORDS)):
    if USER_RECORDS[index]['age'] > 0 and USER_RECORDS[index]['email'] != 'unavailable': # Uses logical operators (and, or) for complex validation rules 
        if USER_RECORDS[index]['age'] < 120 and bool(USER_RECORDS[index]['email'].count('@')): # Uses logical operators (and, or) for complex validation rules 
            VALID_DATA.append(USER_RECORDS[index]['name'])
        else:
            INVALID_DATA.append(USER_RECORDS[index]['name'])
    else:
        INVALID_DATA.append(USER_RECORDS[index]['name'])

# Uses while loop with retry logic for "corrupted" records
temp_index = int()
duration_timeout = 0
print('\nRETRY MECHANISM\n')
while True:
    try:
        if not TERMINATE_PROCESS: TERMINATOR()
        else: break # Implements break condition when too many invalid records found
        for name in INVALID_DATA:
            # temp_index = INVALID_DATA.index(name)
            for index in range(len(USER_RECORDS)):
                if USER_RECORDS[index]['name'] == name:
                    temp_index = USER_RECORDS.index(USER_RECORDS[index])
                    if (USER_RECORDS[index]['age'] < 120 and USER_RECORDS[index]['age'] > 0) and bool(USER_RECORDS[index]['email'].count('@')): # Uses logical operators (and, or) for complex validation rules 
                        VALID_DATA.append(USER_RECORDS[index]['name'])
                    else:
                        print(f"[ STATUS ] Loading {name.capitalize()}'s Data - Retrying... [{duration_timeout}/10]")
        duration_timeout += 1
        time.sleep(1)
    except (KeyError, ValueError, InterruptedError, KeyboardInterrupt):
        print('[ ERROR ] AN ERROR OCCURED - PROCESS TERMINATED'); break

# Generates summary report of data quality issues
def status_check(index):
    if (USER_RECORDS[index]['age'] < 120 and USER_RECORDS[index]['age'] > 0) and bool(USER_RECORDS[index]['email'].count('@')):
        return 'VALID'
    else:
        return 'INVALID'

def quality_check(index):
    if (USER_RECORDS[index]['age'] > 0 and USER_RECORDS[index]['email'].endswith('.com')) and bool(USER_RECORDS[index]['email'].count('@')):
        return '100%'
    elif USER_RECORDS[index]['age'] > 0 and bool(USER_RECORDS[index]['email'].count('@')):
        return '60%'
    elif USER_RECORDS[index]['age'] < 0 and bool(USER_RECORDS[index]['email'].count('@')):
        return '20%'
    elif USER_RECORDS[index]['age'] > 0 and not bool(USER_RECORDS[index]['email'].count('@')):
        return '0%'

space_gen = lambda x: " " * (30 - x)
print('\nDATASET SUMMARY\n')
print('\n\033[33mNAME                         AGE                            EMAIL                         STATUS                         QUALITY\033[0m\n')
for index in range(len(USER_RECORDS)):
    data = USER_RECORDS[index]
    print(f"{data['name']}{space_gen(len(data['name']))}{data['age']}{space_gen(len(str(data['age'])))}{data['email']}{space_gen(len(data['email']))}{status_check(index)}{space_gen(len(status_check(index)))}{quality_check(index)}")






# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE