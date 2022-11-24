from replit import clear
from player import Player
import random
from word_bank import easy, medium, hard
from hangman_art import stages, logo


round1 = True
while round1:
  print(logo)
  print("Welcome to the Hangman Game!")

  player1 = Player(input("First Player, What is your name? "))

  chosen_level = input("Which level of difficulty would you like? Type easy, medium, or hard:\n")

  if chosen_level == "easy":
    chosen_word = random.choice(easy)
  elif chosen_level == "medium":
    chosen_word = random.choice(medium)
  else:
    chosen_word = random.choice(hard)


  def play_round():
    '''while the game is still going, the player can guess up until there are 0 lives left. If they have already guessed a letter, the game will let them know that they have already guessed it.'''
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    display = []
    for _ in range(word_length):
        display += "_"
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        clear()
      
        if guess in display:
            print(f"You've already guessed {guess}")
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
              #replace space with the correct letter guess
              display[position] = letter
        #Check if user is wrong.
        if guess not in chosen_word:
            print(f"you guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The secret word is {chosen_word}")
    
        print(f"{' '.join(display)}")
    
        #Check if user has got all letters. aka if there are no more empty spaces
        if "_" not in display:
            end_of_game = True
            print(f"Congratulations! You win! The secret word is {chosen_word}")
        print(stages[lives]) 

  play_round()
  round1 = False

# round 2
round2 = True
while round2:
  print(logo)
  player2 = Player(input("Second Player, What is your name? "))
  chosen_level = input("Which level of difficulty would you like? Type easy, medium, or hard:\n")
  
  if chosen_level == "easy":
    chosen_word = random.choice(easy)
  elif chosen_level == "medium":
    chosen_word = random.choice(medium)
  else:
    chosen_word = random.choice(hard)
  play_round()
  end_of_game = True
  round2 = False 



if __name__ == "__main__":
  play_round()
