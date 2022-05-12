###############
# cmpt120
# smartBot: a chatbot that intelligently responds to user input
# author: Steven Wong
# date: January 24, 2022

import random

# Greet the user
print("Greetings! I am smartBot, a totally self-aware AI created by Steven.")

# Ask the user for their name
userName = input("Human, what is your name? ")

# Address the user by their name
print("Hello", userName)

# asks the user if they want to hear a joke
userJoke = input("Would you like to hear a funny joke? ").lower()
jokeList = ["Two artists had an art contest. It ended up in draw...",
            "What rhymes with orange? No it doesn't...",
            "What did the DNA say to the other DNA? Do these genes make me look fat..."]

if userJoke == "yes" or userJoke == "sure" or userJoke == "yeah":
    print(random.choice(jokeList))
elif userJoke == "no" or userJoke == "nope" or userJoke == "nah":
    print("Aw", userName, "I had just the joke for you!!")
else:
    print("I didn't understand that.. but I'll take your response as non-interest.")

# asks the user for their favorite TV show
favoriteTV = input(userName + ", what is your favorite TV show? ")

if len(favoriteTV) % 2 == 0:
    print("Oh wow,", favoriteTV, "is also a favorite of mine!")
else:
    print("Darn, I haven't heard of that show before.")

# Asks the user if it is raining outside
rainStatus = input("By the way, is it raining outside? ").lower()
if rainStatus == ("yes") or rainStatus == ("yeah"):
    print("Make sure to bring an umbrella with you.")
print("Thanks for chatting and have a nice day!")






