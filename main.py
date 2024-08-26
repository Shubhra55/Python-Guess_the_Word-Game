from random_word_generator import pick_random_word
# Importing the words from random_word-generator.py 


def change_current_word_state(selected_word,input_char,current_word_state):
    # If the input character is there in the selected word, place it in its place and return the new state or return the same word state
    modified_word_state=""
    
    for i in range(len(selected_word)):
        
        if current_word_state[i]=="_" and selected_word[i]==input_char:
            
            modified_word_state+=selected_word[i]
        else:
            modified_word_state+=current_word_state[i]
            
    return modified_word_state


def input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining):
    # Checks if the input character is there in selected word then run change_current_word_state or decrease one attempt count
    if input_char in selected_word:
        
        current_word_state = change_current_word_state(selected_word,input_char,current_word_state)
    else:
        attempts_remaining-=1    
        
    return current_word_state,attempts_remaining

def print_current_state(current_word_state,attempts_remaining):
    # It will print current status of the game that is the alphabets guesses so and attempts left
    
    print("Latest Word Position : ", end=" ")
    
    for i in current_word_state:
        print(i, end=" ")
    print("\t Attempts remaining : {}".format(attempts_remaining))
    
def check_game_status(selected_word,current_word_state,attempts_remaining):
    # Checks if the game hsa ended or not and print the concluding lines
    if attempts_remaining<=0:
        print("Sorry, you Lost : (Try Again !)")
        print("The word is : {}".format(selected_word))
        return False
    
    if selected_word==current_word_state:
        print("Congratulations, you Won !")
        return False
    
    return True
            
        
def play_game(attempts=10):
    # It will contain the main logic of the game
    
    current_word_state = ""
    # Show present status
    
    selected_word = pick_random_word()
    # Store value of randomly picked word
    
    for i in selected_word:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i==' ':
            current_word_state += i
        else:
            current_word_state+="_"
            
    attempts_remaining = attempts
    
    print_current_state(current_word_state,attempts)
    
    while True:
        # Loop if game is won by the user and 2nd number of chances are no more
        
        input_char = input("Type any Alphabet : ")
        print("")
        
        current_word_state,attempts_remaining = input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining)
        
        print_current_state(current_word_state,attempts_remaining)
        
        game_end_checker = check_game_status(selected_word,current_word_state,attempts_remaining)
        
        if(game_end_checker==False):
            break


if __name__ == "__main__" :
    # Introduction  of the game

    print("\nRules for the game :")
    print("\n1) You will be receiving a random word to guess with vowels already placed.")
    print("2) You will have only 10 attempts to guess the word")
    print("3) Don't guess the same letter again and again")
    print("\nAll the Best! Enjoy your game.\n")
    play_game()