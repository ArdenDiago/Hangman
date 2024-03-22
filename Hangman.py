# Hangman Game
"""
Functions of the game:
    1. wordselector()
    2. executioner()
    3. check()
    4. result()
    5. rules()

  o
 /|\'
  |
 / \'
"""
from random import randrange, choice
from time import sleep
import os
name = None
computerword = computeritem = ""
wordoutline = wordlist = []
usertrys = 0


def wordselector():
    "The function will select a word for the game"
    global computerword, computeritem, wordoutline, wordlist
    fruits = ["Mango","Apple","Orange","Banana","Grape","Kiwifruit","Cherry","Apricot","Pineapple","Watermelon","Papaya","Grapefruit","Strawberry","Lemon","Peach","Avocado","Pear","Blueberry","Plum","Pomegranate","Fig","Blackberry","Guava","Lime"]

    flowervegetable = ["Cauliflower","Broccoli","Artichoke","Banana flower","Romanesco broccoli","Zucchini flowers"]
    leafyvegetables = ["Cabbage","Arugula","Spinach","Celery","Lettuce","Coriander leaves","Mint","Spring onion","Bok choy","Romaine lettuce","Rapini","Mustard greens","Kale"]
    rootvegetables = ["Beetroot","Carrot","Turnip","Radish","White radish","Celeriac","Rutabaga","Swede","Sugar beet","Parsnip","Horseradish"]
    tubervegetables = ["Potato","Tapioca","Arracacia","Elephant yam","Ginger","Greater yam","Turmeric","Purple yam","Chinese potato","Arrowroot"]
    fruitvegetables = ["Cucumber","Pumpkin","Tomato","Peppers","Eggplant","String beans","Green peas","Corn","Lady's finger","Beans","Chickpeas"]
    stemvegetables = ["Asparagus","Lemon grass","Celery","Kohlrabi","Celtuce","Rhubarb","Swiss chard","Cardoon"]

    mywordlist = {
        1 : fruits,
        2 : flowervegetable,
        3 : leafyvegetables,
        4 : rootvegetables,
        5 : tubervegetables,
        6 : fruitvegetables,
        7 : stemvegetables,
    }
    myworditems = {
        1 : "fruits",
        2 : "flower vegetable",
        3 : "leafy vegetables",
        4 : "root vegetables",
        5 : "tuber vegetables",
        6 : "fruit vegetables",
        7 : "stem vegetables",
    }
    randomnumber = randrange(1 , len(mywordlist) + 1)
    computeritem = myworditems.get(randomnumber)
    computerword = choice(mywordlist.get(randomnumber)).upper()
    wordlist = [lettors for lettors in computerword]
    wordoutline = ["_" if i != " " else " " for i in wordlist]
    print(computerword)

def executioner():
    "The Outline of the gallows and the user gussed word"

    manitems = [' O','/|\\',' |','/ \\']
    tabs = 9
    length = 7
    for i in range(length):
        if i == 0:
            [print("_",end="") for x in range(tabs * 4 - 1)]
            print()
        elif i > 0 and i < 3:
            print("|", end="")
            [print(" ",end="") for x in range(tabs * 4 - 2)]
            print("|")
        elif i == length - 1:
            print("|",end="")
            [print("_",end="") for x in range(tabs * 4 - 2)]
            print("|")
        elif usertrys > 0 and usertrys <= 4 and i - 3 == 0:
            for x in range(usertrys):
                print("|",end="")
                [print(" ",end="") for x in range(tabs * 4 - 3)]
                print(manitems[x])
        elif usertrys == 5 and i - 4 == 0:
            print("|",end="")
            [print(" ",end="") for x in range(tabs * 4 - 3)]
            print()
            for x in range(usertrys - 1):
                print("|",end="")
                [print(" ",end="") for x in range(tabs * 4 - 3)]
                print(manitems[x])
        else:
            print("|")
    
    if usertrys != 5:
        for br in range(0,3):
            if br == 0 or br == 2:
                for brout in range(len(wordoutline) * 2 + 6):
                    if brout == 0:
                        [print("=",end="") for i in range(len(computeritem) + 3)]
                        print("| |",end="")
                    else:
                        print("=", end = "")
                print()
            else:
                print("|",computeritem.title(), end="")                   
                print(" | |  ", end="")
                for outline in wordoutline:
                    print(outline, end=" ")
                print("  |")
    return

def check():
    "Check the input of the user and check if it is present in a wordlist and if it is present then it reasigns value to the wordoutline"
    global usertrys
    usrinp = str(input("Enter a Lettor: "))
    while(not(usrinp.isalpha())):
        usrinp = input("Error !!!\nEnter a Lettor: ")
    if usrinp.upper() in wordlist:
        for word in range(len(wordlist)):
            if wordlist[word] == usrinp.upper():
                wordoutline[word] = usrinp.upper()
    else:
        print(f"--- Wrong Lettor ---")
        usertrys += 1
    executioner()
    if wordoutline == wordlist:
        print(f"--- You Won ---")
        result()
    elif usertrys != 5:
        check() 
    else:
        print(f"--- Wrong Lettor ---")
        result()
        
def result():
    "Result Template"
    global usertrys, name, computeritem, computerword, wordoutline
    print("------ Result ------")
    wordattributs = ["Name","Categories","Computer Choice","User Choice","No of tries"]
    wordrow = [name,computeritem,computerword,(list(set(wordoutline))),len(list(set(wordoutline)))]
    totallen = 0
    for (i, j) in zip(wordrow, wordattributs): # Coutn the Border length
        try:
            if len(i) > len(j):
                setspace = len(i) - len(j)
                totallen += setspace + len(j)
            else:
                totallen += len(j)  + 1
        except:
            if type(i) is list:
                setspace = len(i)
                totallen += setspace + 2
            else:
                totallen += len(j) + 1
    totallen *= 2
    for br in range(4): # Rendering the result layout
        if br == 0 or br == 3: # Border ========================
           # print(" ",end="")
            for i in range(0,totallen + 1):
                print("=", end="") 
            print()
        elif br == 1: # field name
            for (i, j) in zip(wordrow, wordattributs):
                try:
                    if type(i) is list:
                        setspace = len(i)
                        print(f"| {j.center((((setspace * 3) + (setspace - 1) + (setspace - 1)) + 2))} ",end="")
                    elif len(i) > len(j):
                        setspace = len(i) - len(j)
                        setspace += len(j)
                        print(f"| {j.center(setspace + 1)} ",end="")
                    else:
                        print(f"| {j.center(len(wordattributs)  + 1)} ",end="")
                except:
                        print(f"| {str(j).center(len(j) + 1)} ", end="")
            print(" |")
        else: # data insertion
            for (i, j) in zip(wordrow, wordattributs):
                try:
                    if len(i) > len(j):
                        setspace = len(i) - len(j)
                        setspace += len(j)
                        print(f"| {i.center(setspace + 1)} ",end="")
                    else:
                        print(f"| {i.center(len(wordattributs + 1))} ",end="")
                except:
                    if  type(i) == list:
                        print(f"| {i} ",end="")
                    else:
                        print(f"| {str(i).center(len(j) + 1)}", end="")
            print("  |")
    replay = str(input("Do U want to play again Y/N: "))
    if replay.upper() == "Y" or len(replay) > 1 and replay[0].upper() == "Y":
        computerword = computeritem = ""
        wordoutline.clear()
        wordlist.clear()
        usertrys = 0
        print(f"Welcome {name.title()}.".center(os.get_terminal_size()[0]))
        sleep(1)
        print("\nHope by now u are familer with the rules.\nSo let the game begin.")
        sleep(2)
        wordselector()
        executioner()
        check()
    else:
        print("Byee :)")

def start():
    global name
    while not bool(name) and not type(name) is str:
        name = input("Enter Your Name: ")
    
    rules = [f"Welcome {name.title()}".center(os.get_terminal_size()[0]), "The computer will pick the secret word","the user will  start guessing letters .","Fill the letter in the blanks if the players guess correctly then it is will be shown.", "Draw part of the hangman when the players guess wrong then the person will be drawn.", "The players win when they guess the correct word.", "let the Game begin"]
    for rule in rules:
        print(rule.title())
        sleep(1)
    wordselector()
    executioner()
    check()

start()
