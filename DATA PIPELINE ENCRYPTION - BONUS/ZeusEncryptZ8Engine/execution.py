from ZeusEncryptZ8Engine.modules.zeus_z8engine import ZeusZ8Engine
import time
metadata, encryption_key, decryption_key = ZeusZ8Engine.get("metadata"), ZeusZ8Engine.get("encryption_key"), ZeusZ8Engine.get("decryption_key")

class ZeusEncryptZ8Engine:
	def __init__(self, main: dict()) -> None:
		self._data = main["Data"]
		self._decrypt = main["Decrypt"]
		self._encrypt = main["Encrypt"]
		self._allowMetadata = main["AllowMetadata"]
		self._allPackages = main["AllPackages"]
		# self.process()
		
	def process( self ) -> list():	
		Encrypto = { "data": {} }
		decrypting = []; encrypting =[]
		
		if self._encrypt and not self._decrypt:
			for chars in self._data:
				for key, value in encryption_key.items():
					if chars == key:
						encrypting.append(value)
						decrypting.append(chars)	
			if self._allowMetadata: Encrypto["metadata"] = metadata; Encrypto["metadata"]["encryption_time"] = f"{time.ctime()} GMT+0100 (West African Standard Time)"
			if self._allPackages:
				Encrypto["data"]["encrypt"] = str().join(encrypting)
				Encrypto["data"]["decrypt"] = str().join(decrypting)
				return Encrypto
			Encrypto["data"] = str().join(encrypting)
			return Encrypto
			
		elif self._decrypt and not self._encrypt:
			def zeusArr() -> list():
				temp = []
				for chars in range(0, len(self._data), 4):
					temp.append(self._data[chars : chars+4])
				return temp
			for chars in zeusArr():
				for key, value in decryption_key.items():
					if chars == key:
						encrypting.append(chars)
						decrypting.append(value)		
			if self._allowMetadata: Encrypto["metadata"] = metadata; Encrypto["metadata"]["encryption_time"] = f"{time.ctime()} GMT+0100 (West African Standard Time)"
			if self._allPackages:
				Encrypto["data"]["encrypt"] = str().join(encrypting)
				Encrypto["data"]["decrypt"] = str().join(decrypting)
				return Encrypto
			Encrypto["data"] = str().join(decrypting)
			return Encrypto
			
		elif not self._encrypt and not self._decrypt:
			return({ "error": "ERROR: Illegal operation - no method supplied" })
			
		else:
			return({ "error": "ERROR: Can not perform two operations at once" })
			

# Expected Object Format for ZeusEncrypt

# testObj = {
# 	"Data": "This is an instance",
# 	"Decrypt": False,
# 	"Encrypt": True,
# 	"AllowMetadata": False,
# 	"AllPackages": False
# }

Zeus = ZeusEncryptZ8Engine