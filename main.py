import random

# Answer chec function
def check_guess(guess, answer):
    global score, live
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            score += 1
            
            print(' Correct Answer')
            
            # Print score and live
            print(f' Your Score: {score}, Your Lives: {'X ' * live} ')
            still_guessing = False
        
        else:
            if attempt < 2:
                guess = input(' Wrong answer. Try again. ')
            attempt += 1
            live -= 1
            
            if live == 0:
                break

    if attempt == 3 and still_guessing:
        print(f' Correct answer is {answer}. ')
        print(f' Your Score: {score}, Your Lives: {'X ' * live }')

# Function to ask a random question
def ask_question(questions):
    index = random.randrange(len(questions))
    
    # Remove the selected question from the list
    question, answer = questions.pop(index)
    guess = input(question + ' ')
    check_guess(guess, answer)


# Creating default variables
score = 0
live = 10

# List of question
questions = [
        (' Which bear lives at the North Pole? ', 'polar bear'),
        (' Which is the fastest land Animal? ', 'cheetah'),
        (' Which is the largest Animal ', 'blue whale'),
        (' Which one of these is a fish?\n A) Whale \n B) Dolphin \n C) Shark \n D) Squid \n Type A, B, C or D ', 'c')
]

# Starting the game with message
print(' Answer by providing correct answer')

# Ask question untill lives or questions run out 
while live > 0 and questions:
    ask_question(questions)

if live == 0:
    print( ' Game Over!!! You\'ve run out of lives. ')

else:
    print(' Congratulations!!! You\'ve answered all questions correctly. ')
