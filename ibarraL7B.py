#Alejandra Ibarra 
#Lab 7B part 1/2 

def play_game():
    my_num = 25
    guess = int(input("Guess what my number is. "))
    result = my_num - guess  

    while(result >= -2 and result <= 2 ): 
        if result == 0:
            break
        guess = int(input("That was close try again :) "))
        result = my_num - guess 

    if result == 0:
        print("Good job, you correctly guessed my number. ")
    elif result < 0: 
        print("Sorry that is incorrect, your guess was too high. My number was 25. ")
    else:
        print("Sorry that is incorrect, your guess was too low. My number was 25. ")

answer = input("Would you like to play my guessing game. ")
while (answer == "yes"):
    play_game()
    answer = input("Would you like to play my guessing game. ")

