# Ryan Bierman
# 10-21-19
# Period 6

myWord = "ryan"
myList = list(myWord)
guessList = list("")
misses = 0
secret = []
# Hangman Picture
hangman = [''' pic 1 ''', ''' pic 2 ''', ''' pic 3 ''', ''' pic 4 ''', ''' pic 5 ''', ''' pic 6 ''', ''' pic 7 ''']

print("0=-- Welcome to Hangman --=0")
for s in myList:
	secret.append("_")


print(secret)

choice = input("what word am I thinking of? ")
if choice == myWord:
	print("Nice Guess, you are correct")
else:
	print("Not the word that I'm thinking of")

while misses < 7:
	print(hangman[misses])
	print(secret)
	guess = input("Pick a letter: ")
	if guess in myList:
		count = 0
		print("That letter is in the secret word")
		for letter in myList:
			if letter == guess:
				secret[count] = guess
			count += 1
	else:
		print("That letter is not in the word")
		misses = misses + 1
	if misses > 7:
		print("GAME OVER")
		break
	if guess == myList:
		print("You WIN!!!")
		break

