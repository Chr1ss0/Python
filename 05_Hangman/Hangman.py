import random
import word_list
import ascii_art

chosen_word = random.choice(word_list.words)
alrady_guessed = []
display = ['_' for _ in chosen_word]
lives = 6
print(ascii_art.logo)


while '_' in display and lives > 0:
    guesed_letter = input('Guess a letter: ').lower()
    if guesed_letter in alrady_guessed:
        print(f'You alreadey guessed the Letter {guesed_letter}')
    elif guesed_letter in chosen_word:
        alrady_guessed.append(guesed_letter)
        for position in range(len(chosen_word)):
            if guesed_letter == chosen_word[position]:
                display[position] = guesed_letter
    else:
        alrady_guessed.append(guesed_letter)
        print(f'The Letter {guesed_letter} is not in the Word')
        lives -= 1
        
    print(f'{ascii_art.stages[lives]}\n{" ".join(display)} ')
    
    if not '_' in display:
        print('Player Won!')
    elif lives <= 0:
        print(f'Player hanged! The word was {chosen_word}')
