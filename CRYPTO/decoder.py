import json

class Decoder:
	def __init__(self):
		self._path = './ascii.json'
		with open(self._path, 'r') as _engine:
			self._ASCII = json.load(_engine)
		
	def _binDecode(self, __crypt):
		_decoded_dec = list()
		_decoded_bin = list()
		for _bytes in __crypt:
			_decoded_bytes = int()
			_index = 0
			for _bits in _bytes:
				x = int(_bits) * (2 ** _index)
				_index += 1
				_decoded_bytes += x
			_decoded_dec.append(_decoded_bytes)
		for _decs in _decoded_dec:
			for _ in range(len(self._ASCII["data"])):
				if _decs == self._ASCII["data"][_]["dec"]:
					_decoded_bin.append(self._ASCII["data"][_]["char"])
		return("".join(_decoded_bin))
				
	def _hexDecode(self, __crypt):
		_decoded_hex = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["hex"]:
					_decoded_hex.append(self._ASCII["data"][_]["char"])
		return("".join(_decoded_hex))
					
	def _octDecode(self, __crypt):
		_decoded_oct = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if _chr == self._ASCII["data"][_]["oct"]:
					_decoded_oct.append(self._ASCII["data"][_]["char"])
		return("".join(_decoded_oct))
		
	def _decDecode(self, __crypt):
		_decoded_dec = list()
		for _chr in __crypt:
			for _ in range(len(self._ASCII["data"])):
				if int(_chr) == self._ASCII["data"][_]["dec"]:
					_decoded_dec.append(self._ASCII["data"][_]["char"])
		return("".join(_decoded_dec))

decode = Decoder()