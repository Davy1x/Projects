import os
import time
from decoder import *
from encoder import *

def _stdin_(_coder_func, _tag):
	_meta = str(time.time()).split('.')[0]
	f_path = './CRYPTS/{:#x}.txt'.format(int(_meta))
	if _tag == 'd':
		_stdin = input('Enter Code: ').strip().split(' ')
		_array_ = [chr for chr in _stdin if chr != ' ']
		_crypt__ = _coder_func(_array_)
		if os.path.exists('./CRYPTS'):
			try:
				with open(f_path, 'w') as _log:
					_log.write(_crypt__)
					print('\n', _crypt__, end='\n\n')
					print("[ CRYPTS LOGGED ]")
			except (PermissionError, FileExistsError):
				print('\n', _crypt__, end='\n\n')
		else:
			print('\n', _crypt__, end='\n\n')
			
	elif _tag == 'en':
		_stdin = input('Enter Text: ').strip()
		_array_ = [chr for chr in _stdin]
		__crypt_ = _coder_func(_array_)
		if os.path.exists('./CRYPTS'):
			try:
				with open(f_path, 'w') as _log:
					_log.write(__crypt_)
					print('\n', __crypt_, end='\n\n')
					print("[ CRYPTS LOGGED ]")
			except (PermissionError, FileExistsError):
				print('\n', _crypt__, end='\n\n')
		else:
			print('\n', _crypt__, end='\n\n')

def _user_interface():
    os.system('clear')
    print(
        "\033[92m[001] [ LAUNCH DECODER ]\
    	\n[002] [ LAUNCH ENCODER ]\
    	\n[404] [  EXIT PROGRAM  ]"
    )
    _stdin_cls = input('[KEY] $')
    if _stdin_cls == '001':
    	os.system('clear')
    	print(
    		"[010] [    BINARY DECODER    ]\
    		\n[020] [ HEXADECIMAL DECODER  ]\
    		\n[030] [ OCTA-DECIMAL DECODER ]\
    		\n[040] [   DECIMAL DECODER    ]"
    	)
    	_stdin_mth = input('[KEY] $')
    	if _stdin_mth == '010':
    		_stdin_(decode._binDecode, 'd')
    	elif _stdin_mth == '020':
    		_stdin_(decode._hexDecode, 'd')
    	elif _stdin_mth == '030':
    		_stdin_(decode._octDecode, 'd')
    	elif _stdin_mth == '040':
    		_stdin_(decode._decDecode, 'd')
    	else:
    		print("[ERR][ invalid choice ]")
    		exit()
    elif _stdin_cls == '002':
    	os.system('clear')
    	print(
    		"[010] [    BINARY ENCODER    ]\
    		\n[020] [ HEXADECIMAL ENCODER  ]\
    		\n[030] [ OCTA-DECIMAL ENCODER ]\
    		\n[040] [   DECIMAL ENCODER    ]"
    	)
    	_stdin_mth = input('[KEY] $')
    	if _stdin_mth == '010':
    		_stdin_(encode._binEncode, 'en')
    	elif _stdin_mth == '020':
    		_stdin_(encode._hexEncode, 'en')
    	elif _stdin_mth == '030':
    		_stdin_(encode._octEncode, 'en')
    	elif _stdin_mth == '040':
    		_stdin_(encode._decEncode, 'en')
    	else:
    		print("[ERR][ invalid choice ]")
    		exit()
    elif _stdin_cls == '404':
    	print("[EXT][ PROGRAM TERMINATED ]")
    	exit()
    else:
    	print("[ERR][ invalid choice ]")
    	exit()
    	
if __name__ == '__main__':
	_user_interface()