"""Module providing a function printing python version."""
import os
import random

from isort import file

print("Welcome to a random word generator!")
print("This program will generate a random word for you")

print("Please enter a selection from the following options:")
print("1. Generate a random word")
print("2. Exit")
selection = input("Enter your selection: ")

if selection == "1":
    # RootDir = "./"
    # fileToSearch = "words.txt"
    # first search for the file in the current directory
    if os.path.isfile("words.txt"):
        # print("File Found")
        with open("words.txt", "r") as f:
            # print(f.read())
            print("Here's your random word")
            randomWord = random.choice(f.read().splitlines())
            print(randomWord)

    print("Word Selected")
    exit()
else:
    print("Exiting the program. Goodbye!")
    exit()
