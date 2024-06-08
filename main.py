# Answer check function
def check_guess(guess, answer):
    global score, live
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            score = score + 1
            live = live
            print(' Correct Answer')
            # Print score and live
            print(f' Your Score: {str(score)}, ', 'Your Lives:', 'X ' * live)
            still_guessing = False
        else:
            if attempt < 2:
                guess = input(' Wrong answer. Try again. ')
            attempt = attempt + 1
            live = live - 1
    if attempt == 3:
        print(f' Correct answer is {answer}. ')
        print(f' Your Score: {str(score)}, ', 'Your Lives:', 'X ' * live)

# Creating default variables
score = 0
live = 10

# Starting the game with message
print(' Answer by providing correct answer')

# Ask question
guess1 = input(' Which bear live at the North Pole? ')
check_guess(guess1, 'polar bear')

guess2 = input(' Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')

guess3 = input(' Which is the largest animal? ')
check_guess(guess3, 'blue whale')

