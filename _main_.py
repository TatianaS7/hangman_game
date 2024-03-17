import random

categoryKey = {
   'categories': ['Colors', 'Fruits', 'Car Models', 'Animals', 'Instruments'],
   'values': {
       'Colors': [ 'Blue', 'Red', 'Green', 'Orange', 'Purple', 'Yellow', 'Black', 'White', 'Brown' ],
       'Fruits': ['Apples', 'Strawberries', 'Mango', 'Kiwi', 'Grapefruit', 'Banana', 'Pineapple', 'Blood Orange', 'Blueberries', 'Clementines', 'Watermelon', 'Canteloupe', 'Honeydew'],
       'Car Models': ['Chevrolet', 'Toyota', 'Ford', 'Honda', 'Hyundai', 'Acura', 'Audi', 'BMW', 'Cadillac', 'Ferrari', 'Dodge', 'Tesla', 'Volkswagen', 'Rolls Royce', 'Porsche'],
       'Animals': ['Monkey', 'Salamander', 'Panda', 'Giraffe', 'Lion', 'Grizzly Bear', 'Rattlesnake', 'Panther', 'Leopard', 'Cheetah', 'Pelican', 'Iguana', 'Meerkat'],
       'Instruments': ['Saxaphone', 'Flute', 'Piano', 'Trombone', 'Violin', 'Guitar', 'Clarinet', 'Trumpet', 'Drums', 'Cello', 'Bass Guitar']
   }
}

categoryList = categoryKey['categories']
valuesList = categoryKey['values']


def main():
    print('Game Categories:')
    for category in categoryList: # iterates through categries and prints for users to pick
        print('-', category)

    selectedCategory = input('Pick One:\n')
    randomValue = random.choice(valuesList[selectedCategory]).lower()  # random.choice module randomly picks a value from user specified category 
    
    # convert to lowercase for guesses because all text is capitalized in dictionary
    
    letterCount = 0
    for i in range(len(randomValue)): # iterates through length of word to count letters
        if i == ' ': # ignores spaces in words for letter count
            letterCount += 0
        else:
            letterCount += 1

    underscores = '_ ' * letterCount # creates a string with the same amount of underscores as letters in the word

    wrongGuesses = [] # container for incorrectly guessed letters

    print(letterCount, 'Letter Word')
    print(underscores)
    # print(randomValue) #Remove after testing

    while True: # the default condition is true, so the while loop runs until it reaches a break statement 
        letterGuess = input('Guess a letter: \n').lower() # converts letter to lowercase since word is lowercase 

        if letterGuess in randomValue: # if letter is present in the word
            print('Correct!')

            for i in range(len(randomValue)): # loops through length of word to access letters
                if randomValue[i] == letterGuess: # if current letter is equal to guessed letter
                    underscores = underscores[:2 * i] + letterGuess + underscores[2 * i + 1:] # underscore string is updated to display correctly guessed letters 

            print(underscores)

            if '_' not in underscores: # if all letters are guessed (no underscores left), you won the game
                print('You guessed the word:', randomValue)
                playAgain = input('Play Again?(y/n)\n')
                if playAgain.lower() == 'y':
                    main()
                elif playAgain.lower() == 'n':
                    break

        else: # if letter is NOT present in the word, youre prompted to guess again
            wrongGuesses.append(letterGuess) # adds wrong letter guess to list 
            print('Wrong! Try again\n')
            print('Your Guesses', wrongGuesses)
            print(underscores)

main() # calls function to be run