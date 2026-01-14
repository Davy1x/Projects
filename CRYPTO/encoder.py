import json

class Encoder:
	def __init__(self):
		self._path = './ascii.json'
		with open(self._path, 'r') as _engine:
			self._ASCII = json.load(_engine)
		
	def _binEncode(self, __crypt):
		_encoded_dec = list()
		_encoded_bytes = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["char"]:
					_encoded_dec.append(self._ASCII["data"][_]["dec"])
		_divisor = int()
		for _decs in _encoded_dec:
			_divisor = _decs
			_divider = str()
			while _divisor != 0:
				_x = _divisor % 2
				_divider += str(_x)
				_divisor = _divisor // 2
			_encoded_bytes.append(_divider)
		return(" ".join(_encoded_bytes))
	
	def _hexEncode(self, __crypt):
		_encoded_hex = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["char"]:
					_encoded_hex.append(self._ASCII["data"][_]["hex"])
		return(" ".join(_encoded_hex))
					
	def _octEncode(self, __crypt):
		_encoded_oct = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["char"]:
					_encoded_oct.append(self._ASCII["data"][_]["oct"])
		return(" ".join(_encoded_oct))
		
	def _decEncode(self, __crypt):
		_encoded_dec = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["char"]:
					_encoded_dec.append(str(self._ASCII["data"][_]["dec"]))
		return(" ".join(_encoded_dec))
		
encode = Encoder()