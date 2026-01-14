#Rock Paper Scissors
import time
import sys
import random as ran

def loading_animation(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        progress = (time.time() - start_time) / duration
        bar_length = 20
        filled_length = int(round(bar_length * progress))
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        sys.stdout.write('\rLoading game: |%s| %d%%' % (bar, int(round(progress * 102))))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')
    
def computer():
	choices = ["Rock","Paper","Scissors"]
	return ran.choice(choices)

loading_animation(2)
a = " "*7
b = "="*21
print()
print(f"{a}Game:\n{b}\nRock, Paper, Scissors\n")
	
while True:
	loading_animation(1)
	print("Enter a digit:\n1.(Rock)\n2.(Paper)\n3.(Scissors)")
	human = int(input("Enter choice: "))
	if human == 1:
		print(f"You selected ({human}.Rock)\n\nThe computer selected ({computer()})\n")
	elif human == 2:
		print(f"You selected ({human}.Paper)\n\nThe computer selected ({computer()})\n")
	elif human == 3:
		print(f"You selected ({human}.Scissors)\n\nThe computer selected ({computer()})\n")
	else:
		print("invalid response, Try again!")
		print()
		loading_animation(2)
		print()
		continue
		