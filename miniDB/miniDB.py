import os
import json
import threading

class MiniDatabase:
	def __init__(self, _dbFile):
		if not _dbFile.endswith('.json'):
			_dbFile = f"{_dbFile}.json"
		self._dbFile = _dbFile
		self._thread_lock = threading.Lock()
		if not os.path.exists(f'./{self._dbFile}'):
			with open(f"./{self._dbFile}", 'w') as dbFile:
				dbFile.write('{"minidb" : {}}')
		with open(self._dbFile, 'r') as dbFile:
			self._loaded = json.loads(dbFile.read())
		
	def insert(self, __jsonData: dict):
		with self._thread_lock:
			self._loaded["minidb"].update(__jsonData)
			with open(self._dbFile, 'w') as dbFile:
				dbFile.write(json.dumps(self._loaded))
			
	def every(self) -> dict:
		with self._thread_lock:
			dictionary = dict()
			for docs in self._loaded["minidb"].items():
				dictionary[docs[0]] = docs[1]
			return dictionary
		
	def discard(self, __key=None):
		with self._thread_lock:
			if not __key in self._loaded["minidb"]:
				return 
			self._loaded["minidb"].pop(__key)
			with open(self._dbFile, 'w') as dbFile:
				dbFile.write(json.dumps(self._loaded))
	
	def update(self, __key: str, __jsonData: dict):
		with self._thread_lock:
			if not __key in self._loaded["minidb"]:
				return 
			for docs in self._loaded["minidb"][__key]:
				for doc in __jsonData:
					if docs == doc:
						self._loaded["minidb"][__key][docs] = __jsonData.get(doc)
			with open(self._dbFile, 'w') as dbFile:
				dbFile.write(json.dumps(self._loaded))
			
	def reset(self):
		with self._thread_lock:
			self._loaded["minidb"].clear()
			with open(self._dbFile, 'w') as dbFile:
				dbFile.write(json.dumps(self._loaded))
			
miniDB = MiniDatabase