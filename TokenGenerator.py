tokens = []
path = '/storage/emulated/0/programs/tokens.json'

import random

def tok():
	ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890#$&!?"
	token = ''.join(random.choice(ref) for x in range(12))
	return token

for z in range(100):
	tokens.append(tok())
	
for y in tokens:
	with open(path, 'a') as file:
		ton = f' "@avt.{y}",\n '
		file.write(ton)