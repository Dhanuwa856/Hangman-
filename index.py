import random
import string
from words import country_names 


def get_word(country_names):
  word = random.choice(country_names)
  while '-' in word or '' in word:
    word = random.choice(country_names)
    return word.upper()
  
  
def hangman():
  word = get_word(country_names)
  word_letters = set(word) # Letter in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # what the user guessed 
  
  
  lives = 6 # <--- Change the number of instances as you wish
  
  
  
  # getting user input
  while len(word_letters) > 0 and lives > 0:
    
    print('You have ',lives,'left and You have used these letters:',' '.join(used_letters))
  
  
  
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word: ",''.join(word_list))
    
    user_letter = input('Guess a letter: ').upper()
    
    
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)  
      else:
        lives = lives - 1
        print('Letter is not word!')
        
    elif user_letter in used_letters:
      print('You have already used that character. please try again!')    
    else:
      print('Invalid character. please try again!')
      
      
  if lives == 0:
    print('You died, sorry. the word',word)
  else:
    print('You guessed the word ',word,' !!')    
    
hangman()    
