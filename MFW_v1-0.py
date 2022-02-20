# Merlin for Wordle 1.0
# 2022 (C) ChappyPop

import copy
import csv
import string

def getChar():
   while True:
      
      try:
           character = input()
           if len(character) == 1 and character.islower():
              return character
      except:
           print("Please enter a single lower case letter: ")
      print("Please enter a single lower case letter: ")

def getPosition():
   valid = ('1', '2', '3', '4', '5')
   while True:
      print("Please enter a number 1-5: ")
      position = input()
      if len(position) == 1 and position in valid:
         return (int(position)-1)
         
def wordsLeft():
    print("\nNumber of word possibilities remaining:", len(remaining))

def includeLetter(letter):
   global remaining 
   # Use list comprehension to grab words to keep while iterating list
   newList = [word for word in remaining if letter in word]
   remaining = copy.deepcopy(newList);
   wordsLeft()

def pinLetter(letter, position):
    global remaining
    # List comprehension 
    newList = [word for word in remaining if word[position] == letter]
    remaining = copy.deepcopy(newList);
    wordsLeft()
   
def removeLetter(letter):
   global remaining 
   # List comprehension
   newList = [word for word in remaining if letter not in word]
   remaining = copy.deepcopy(newList);
   wordsLeft()
   
def printWords():
    print()
    for word in remaining:
        print(word)
    print()    

def blockLetter(letter, position):
   global remaining 
   
   # List comprehension
   newList = [word for word in remaining if letter not in word[position]]
   remaining = copy.deepcopy(newList);
   wordsLeft()
    
def analysis():
   global remaining
   results      = {}    #wordList of word score pairs
   noDuplicates = {}    #wordlist with no repeated letters
   letterSet    = set() #a set to check for repeated letters
   
   for word in remaining:
      score = 0
      for letter in word:
         score += frequencies[letter]
      
      results[word]= score #put the scores in the wordList
      
   #sort the wordList by score
   results = sorted(results.items(), key=lambda y: y[1], reverse=True)
   
   #print out the top 10 suggestions with scores
   print("The top recommended choices with duplicates:")

   tops = len(results)
   if tops > 10: tops = 10
   for count in range (0,tops):
      item = results[count]
      print(item[0], format(item[1], '.2f'))

   #vesion without duplicates
   print("The top recommended choices WITHOUT duplicate letters:")     
   for item in results:
      letterSet.clear()
      for letter in item[0]:
         letterSet.add(letter)
      if len(letterSet) == 5:
         noDuplicates[item[0]] = item[1]

   #sort the wordList by score
   noDuplicates = sorted(noDuplicates.items(), key=lambda y: y[1], reverse=True)
   tops = len(noDuplicates)
   if tops > 10: tops = 10
   for count in range (0,tops):
      row = noDuplicates[count]
      print(row[0], format(row[1], '.2f'))
       
   print() 

#Globals
wordList  = [] #imported list
remaining   = [] #remaining word list
frequencies = {} #wordList for the frequecy pairs Letter/probability

# Import the word list - downloaded from
# https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
# sort it and make a copy for modification during the game
# split() method divides a string into a list.

print("----- Merlin for Wordle 1.0 -----")
print("----- 2022 (C) ChappyPop    -----\n")

#get the wordList - built with only 5 letter words
with open("fivewords.txt", 'r') as textfile:
   for line in textfile:
       for word in line.split():
          wordList.append(word)

wordList = sorted(wordList)
textfile.close()

remaining = copy.deepcopy(wordList)
print("Imported words in wordList:", len(wordList))

#get the letter frequencies in a csv file 
frequenciesFile = open("frequencies.csv")
with frequenciesFile:
   read=csv.reader(frequenciesFile)
   for row in read:
      #print(row)
      frequencies[row[0]] = float(row[1])     
frequenciesFile.close()

# Menu
choice = 'n'
while choice != 'e':
    print("(a)nalysis")
    print("(b)lock a letter from a position")
    print("(i)include a letter")
    print("(p)in a letter")
    print("(r)emove letter")
    print("(s)how words remaining")
    print("(e)xit")
    choice = getChar()

    if choice == 'a':
        analysis()

    elif choice == 'b':
       print("Letter to block: ")
       block = (getChar())
       print("Position to block", block, ": ")
       blockLetter(block, getPosition())

    elif choice == 'i':
        print("Letter to include: ")
        includeLetter(getChar())

    elif choice == 'p':
        print("Letter to pin: ")
        pinLetter(getChar(), getPosition())

    elif choice[0] == 'r':
        print('Letter to remove: ')
        removeLetter(getChar())

    elif choice[0] == 's':
        printWords()

    print("Please select a letter from the menu below.")
print("\nCome again some time...")
        






    
