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
            

# Creating Function to run the game
def run_game():
    global score, live, player_name, elapsed_time
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
    ('Humans can distinguish between over a trillion different smells. True or False?', 'true'),
    ('What is 15 - 7?', '8'),
    ('What is 9 * 3?', '27'),
    ('What is the square root of 81?', '9'),
    ('What is 50 / 5?', '10'),
    ('What is 8 + 6?', '14'),
    ('What is the capital of Germany?', 'berlin'),
    ('What is the capital of Spain?', 'madrid'),
    ('What is 14 * 2?', '28'),
    ('What is 49 / 7?', '7'),
    ('What is 100 - 25?', '75'),
    ('Who wrote "Pride and Prejudice"?', 'austen'),
    ('Who discovered America?', 'columbus'),
    ('What is 7 + 8?', '15'),
    ('What is 12 - 5?', '7'),
    ('What is 6 * 6?', '36'),
    ('What is 24 / 4?', '6'),
    ('What is the capital of Russia?', 'moscow'),
    ('What is the capital of China?', 'beijing'),
    ('Who painted "Starry Night"?', 'van gogh'),
    ('Who wrote "To Kill a Mockingbird"?', 'lee'),
    ('What is the capital of Brazil?', 'brasilia'),
    ('What is 11 + 13?', '24'),
    ('What is 30 - 10?', '20'),
    ('What is 5 * 5?', '25'),
    ('What is 18 / 3?', '6'),
    ('What is the chemical symbol for water?', 'h2o'),
    ('What is the capital of India?', 'new delhi'),
    ('What is 9 + 10?', '19'),
    ('What is 22 - 9?', '13'),
    ('What is 7 * 4?', '28'),
    ('What is 40 / 8?', '5'),
    ('What is the capital of Egypt?', 'cairo'),
    ('What is the capital of Mexico?', 'mexico city'),
    ('What is the chemical symbol for oxygen?', 'o'),
    ('What is the capital of Greece?', 'athens'),
    ('What is 4 + 5?', '9'),
    ('What is 20 - 5?', '15'),
    ('What is 8 * 3?', '24'),
    ('What is 35 / 7?', '5'),
    ('What is the capital of South Korea?', 'seoul'),
    ('What is the capital of Argentina?', 'buenos aires'),
    ('What is 6 + 7?', '13'),
    ('What is 15 - 6?', '9'),
    ('What is 10 * 3?', '30'),
    ('What is 45 / 5?', '9'),
    ('What is the capital of Australia?', 'canberra'),
    ('What is the capital of Turkey?', 'ankara'),
    ('What is 5 + 6?', '11'),
    ('What is 21 - 7?', '14'),
    ('What is 4 * 7?', '28'),
    ('What is 36 / 6?', '6'),
    ('What is the chemical symbol for sodium?', 'na'),
    ('What is the capital of Norway?', 'oslo'),
    ('What is 3 + 8?', '11'),
    ('What is 25 - 15?', '10'),
    ('What is 7 * 7?', '49'),
    ('What is 60 / 12?', '5'),
    ('What is the capital of Sweden?', 'stockholm'),
    ('What is the capital of Portugal?', 'lisbon'),
    ('What is 12 + 8?', '20'),
    ('What is 27 - 9?', '18'),
    ('What is 3 * 10?', '30'),
    ('What is 48 / 8?', '6'),
    ('What is the powerhouse of the cell?', 'mitochondria'),
    ('What is the basic unit of life?', 'cell'),
    ('What is the process by which plants make their food using sunlight?', 'photosynthesis'),
    ('What type of blood cells are responsible for fighting infections?', 'white blood cells'),
    ('What is the genetic material in cells?', 'DNA'),
    ('What is the largest organ in the human body?', 'skin'),
    ('What organ is responsible for pumping blood throughout the body?', 'heart'),
    ('What is the process by which cells divide to produce identical daughter cells?', 'mitosis'),
    ('What is the name of the process by which a single parent organism reproduces by itself?', 'asexual reproduction'),
    ('What type of cell lacks a nucleus?', 'prokaryotic cell'),
    ('Which macromolecule is primarily responsible for storing genetic information?', 'nucleic acids'),
    ('What is the name of the pigment that gives plants their green color?', 'chlorophyll'),
    ('What is the name of the process by which water moves across a semipermeable membrane?', 'osmosis'),
    ('What is the main component of the plant cell wall?', 'cellulose'),
    ('What is the term for the variety of different species in an ecosystem?', 'biodiversity'),
    ('What organ in the human body is primarily responsible for detoxifying chemicals?', 'liver'),
    ('What is the name of the protein that carries oxygen in the blood?', 'hemoglobin'),
    ('What is the term for a change in the DNA sequence?', 'mutation'),
    ('What organelle is responsible for protein synthesis in the cell?', 'ribosome'),
    ('What type of organism produces its own food from inorganic substances?', 'autotroph'),
    ('What is the process by which organisms with favorable traits survive and reproduce?', 'natural selection'),
    ('What is the name of the structure that protects the ends of chromosomes?', 'telomere'),
    ('What is the primary function of the roots of a plant?', 'absorption of water and nutrients'),
    ('What is the name of the process by which a sperm cell unites with an egg cell?', 'fertilization'),
    ('What part of the brain is responsible for regulating heart rate and breathing?', 'medulla oblongata'),
    ('What is the name of the molecule that provides energy for cellular processes?', 'ATP'),
    ('What is the main function of the large intestine in the digestive system?', 'absorption of water'),
    ('What is the name of the process by which plants lose water through their leaves?', 'transpiration'),
    ('What is the term for a group of organisms of the same species living in a specific area?', 'population'),
    ('What is the primary pigment found in the human retina responsible for detecting light?', 'rhodopsin'),
    ('What is the function of the Golgi apparatus in the cell?', 'modifying, sorting, and packaging proteins'),
    ('What is the name of the process by which bacteria reproduce asexually?', 'binary fission'),
    ('What is the name of the hormone that regulates blood sugar levels?', 'insulin'),
    ('What is the term for the symbiotic relationship where both organisms benefit?', 'mutualism'),
    ('What is the name of the process by which genetic information is copied from DNA to RNA?', 'transcription'),
    ('What is the primary function of red blood cells?', 'transporting oxygen'),
    ('What is the term for the movement of molecules from an area of higher concentration to an area of lower concentration?', 'diffusion'),
    ('What is the main function of the small intestine in the digestive system?', 'absorption of nutrients'),
    ('What is the name of the process by which plants convert carbon dioxide into organic compounds using the energy from sunlight?', 'carbon fixation'),
    ('What is the term for an organism that feeds on dead organic matter?', 'decomposer'),
    ('What is the main function of chloroplasts in plant cells?', 'photosynthesis'),
    ('What is the name of the process by which cells obtain energy from glucose?', 'cellular respiration'),
    ('What is the term for the study of how traits are passed from parents to offspring?', 'genetics'),
    ('What is the function of the mitochondria in the cell?', 'producing energy'),
    ('What is the name of the process by which cells engulf large particles?', 'phagocytosis'),
    ('What is the term for the range of physical and biological conditions in which an organism lives and the way it uses those conditions?', 'niche'),
    ('What is the main function of the nervous system?', 'transmitting signals between different parts of the body'),
    ('What is the term for the process by which an organism changes form during its life cycle?', 'metamorphosis'),
    ('What is the name of the cell structure that controls the movement of substances in and out of the cell?', 'cell membrane'),
    ('What is the main function of the ribosomes in the cell?', 'protein synthesis')
]

    # Ask player name
    player_name = input(' Enter your name: ').capitalize()
    
    # Starting the game with message
    print(f' Hello {player_name} Please provide answer by entering correct answer. Type "hint" to get a hint (Penalty to ponts). ')
    
    # Start time
    start_time = time.time()
    
    # Ask question untill lives or questions run out 
    while live > 0 and questions:
        ask_question(questions)
    
    # Ending time
    end_time = time.time()
    elapsed_time = int(end_time - start_time)

    if live == 0:
        print(f' Game Over!, {player_name}  You\'ve run out of lives. ')
    else:
        print(f' Congratulations! {player_name} You\'ve answered all questions correctly. ')


# Main game loop
while True:
    run_game()
    choice = input(' Do you want to play again? Yes or No: ').strip().lower()
    if choice != 'yes':
        break
    
print(f' Thank you {player_name} for playing. You\'ve spend {elapsed_time} seconds in playing and score {score} points. ')



