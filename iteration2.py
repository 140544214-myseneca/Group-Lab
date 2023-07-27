#!/usr/bin/env python3

"""
Group Project
Student: Parth Patel , Dhruv Patel
Student Number: 140544214 , 164386211
"""
import random

def get_user_choice():
    print("Welcome Games4You RPS!")
    print("Enter your choice: if rock type r for paper type p , or scissors type s")
    user_choice = input()
    while user_choice not in ["r", "p", "s"]:
        print("Invalid choice! Please enter either r,p,s")
        user_choice = input()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    options = ["r", "p", "s"]
    play_again = True

    while play_again:
        computer_choice = random.choice(options)

        user_choice = get_user_choice()
        userc = user_choice
        compc = computer_choice

        if user_choice == "r":
            userc = "rock"
        elif user_choice == "p":
            userc = "paper"
        else:
            userc = "sissors"
            
        if computer_choice == "r":
            compc = "rock"
        elif computer_choice == "p":
            compc = "paper"
        else:
            compc = "sissors"
            

        print(f"\nYou chose: {userc}")
        print(f"Computer chose: {compc}\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)


        play_again_input = input("Do you want to play again? (y/n): ")
        play_again = play_again_input == "y"


if __name__ == "__main__":
    play_game()
