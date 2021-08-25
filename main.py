import random
import time

words = {
    'apple': ['ap___', '___le', 'Bruh u got smol bren'],
    'car': ['_a_', 'Rhymes with bar', '__r']
}

while True:
    game_over = False
    hint_list_index = 0
    guesses = 3
    hints_remaining = 3
    score = 5
    selected_word = random.choice(list(words.keys()))
    while guesses > 0:
        response = input('Try to guess the word or type "hint" for a hint: ')
        if response.lower() == selected_word:
            print(f'Correct! The word was indeed {selected_word}')
            break
        elif response.lower() == 'hint':
            if hints_remaining <= 0:
                print('Sorry, no hints available!')
            else:
                print(words[selected_word][hint_list_index])
                hint_list_index += 1
                score -= 1
                hints_remaining -= 1
        else:
            print('Wrong! ', end='')
            score -= 1
    else:
        game_over = True
    if game_over is True:
        print('Game over and you lost!')
        end_response = input('Continue?(y/n) --> ')
        if end_response == 'y' or end_response == 'yes':
            continue
        elif end_response == 'n' or end_response == 'no':
            print('Good Game! Quitting in 2 seconds ...')
            time.sleep(2)
            break
        else:
            print('Invalid Answer!')
    else:
        print(f'Game over and you won, Congrats!\nYour score --> {score}')
        win_response = input('Continue?(y/n) --> ')
        if win_response == 'y' or win_response == 'yes':
            continue
        elif win_response == 'n' or win_response == 'no':
            print('Good Game! Quitting in 2 seconds ...')
            time.sleep(2)
            break
        else:
            print('Invalid Answer!')
