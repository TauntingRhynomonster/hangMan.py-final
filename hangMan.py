# Ryan Bierman
# 10-21-19
# Period 6

myWord = "ryan"
myList = list(myWord)
misses = 0
secret = []
# Hangman Picture
hangman = [''' pic 1 ''', ''' pic 2 ''', ''' pic 3 ''', ''' pic 4 ''', ''' pic 5 ''', ''' pic 6 ''', ''' pic 7 ''']

print("0=-- Welcome to Hangman --=0")
for s in myList:
		secret.append("_")

	

print(secret)
count = 0
choice = input("what word am I thinking of? ")
if choice == "ryan":
	print("Nice Guess, you are correct")
else:
	print("Not the word that I'm thinking of")

while True:
	while misses < 7:
		print(hangman[misses])
		print(secret)
		guess = input("Pick a letter: ")
		if guess in myList:
			print("That letter is in the secret word")
			secret[count] = choice
		else:
			print("That letter is not in the word")
			misses = misses + 1




	