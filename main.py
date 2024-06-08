import random
import time

# Answer check and score update function
def check_guess(guess, answer, attempts, hints_used):
    global score, live
    
    if guess.lower() == answer.lower():
        points = (3 - attempts) - hints_used
        # Ensure player get at least 1 point for a correct answer
        score += max(points, 1)
            
        print(' Correct Answer')
            
        # Print score and live
        print(f' Your Score: {score}, Your Lives: {'X ' * live} ')
        return True
        
    else:
        live -= 1

        if live > 0:
            print(f' Wrong answer. Your lives:{'X ' * live} ')
        return False

# Function to ask a random question
def ask_question(questions):
    global live, attempts, hints_used
    index = random.randrange(len(questions))
    
    # Remove the selected question from the list
    question, answer = questions.pop(index)
    attempts = 0
    hints_used = 0
    
    while attempts < 3 and live > 0:
        guess = input(question + ' ')
        if guess.lower() == 'hint':
            hints_used += 1
            if hints_used == 1:
                print(f' Hint: The answer starts with "{answer[0]}" ')
            elif hints_used == 2:
                print(f' Hint: The answer starts with "{answer[:2]}" ')
            elif hints_used == 3:
                print(f' Hint: The answer is "{answer}" ')
                live -= 1
                break
            continue
        if check_guess(guess, answer, attempts, hints_used):
            break
        attempts += 1
        if attempts == 3:
            print(f' The correct answer is {answer}. ')
            break

# Display Learderboard
def display_leaderboard(learderboad):
    print('\nLeaderboard: ')
    sorted_leaderboard = sorted(leaderboard.items(), key = lambda item: item[1], reverse = True)
    for player, score in sorted_leaderboard:
        print(f' {player}: {score} ')

# Creating Function to run the game
def run_game():
    global score, live, player_name
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
    print(' Answer by providing correct answer. Type "hint" to get a hint (Penalty to ponts). ')

    # Ask player name
    player_name = input(' Enter your name: ').capitalize()

    # Ask question untill lives or questions run out 
    while live > 0 and questions:
        ask_question(questions)

    if live == 0:
        print(f' Game Over!, {player_name}  You\'ve run out of lives. ')

    else:
        print(f' Congratulations! {player_name} You\'ve answered all questions correctly. ')

    # Add player score to the leader board
    leaderboard[player_name] = score

    # Display Leaderboard
    display_leaderboard(leaderboard)

# Creating leaderboard dictionary
leaderboard = {}

# Main game loop
while True:
    run_game()
    choice = input(' Do you want to play again? Yes or No: ').strip().lower()
    if choice != 'yes':
        break
    
print(f' Thank you {player_name} for playing')



