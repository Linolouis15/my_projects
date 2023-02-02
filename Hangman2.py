import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
  _    _                        __  __               
 | |  | |                      |  \/  |              
 | |__| |  __ _  _ __    __ _  | \  / |  __ _  _ __  
 |  __  | / _` || '_ \  / _` | | |\/| | / _` || '_ \ 
 | |  | || (_| || | | || (_| | | |  | || (_| || | | |
 |_|  |_| \__,_||_| |_| \__, | |_|  |_| \__,_||_| |_|
                         __/ |                       
                        |___/                        
''')
fruit=["app","grape","jackfruit"]
choosen_word=random.choice(fruit) # choosing random word from list
display=[] #Creating a empty list
lives=6 #no of lives set as 6
for word in choosen_word:   # for loop for adding "_" to list for each letter in choosen word
    display.append("_")
print(display)
end_of_game=False # setting end of game as FALSE
while not end_of_game:
    guess=input("enter your guess letter : ")# whiel loop for no of iterations until condotion becomes true
    for i in range(len(choosen_word)):
        if guess==choosen_word[i]:
            display[i]=guess #replacing the character in display list
    if guess not in choosen_word:
        lives=lives-1 #reducing lives by one for each wrong entry
        print(stages[lives])
        if lives == 0:
            print("YOU LOSE")


    print(display)