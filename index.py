import random

def random_num():
  return random.randint(1000,10000)

def get_num():
	is_num = False
	while is_num is False:
		num = input("Enter a 4-digit whole number: ")
		if num.strip().isdigit():
			if len(num) != 4:
				print("Sorry, that wasn't a positive 4-digit whole number, please try again.")
			else:
				is_num = True
		else:
			print("That's not a positive whole number, please try again.")
	return num

def cow(guess, target):
	num_cows = 0
	numbers = []
	tar_nums = list(target)
	gue_nums = list(guess)
	for i in range(4):
		if tar_nums[i] == gue_nums[i]:
			num_cows += 1
			numbers.append(tar_nums[i])
	return num_cows, numbers

def bull(guess, target):
	num_bulls = 0
	numbers = []
	for num1 in target:
		if num1 in guess:
			num_bulls += 1
			numbers.append(num1)
	return num_bulls, numbers

def give_up(target):
	cont = input("Enter to continue or Press x to give up: ")
	again = ''
	if cont == 'x':
		print('Sorry to see you go, the answer was ', target, " :(\nBetter luck next time!")
		again = input("Do you want to play again? Press 'y' is yes or press anything else to exit: ")
	return again

def play_game(target):
	rounds = 0
	end = False
	while end is False:
		rounds += 1
		number = get_num()
		cows, listc = cow(number, str(target))
		bulls, listb = bull(number, str(target))
		listd = [x for x in listb if x not in listc]
		bulls = bulls - cows
		print(rounds, ': ', cows, ' cows, ', bulls, ' bull')
		# give up option after every 4 rounds
		# again = give_up(target)
		# if again != 'y' or again != 'yes':
		# 	end = True
		# else:
		# 	print("Goodbye.")
		if cows == 4:
			print('Congradulations! You won in only ', rounds, ' round/s!')
			again = input("Do you want to play again? (type n for no or enter to continue) ")
			if again == "n" or again == "no":
				end = True
	

def main():
	welcome = "Welcome to the Bulls and Cows Game!"
	print(welcome)
	print("-" * len(welcome))
	print("In this game, you are trying to guess what the 4-digit number is.\nThen we will tell you how many cows and bulls you got.\nThe number of Cows is how many numbers are in the right place.\nThe number of bulls are how many of the other numbers are in the target.\nGood luck!")
	print("-" * 72)
	target = random_num()
	play_game(target)

main()
