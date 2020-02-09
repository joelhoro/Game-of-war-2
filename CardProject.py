from utils import pickNumber

def setUp():
    print('/////-----Welcome To WAR!-----\\\\\\\\\\')
    player1 = player(50, input("What is your name?  "))
    print("Welcome %s!\nYou will begin with %s Shekels in Cash!" % (player1.name, player1.balance))

    if getAnswer("Do you know how to play?") == False:
        printInstructions()

    setBet(player1)


def setBet(player):
    loop = True
    while loop:
        try:
            bet = int(input('How much would you like to bet %s?' % player.name))
            if bet > player.balance:
                print("You don't have enough money!")
            else:
                loop = False
        except:
            print('You must enter a number.')
    player.bet = bet
    makeBet(player)


def makeBet(player):
    player.card = pickNumber(10)

    print("%s got the %s of %s" % (player.name, player.card, pickSuite()))
    computerCard = pickNumber(10)
    print("The computer got the %s of %s" % (computerCard, pickSuite()))
    if computerCard >= player.card:
        print("That means that you lost!")
        player.remove(player.bet)
        print("Your balance is now %s" % player.balance)
    else:
        print("That means that you won!")
        player.add(player.bet)
        print("Your balance is now %s" % player.balance)
    newGame(player)


def newGame(player):
    if player.balance == 0:
        print("You are now broke!")
        exit()
    if getAnswer("Would you like to play again?"):
        setBet(player)
    else:
        print("Bye Bye %s, enjoy the money and don't forget to gamble in moderation!" % player.name)
        exit()


def pickSuite():
    number = pickNumber(4)
    if number == 1:
        suite = "hearts"
    elif number == 2:
        suite = "clubs"
    elif number == 3:
        suite = "spades"
    else:
        suite = "diamonds"
    return suite



def printInstructions():
    print(
        "You and the computer will pick random cards from 1 to 10 and whoever gets the highest card wins, if it is a draw, the computer wins: the house always wins ;)")


def getAnswer(message):
    loop = True
    while loop:
        answer = input(message)
        if answer == "Y" or answer == "y" or answer == "yes":
            YesOrNo = True
            loop = False
        elif answer == "N" or answer == "n" or answer == "no":
            YesOrNo = False
            loop = False
        else:
            print("Answer only with yes or no")
    return YesOrNo


class player():
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.bet = 0
        self.card = 0

    def remove(self, amount):
        self.balance -= amount

    def add(self, amount):
        self.balance += amount

    def __repr__(self):
        return '%s has %s Shekels!' % (self.name, self.balance)


setUp()
