# Create a data pipeline setup script that:  
# • Initializes variables for database_name, table_count, and status
# • Uses input() to collect database connection details  
# • Reassigns variables based on user input  
# • Demonstrates proper variable naming (avoid single letters)  
# • Uses both single-line and multi-line operations  
# • Include error prevention comments 

import os
import time
import json

SECURITY_KEY = str()
try:
    with open(os.path.dirname(__file__) + '\\sys_key.txt', 'r') as access_key:
        SECURITY_KEY = access_key.read()
except FileNotFoundError:
    print("[ ERROR ] ACCESS KEY NOT FOUND"); exit()

STATUS = str() #status
DATA_STREAM = dict()
TABLE_COUNT = str() #table_count
DATA_PATH = str()
DB_NAME = () #database_name

def Initialization():
    global DATA_STREAM, DATA_PATH, DB_NAME, TABLE_COUNT, STATUS

    DATA_PATH = os.path.join(os.path.dirname(__file__), 'car-data.json')
    DB_NAME = DATA_PATH.split('\\')[len(DATA_PATH.split('\\')) - 1] #database_name
    try:
        with open(DATA_PATH, 'r') as database:
            DATA_STREAM = json.loads(database.read()); STATUS = 'Running'
            TABLE_COUNT = len(DATA_STREAM["cars"]) #table_count

    except FileNotFoundError:
        print("[ ERROR ] DATABASE NOT FOUND"); STATUS = 'Crashed'; exit()
        
    print('[ 001 ] VIEW CAR DATA\n[ 002 ] EDIT CAR DATA')
    std_in_stream = input('Enter choice: ')
    if std_in_stream == '001':
        display_db()
    elif std_in_stream == '002':
        edit_db()
    else:
        print('[ Invalid Choice ]')

def display_db():
    space_align = lambda z: " " * (20 - z)
    print('\033[33mMODEL               ENGINE               MAKE               DATE               VERSION               FUEL               WHEELS               KM\\HR               MAX-SPEED\033[0m\n')
    for index in range(len(DATA_STREAM['cars'])):
        car = DATA_STREAM['cars'][index]
        print(f"{car['car_model']}{space_align(len(car['car_model']))}{car['engine_type']}{space_align(len(car['engine_type']))}{car['make']}{space_align(len(car['make']))}{car['date_created']}{space_align(len(car['date_created']))}{car['version']}{space_align(len(str(car['version'])))}{car['fuel_type']}{space_align(len(car['fuel_type']))}{car['num_wheels']}{space_align(len(str(car['num_wheels'])))}{car['km_per_hr']}{space_align(len(str(car['km_per_hr'])))}{car['max_speed']}")

def edit_db():
    car_name = input('Enter car name: ')
    print('Available Categories: car_model | engine_type | make | date_created | version | fuel_type | num_wheels | km_per_hr | max_speed')
    car_category = input('Enter Category: ') #Chevrolet Bolt
    category_value = input('Enter New Value: ')

    for index in range(len(DATA_STREAM['cars'])):
        # car = DATA_STREAM['cars'][index]
        if car_name == DATA_STREAM['cars'][index]['car_model']:
            try:
                if DATA_STREAM['cars'][index][car_category]:
                    # print(DATA_STREAM['cars'][index]['car_model'], DATA_STREAM['cars'][index][car_category])
                    DATA_STREAM['cars'][index][car_category] = category_value
                    print(f"\n[ Successfully Updated {car_name}'s {car_category}]\n"); display_db()
                    return
            except KeyError:
                print(f'\n[ Invalid Choice ] {car_category} is Unavailable\n')
                return
        else:
            continue
    print(f'\n[ Invalid Choice ] {car_name} is Unavailable\n')


if __name__ == "__main__":
    validate = input('Enter Security Key To Connect: ')
    if validate == SECURITY_KEY:
        print('[ ACCESS GRANTED ] Welcome Back To Our Car Collection Data Center'); Initialization()
    else:
        print('[ ACCESS DENIED ] Unauthorized Access Detected'); exit()





# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE