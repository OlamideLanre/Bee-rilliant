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
    "gregarious",
    "haphazard",
    "incongruous"
]
correct=[]
missed=[]
said= None
count=0
# Initialize the TTS engine
engine = pyttsx3.init()
    # Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

def usersGuess(users_spelling,word, index):
    if users_spelling == word[index]:
        count=count+1
        engine.say("Correct!")
        engine.runAndWait()
        
        # appended= correct.append(users_spelling)
        # if appended in spelling_bee_words:
        #     said= True
        #     if said==True:
        # SayWord()
        if count== len(spelling_bee_words):
            engine.say("game over")
            engine.runAndWait()
    else:
        engine.say("Incorrect")
        engine.runAndWait()

def SayWord():
    while True:
        random_number = random.randint(1, 19)
        print(random_number)
        for index in range(len(spelling_bee_words)):
            if random_number == index:
                # Convert text to speech
                engine.say(spelling_bee_words[index])
                engine.runAndWait()
                users_spelling= input("spell the word: ")
                usersGuess(users_spelling= users_spelling,word= spelling_bee_words, index=index)
               

SayWord()




