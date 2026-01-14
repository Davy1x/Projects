import os
import time
from ZeusEncryptZ8Engine.execution import Zeus

filename_stdin = input('Enter Database You Wish To Encrypt: ')

MEMORY_DATA = str()
SAVE_PATH = os.path.join(os.path.dirname(__file__), f'ENCRYPTED_DATA')
DB_PATH = os.path.join(os.path.dirname(__file__), f'UNENCRYPTED_DATA\\{filename_stdin}')
try:
    with open(DB_PATH, 'r') as database:
        MEMORY_DATA = database.read()
except FileNotFoundError:
    print('[ FILE NOT FOUND ERROR ] CONFIRM DATABASE IS STORED IN THE "UNENCRYPTED_DATA" FOLDER'); exit()

def _CRYPTONIC_(D, E):
    try:
        data_obj = {
            "Data": MEMORY_DATA,
            "Decrypt": D,
            "Encrypt": E,
            "AllowMetadata": True,
            "AllPackages": False
        }
        response = Zeus({ **data_obj }).process()
        print(f"\n\033[33mresponse['metadata']\033[0m\n")
        if E:
            encrypted_fileName = SAVE_PATH +'\\'+ str(round(time.time())) + '.txt'
        else:
            encrypted_fileName = SAVE_PATH +'\\'+ str(round(time.time())) + '.json'
        
        with open(encrypted_fileName, 'w') as encrypted_buffer:
            encrypted_buffer.write(response['data'])
        print(f'[ ENCRYPTION SUCCESS ] DATABASE ENCRYPTED SUCCESSFULLY - {encrypted_fileName}'); exit()
    except FileExistsError:
        print('[ FILE EXIST ERROR ] CONFIRM NO DUPLICATE FILE NAMES EXIST'); exit()

def Initialization():
    user_stdin = input('[ 00 ] ENCRYPT DATABASE\n[ 11 ] DECRYPT DATABASE\nENTER CHOICE: ')
    if user_stdin == '00':
        _CRYPTONIC_(False, True)
    elif user_stdin == '11':
        _CRYPTONIC_(True, False)
    else:
        print('[ INVALID CHOICE ]'); return

if __name__ == '__main__':
    Initialization()



# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE