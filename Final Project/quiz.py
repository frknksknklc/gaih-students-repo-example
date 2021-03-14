import json
import random
import getpass

user = []

def play():
	print("\n==========KNOWLEDGE COMPETITION START==========")
	score = 0
	with open("questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(10):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[ch]
		print(f'\nFINAL SCORE: {score}')
                        



if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========WELCOME TO KNOWLEDGE COMPETITION==========')
		print('-----------------------------------------')
		print('1. KNOWLEDGE COMPETITION')
		print('2. EXIT')
		
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
