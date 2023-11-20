
#3.1) Function to generate 2 random numbers
import random
def generate_numbers():
    num1 =random.randint(1, 10)
    num2 =random.randint(1, 10)
    return num1, num2

#3.2)Function to prompt player for answer
def prompt_for_answer(num1 ,num2):
    print("What is the product of",num1,"and",num2,"?")
    answer= int(input(f"what is {num1} x {num2}? "))
    return answer

#3.3)Function to check if answer is correct
def check_answer(num1, num2, answer):
    if num1*num2 == answer:
        print("Correct")
        return True
    else:
        print("incorrect")
        return False

#3.4)Function to start the game
def play_game():
    print("Welcome to the multiplication game!")
    correct_answers = 0
    playing = True
    while playing:
        num1, num2 = generate_numbers()
        answer = prompt_for_answer(num1, num2)
        if check_answer(num1, num2, answer):
            correct_answers += 1
        else:
            playing = False
        continue_playing = input("Do you want to continue playing? (y/n) ")
        if continue_playing.lower() != "y":
            playing = False
    print(f"Game over! Your score is {correct_answers}.")

#3.5)Call the play_game function to start the game
play_game()
        