import random

class games:
    def __init__(self, someString):
         getattr(self, someString)

    def evenodd():
        aNum = int(input("What number are you playing to?"))
        aNum = random.randint(0, aNum)
        guess = ""
        while guess != "even" or guess != "odd":
            guess = "What is your guess?"
        if guess == "odd":
            if aNum%2 ==0:
                print("You won!")
                return
            else:
                print("Wrong guess!")
                return
        else:
            if aNum%2 ==0:
                print("Wrong guess!")
                return
            else:
                print("You won!")
                return
    def headstails():
        guess = ""
        while guess != "heads" or guess != "tails":
            guess = input("Heads or tails?").lower()
        lst = ["heads", "tails"]
        result = lst[random.randint(0, 1)]
        if guess == result:
            print("You won with your guess of ", result, "!")
        else:
            print("It was not ", result)






gameStr = input("What game are you playing?").lower()

aGame = games(gameStr)
