#SaanviTatipalli
#1/21/22
#Mastermind
import random
def guessmaker ():
  guess.append(int(input("Type your guess for the first digit of the code: ")))
  guess.append(int(input("Type your guess for the second digit of the code: ")))
  guess.append(int(input("Type your guess for the third digit of the code: ")))
  guess.append(int(input("Type your guess for the fourth digit of the code: ")))
  print (guess)
#guessmaker is defined and is reffered to for user input for four digit guess
def guesschecker ():
  if guess == code:
    print ("You got the code right!")
    return True
  if code[0] == guess[0]:
    print ("You got the first digit right!")
  if code[1] == guess[1]:
    print ("You got the second digit right!")
  if code[2] == guess[2]:
    print ("You got the third digit right!")
  if code[3] == guess[3]:
    print ("You got the last digit right!")
  if guess != code:
    print ("You got the code wrong!")
  return False
#guesschecker verifies if the guess equals the secret code and if not, which parts are equal
print ("Let's play the game Mastermind. I will generate a random code with 4 digits (1-9) and you must try to break the code!")
name = input("What's your name code breaker? ")
code = []
for i in range (4):
  code.append(int(random.randint(1,9)))
#a random 4-digit code is generated
tries = 0
guess = []
while guess != code:
  guess = []
  guessmaker ()
  guesschecker ()
  tries = tries + 1
#the player must keep guessing until they get it correct.
print ("You took " + str(tries) + " tries! Congrats!")