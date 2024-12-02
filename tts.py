import pyttsx3
import random

spelling_bee_words = [
    "quintessential",
    "ambiguous",
    "phenomenon",
    "conundrum",
    "allegiance",
    "indispensable",
    "quarantine",
    "enigmatic",
    "idiosyncrasy",
    "gregarious",
    "vivacious",
    "anachronistic",
    "benevolent",
    "camaraderie",
    "diabolical",
    "effervescent",
    "facetious",
    "aerodynamic",
    "haphazard",
    "incongruous"
]

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

def SayWord():
    count = 19
    score = 0
    missed = 0
    while spelling_bee_words:
        word = random.choice(spelling_bee_words)  # Select a random word from the list
        engine.say(word)
        engine.runAndWait()
        users_spelling = input("Spell the word: ")
        if users_spelling == word:
            score += 1
            engine.say("Correct!")
            engine.runAndWait()
            spelling_bee_words.remove(word)
        else:
            engine.say("Incorrect")
            engine.runAndWait()
            missed += 1
            spelling_bee_words.remove(word)
        
        if spelling_bee_words:
            print("Game continues")
        else:
            engine.say(f"Game over, you scored {score} out of {count} and missed {missed}")
            engine.runAndWait()
            break

print("******BEE-RILLIANT*****")
user= input("Please register by entering your name: ")
print("******YOU READY?*****")
option=input("yes/no: ")
if option=="yes" or option=="Yes":
    print(f"Welcome {user} to BEE-RILLIANT spelling bee!")
    print("LETS GO!")
    SayWord()
else:
    print("ok bye")


