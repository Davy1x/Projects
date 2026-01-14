import os
import json
import time

class Hexabyte:
	def __init__(self, __path):
		self._content = []
		self._encoded = []
		self._path = __path
		with open('ascii.json', 'r') as _base:
			db = _base.read()
			self.ascii = json.loads(db)
		self.__loadFile__()
			
	def __loadFile__(self):
			_textFiles = os.listdir('./_texts/')
			if not self._path in _textFiles:
				print("[404] FileNotFound")
				return None
			else:
				with open(f'./_texts/{self._path}', 'r') as file:
					_texts = file.read()
					if _texts:
						self._content = [chr for chr in _texts]
						self.__encodeFile__()
					else:
						print("[404] FileEmpty")
						return None
					
	def __encodeFile__(self):
			for chars in self._content:
					for _ in range(len(self.ascii["data"])):
						if chars == self.ascii["data"][_]["char"]:
							_x = self.ascii["data"][_]["hex"]
							self._encoded.append(_x)
			with open(f'./_encodes/{self._path}', 'w') as file:
					_nCrypt = [ch.replace('0x','') for ch in self._encoded]
					file.write("".join(_nCrypt))
					print("[200] FileEncoded")
					return None
					
					
					
				
			
			
			
			
			
			


if __name__ == '__main__':
	hexa = Hexabyte
	
	print('Files must be stored in the < _texts > directory.\nNote: Only text files are allowed.')
	
	_stdin = input('Enter File Name: ').strip()
	hexa(_stdin)