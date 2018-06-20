def hangman():
    word = "caat"
    wrong_guesses = 0
    stages = ["", "______  ", "||  ","|   0", "|  /|\  ","|  / \  ","|"]
    letters_left = list(word)
    score_board = [ '__' ]*len(word)
    win = False
    print("Welcome to hangman")
    
    while (wrong_guesses < len(stages)-1):
        print('\n')
        guess = input("Guess a letter: ")
        if guess in letters_left:
            character_index = letters_left.index(guess)
            score_board[character_index] = guess
            letters_left[character_index] = '$'
        else:
            wrong_guesses += 1
        print("".join(score_board))
        print("\n".join(stages[0 : wrong_guesses+1]))
        if '__' not in score_board:
            print('You win! The Word Was: ')
            print("".join(score_board))
            win = True
            break
    if not(win):
        print("You Lose friend...") 
hangman()