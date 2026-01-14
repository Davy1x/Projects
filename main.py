# Dependencies/Modules Embedded

def text(text, space, color_code=None):
    white_space = " "
    if len(str(text)) > space:
        return
    calc = space - len(str(text))
    if color_code:
        final = "\033[{}m{}{}\033[0m".format(color_code,text, white_space * calc)
        return final
    else:
        final = "{}{}".format(text, white_space * calc)
        return final

def gap(text, space, symbol=" ", color_code=None):
    half = symbol * int(space / 2)
    if color_code:
        final = "\033[{}m{} {} {}\033[0m".format(color_code, half, text, half)
        return final
    else:
        final = "{} {} {}".format(half, text, half)
        return final

# Database Embedded

RECORDS = [
    {"name": "Alice Johnson", "score": "38", "attendance": "93"},
    {"name": "Bob Smith", "score": "ninety", "attendance": "88"},
    {"name": "Carol White", "score": "150", "attendance": "95"},
    {"score": "75", "attendance": "80"},
    {"name": "Dave Brown", "score": "78", "attendance": "92.5"},
    {"name": "Eve Davis", "score": "92", "attendance": "-10"},

    {"name": "Maga Lora", "score": "23", "attendance": "86"},
    {"name": "Will Smith", "score": "23", "attendance": "34"},
    {"name": "William Anne", "score": "189", "attendance": "42"},
    {"score": "47", "attendance": "80"},
    {"name": "Micheal Jack", "score": "87", "attendance": "82.6"},
    {"name": "Mayo Kolo", "score": "37", "attendance": "-23"},

    {"name": "Guru Jank", "score": "73", "attendance": "93"},
    {"name": "Zerry Dl", "score": "89", "attendance": "100"},
    {"name": "Star Wizkid", "score": "150", "attendance": "98.1"},
    {"score": "96", "attendance": "48"},
    {"name": "David Obo", "score": "99", "attendance": "98.5"},
    {"name": "Ronaldo jr", "score": "88", "attendance": "93.76"},

    {"name": "Vini Jr", "score": "62", "attendance": "30"},
    {"name": "Burna Boy", "score": "84", "attendance": "74"},
    {"name": "Joe Boy", "score": "17", "attendance": "95"},
    {"score": "67", "attendance": "59"},
    {"name": "Davy Dale", "score": "98", "attendance": "47"},
    {"name": "Zoro wise", "score": "16", "attendance": "-74"},

    {"name": "Gojo Powa", "score": "40", "attendance": "43"},
    {"name": "Mary Jane", "score": "49", "attendance": "88"},
    {"name": "Manny Mai", "score": "97", "attendance": "45"},
    {"score": "80", "attendance": "87"},
    {"name": "Dane Day", "score": "80", "attendance": "92.5"},
    {"name": "Lollipop Bby", "score": "46", "attendance": "77"}
]

# Header / Title

print('\033[32m' + r"""
   _____ __            __           __     ______               __                 ____
  / ___// /___  ______/ /__  ____  / /_   / ____/________ _____/ /__              / __ \_________  ________  ______________  _____
  \__ \/ __/ / / / __  / _ \/ __ \/ __/  / / __/ ___/ __ `/ __  / _ \   ______   / /_/ / ___/ __ \/ ___/ _ \/ ___/ ___/ __ \/ ___/
 ___/ / /_/ /_/ / /_/ /  __/ / / / /_   / /_/ / /  / /_/ / /_/ /  __/  /_____/  / ____/ /  / /_/ / /__/  __(__  |__  ) /_/ / /    
/____/\__/\__,_/\__,_/\___/_/ /_/\__/   \____/_/   \__,_/\__,_/\___/           /_/   /_/   \____/\___/\___/____/____/\____/_/ 
""" + '\033[0m')

# Part 1: Student Record Processor (50 points)
# Create a function called process_student_record() that:
# Accepts a dictionary containing student information with keys: 'name', 'score', and 'attendance'
# Validates that all required fields are present (handle KeyError)
# Converts the score to an integer (handle ValueError if conversion fails)
# Validates that the score is between 0 and 100 (raise ValueError if out of range)
# Converts attendance to a float (handle ValueError if conversion fails)
# Validates that attendance is between 0 and 100 (raise ValueError if out of range)
# Calculates the final grade using the formula: final_grade = score * 0.7 + attendance * 0.3
# Returns a dictionary with processed data including the final grade
# Uses try-except-finally blocks appropriately
# Includes a finally block that prints "Processing completed for record"

# import os
# import json
# import pyfiglet
# import module.align as align

# RECORDS = list()

# BASE_PATH = os.path.dirname(__file__)
# with open(os.path.join(BASE_PATH,"records.json"), 'r') as buffer:
#     RECORDS = json.loads(buffer.read())

# print('\033[32m' + pyfiglet.figlet_format("Student Grade - Processor", font='slant', width=500) + '\033[0m')

