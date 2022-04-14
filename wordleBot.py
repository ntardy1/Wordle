# Clearing the screen for aesthetic purposes
import os
os.system("cls")

print("Welcome to the Wordle Bot!")
print("To use, make a guess and then enter the corresponding results")
print("Grey square = 0, Yellow square = 1, Green square = 2")

smallWordsFile = open(r"path-to-file", "r")
largeWordsFile = open(r"path-to-file", "r")

smallWordsList = smallWordsFile.readlines()
largeWordsList = largeWordsFile.readlines()

possibleWordsList = smallWordsList
i = 0

smallWordsFile.close()
largeWordsFile.close()

for elem in smallWordsList:
  for letter in elem:
    if (letter == '\n'):
      smallWordsList[smallWordsList.index(elem)] = elem[0:elem.index(letter)]

for elem in largeWordsList:
  for letter in elem:
    if (letter == '\n'):
      largeWordsList[largeWordsList.index(elem)] = elem[0:elem.index(letter)]

# Loop that goes through every attempt (6) at the game
#for elem in range(len(smallWordsList[0])):
while True:
  # Input for the word guess
  wordGuess = str(input("Enter the guess: "))
  # Converting the word guess to all captial to match it with the list of allowed guesses
  wordGuess = wordGuess.upper()
  # Input for the hints given by the actual wordle game
  givenHints = str(input("Enter the hints: "))
  # Checking if the player got the word correct (for celebratory reasons)
  if (givenHints == "22222"):
    print("Congratulations!")
    break
  # Checking to make sure the input is a legit word
  if (any(wordGuess == word for word in largeWordsList)):
    # Loop that goes through the given hints, checks for zeros, and removes any words with that letter
    for index in range(len(givenHints)):
      # If the letter is in the word in that spot
      if (givenHints[index] == "2"):
        # i = 0 to start (while loop because removing from possibleWordsList also removes from smallWordsList)
        while (i <= len(smallWordsList)):
          # i was somehow becoming == to len(smallWordsList), which screwed up letters other than first
          # This seems to correct that
          if (i == len(smallWordsList)):
            i = 0
            break
          if (smallWordsList[i][index] != wordGuess[index]):
            possibleWordsList.remove(smallWordsList[i])
            i = 0
          else:
            i += 1
      # If the letter isn't in the word
      elif (givenHints[index] == "0"):
        # i = 0 to start (while loop because removing from possibleWordsList also removes from smallWordsList)
        while (i <= len(smallWordsList)):
          # i was somehow becoming == to len(smallWordsList), which screwed up letters other than first
          # This seems to correct that
          if (i == len(smallWordsList)):
            i = 0
            break
          if all(possibleWordsList[i][j] != wordGuess[index] for j in range(len(smallWordsList[i]))):
            i += 1
          elif (any(possibleWordsList[i][j] == wordGuess[index] for j in range(len(smallWordsList[i])))):
              possibleWordsList.remove(smallWordsList[i])
              i = 0
      elif (givenHints[index] == "1"):
        # i = 0 to start (while loop because removing from possibleWordsList also removes from smallWordsList)
        while (i <= len(smallWordsList)):
          # i was somehow becoming == to len(smallWordsList), which screwed up letters other than first
          # This seems to correct that
          if (i == len(smallWordsList)):
            i = 0
            break
          if (all(smallWordsList[i][j] != wordGuess[index] for j in range(len(smallWordsList[i])))):
            possibleWordsList.remove(smallWordsList[i])
            i = 0
          else:
            i += 1
    print(possibleWordsList)
  else:
    print("Invalid word")
