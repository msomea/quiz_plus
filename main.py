import random

# Answer chec function
def check_guess(guess, answer):
    global score, live
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            score += 3 -attempt
            
            print(' Correct Answer')
            
            # Print score and live
            print(f' Your Score: {score}, Your Lives: {'X ' * live} ')
            still_guessing = False
        
        else:
            attempt += 1
            live -= 1
            if attempt < 2:
                guess = input(f' Wrong answer. Your lives {'X ' * live} Try again. ')
            
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
    ('Which bear lives at the North Pole?', 'polar bear'),
    ('Which is the fastest land animal?', 'cheetah'),
    ('Which is the largest animal?', 'blue whale'),
    ('Which one of these is a fish?\nA) Whale\nB) Dolphin\nC) Shark\nD) Squid\nType A, B, C or D', 'c'),
    ('What is the capital of France?', 'paris'),
    ('What is 5 + 7?', '12'),
    ('What is the largest planet in our solar system?', 'jupiter'),
    ('Who wrote "Romeo and Juliet"?', 'shakespeare'),
    ('What is the smallest prime number?', '2'),
    ('In which year did the Titanic sink?', '1912'),
    ('What is the chemical symbol for gold?', 'au'),
    ('Who painted the Mona Lisa?', 'da vinci'),
    ('What is the square root of 64?', '8'),
    ('What is the capital of Japan?', 'tokyo'),
    ('What is the boiling point of water at sea level (in Celsius)?', '100'),
    ('Who discovered penicillin?', 'fleming'),
    ('What is the capital of Italy?', 'rome'),
    ('Who is the author of "Harry Potter"?', 'rowling'),
    ('What is the capital of Canada?', 'ottawa'),
    ('What is the largest ocean on Earth?', 'pacific'),
    ('What is the speed of light in vacuum (m/s)?', '299792458'),
    ('Who was the first president of the United States?', 'washington'),
    ('Which planet is known as the Red Planet?', 'mars'),
    ('What is the tallest mountain in the world?', 'everest'),
    ('The sky is blue. True or False?', 'true'),
    ('The capital of Australia is Sydney. True or False?', 'false'),
    ('Light travels faster than sound. True or False?', 'true'),
    ('The Great Wall of China is visible from space. True or False?', 'false'),
    ('Water boils at 90 degrees Celsius at sea level. True or False?', 'false'),
    ('Humans have more than two lungs. True or False?', 'false'),
    ('The earth is flat. True or False?', 'false'),
    ('Mount Everest is in Nepal. True or False?', 'true'),
    ('Honey never spoils. True or False?', 'true'),
    ('Sharks are mammals. True or False?', 'false'),
    ('The atomic number of carbon is 6. True or False?', 'true'),
    ('Venus is the closest planet to the Sun. True or False?', 'false'),
    ('The human body has four lungs. True or False?', 'false'),
    ('There are seven continents on Earth. True or False?', 'true'),
    ('Albert Einstein developed the theory of relativity. True or False?', 'true'),
    ('Bats are blind. True or False?', 'false'),
    ('Goldfish have a memory span of three seconds. True or False?', 'false'),
    ('Humans can distinguish between over a trillion different smells. True or False?', 'true')
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