def process_student_record(records:list()):

    # Validates that all required fields are present (handle KeyError)

    for index in range(len(records)):
        try:
            if records[index]["name"] and records[index]["score"] and records[index]["attendance"]:
                continue
        except KeyError as keyErr:
            err = str(keyErr)
            if err == "'name'":
                records[index]["name"] = 'null'
            elif err == "'score'":
                records[index]["score"] = '0'
            elif err == "'attendance'":
                records[index]["attendance"] = '0'

    # Converts the score to an integer (handle ValueError if conversion fails)

    for index in range(len(records)):
        try:
            records[index]["score"] = int(records[index]["score"])
        except ValueError:
            records[index]["score"] = 0

    # Validates that the score is between 0 and 100 (raise ValueError if out of range)

    # for index in range(len(records)):
    #     if records[index]["score"] > 100 or records[index]["score"] < 0:
    #         raise ValueError(f"{records[index]['name']}'s score sholud be between 100 & 0")

    # Converts attendance to a float (handle ValueError if conversion fails)

    for index in range(len(records)):
        try:
            records[index]["attendance"] = float(records[index]["attendance"])
        except ValueError:
            records[index]["attendance"] = 0.0

    # Validates that attendance is between 0 and 100 (raise ValueError if out of range)

    # for index in range(len(records)):
    #     if records[index]["attendance"] > 100 or records[index]["attendance"] < 0:
    #         raise ValueError(f"{records[index]['name']}'s score sholud be between 100 & 0")

    # Calculates the final grade using the formula: final_grade = score * 0.7 + attendance * 0.3

    try:
        final_grade = lambda score, attendance: round((score * 0.7) + (attendance * 0.3), 2)
        for index in range(len(records)):
            score, attendance = records[index]["score"], records[index]["attendance"]
            records[index]["final_grade"] = final_grade(score, attendance)
    except Exception:
        records[index]["final_grade"] = 0

    # Returns a dictionary with processed data including the final grade

    return records

try:
    processed_data = process_student_record(RECORDS)
    print(gap("COMPLETE LIST OF STUDENT RECORDS", 40, color_code=33), end='\n\n')
    print(text('NAME', 19, color_code=32), text('SCORE', 19, color_code=32), text('ATTENDANCE', 19, color_code=32), text('FINAL GRADE', 19, color_code=32), end='\n\n')

    for index in range(len(processed_data)):
        data = processed_data[index]
        print(text(data['name'], 20), text(data['score'], 20), text(data['attendance'], 20), text(data['final_grade'], 20))
except Exception:
    print('An Unexpected Error Occured - Please Debug!')
finally: 
    print('\n\n' + gap("PROCESSING COMPLETED FOR RECORD!", 40, color_code=32), end='\n\n')
pg2 = input("Enter to continue...")

# Part 2: Batch Processing (30 points)
# Create a function called process_class_records() that:
# Accepts a list of student record dictionaries
# Processes each record using your process_student_record() function
# Continues processing even if some records have errors (doesn't stop on first error)
# Keeps track of successful and failed records
# Returns a summary dictionary containing: 
# Total records processed
# Number of successful records
# Number of failed records
# List of successfully processed students
# List of errors encountered

def process_class_records(records:list()):

    TOTAL = 0
    SUCCESSFUL_RECORDS = []
    FAILED_RECORDS = []
    SUMMARY_OBJ = dict()

    SUMMARY_OBJ['total_records_processed'] = TOTAL
    SUMMARY_OBJ['no_successfull_records'] = len(SUCCESSFUL_RECORDS)
    SUMMARY_OBJ['no_failed_records'] = len(FAILED_RECORDS)
    SUMMARY_OBJ['successfull_records'] = []
    SUMMARY_OBJ['failed_records'] = []

    for index in range(len(records)):
        if records[index]['name'] != 'null':
             SUMMARY_OBJ['successfull_records'].append(records[index]['name'])
        else:
            SUMMARY_OBJ['failed_records'].append(records[index]['name'])


    # List of successfully processed students

    print(gap("COMPLETE LIST OF SUCCESSFUL STUDENT RECORDS", 28, color_code=33), end='\n\n')
    print(text('NAME', 19, color_code=32), text('SCORE', 19, color_code=32), text('ATTENDANCE', 19, color_code=32), text('FINAL SCORE', 19, color_code=32), end='\n\n')
    for index in range(len(records)):
        data = records[index]
        if records[index]['name'] != 'null':
            print(text(data['name'], 20), text(data['score'], 20), text(data['attendance'], 20), text(data['final_grade'], 20))
    
    pg2 = input("\nEnter to continue...")
    # List of errors encountered

    print('\n\n' + gap("COMPLETE LIST OF UNSUCCESSFUL STUDENT RECORDS", 28, color_code=33), end='\n\n')
    print(text('NAME', 19, color_code=32), text('SCORE', 19, color_code=32), text('ATTENDANCE', 19, color_code=32), text('FINAL SCORE', 19, color_code=32), end='\n\n')
    for index in range(len(records)):
        data = records[index]
        if records[index]['name'] == 'null':
            print(text(data['name'], 20), text(data['score'], 20), text(data['attendance'], 20), text(data['final_grade'], 20))
    print('\n' + gap("[ Issue ] Students in this record could not be identified!", 6, color_code=31), end='\n\n')
    pg2 = input("\nEnter to continue...")
process_class_records(processed_data)

# Part 3: Safe Calculator (20 points)
# Create a function called calculate_class_average() that:
# Accepts a list of final grades (numbers)
# Calculates the average of all grades
# Handles ZeroDivisionError if the list is empty
# Handles TypeError if non-numeric values are in the list
# Uses try-except-else-finally blocks: 
# try: Attempt to calculate the average
# except: Handle specific errors
# else: Print "Calculation successful" (only if no errors)
# finally: Print "Average calculation completed"
# Returns the average or None if an error occurs

def calculate_class_average(records:list()):
    AVG_LIST = []
    AVG_TOTAL = 0
    try:
        for index in range(len(records)):
            AVG_LIST.append(records[index]['final_grade'])
        AVG_TOTAL = sum(AVG_LIST) / len(AVG_LIST)
    except (ZeroDivisionError, TypeError, ValueError):
        print('An Unexpected Error Occured - Please Debug!')

    print('\n\n' + gap(f"TOTAL AVERAGE OF ALL STUDENTS ON THE RECORD: {round(AVG_TOTAL, 2)}", 16, color_code=33), end='\n\n')
    print('\n\n' + gap("CALCULATION SUCCESSFUL", 40, color_code=33), end='\n\n')

calculate_class_average(RECORDS)