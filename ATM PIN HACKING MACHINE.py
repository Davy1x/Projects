#Atm Hack
import time as tm
from tqdm import tqdm as load
from colorama import Fore as fo, Style
import random as ran


def load_anime():
	for zzz in load(range(100)):
		tm.sleep(0.02)

balance = 0

def atm_pin():
	return 8888
	
def check_balance():
	print(fo.GREEN+f"Your balance: ${balance:,}"+Style.RESET_ALL)


def deposite():
	global balance
	depo = int(input("Enter amount to deposite:  "))
	if depo > 1000:
		print(fo.RED+f"error:<{depo} is greater than 1000>"+Style.RESET_ALL)
	elif depo < 0:
		print(fo.RED+f"error:<{depo} is not valid>"+Style.RESET_ALL)
	else:
		print(fo.GREEN+"Deposite success"+Style.RESET_ALL)
		balance += depo
		return balance
		
		
def withdraw():
		global balance
		draw = int(input("Enter amount to withdraw: "))
		if draw > balance:
			print(fo.RED+"Insufficent funds"+Style.RESET_ALL)
		elif draw < 1:
			print(fo.RED+f"error:<{draw} is not valid>"+Style.RESET_ALL)
		else:
			print(fo.GREEN+"Withdraw success"+Style.RESET_ALL)
			balance -= draw
			return balance
			
def exit_msg():
	msgs = ["Bye", "Have a nice day", "See you next time", "Great banking session"]
	node = ran.choice(msgs)
	print(fo.GREEN+f"{node}"+Style.RESET_ALL)
	
def page():
	load_anime()
	print()
	print("_Welcome to the Pybank_")
	while True:
		print("1. Check Balance\n2. Deposite\n3. Withdraw\n4. Exit")
		enter1 = int(input("Enter choice: "))
		if enter1 == 1:
			check_balance()
		elif enter1 == 2:
			deposite()
		elif enter1 == 3:
			withdraw()
		elif enter1 == 4:
			exit_msg()
			break
		else:
			print(fo.RED+"Invalid choice!"+Style.RESET_ALL)
		load_anime()
		print()

main = int(input("__WELCOME__\nEnter atm pin: "))
if main == atm_pin():
	page()
elif main != atm_pin():
			print(fo.RED+"Incorrect pin!"+Style.RESET_ALL)
			enter2 = input(fo.RED+"Do you wish to hack the atm pin: "+Style.RESET_ALL)
			if enter2.lower() == "yes":
				print(fo.RED+"_hacking_"+Style.RESET_ALL)
				load_anime()
				x = " "*5
				for hack in range(1000,10001):
					tm.sleep(0.001)
					print(fo.RED+f"{x}{hack}{x}"*4+Style.RESET_ALL)
					if hack == atm_pin():
						print(fo.GREEN+"_SYSTEM UNLOCKED_"*3+Style.RESET_ALL)
						tm.sleep(1)
						page()
			else:
				print("...!")
