import random
import time

money = 100

#Write your game of chance functions here
class Deck:
    def __init__(self):
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', "King", "Ace"]
        self.names = ['hearts', 'diamonds', 'spades', 'clubs']
        self.deck = []
        for value in self.values:
            for name in self.names:
             self.deck.append('{value} of {name}'.format(value=value, name=name))

def coin_flip(player_choice, player_bet):
    odds = random.randint(1, 100)
    result = None
    if odds <= 50:
        result = "Heads"
    elif odds >=51:
        result = "Tails"
    else:
        print("There has been an error recording the coin flip results")
    print("The coin has landed on " + result + "!")
    if player_choice == result:
        player_bet = (player_bet * 1.5)
        print("You have won the coin toss!, and won " + str(player_bet) + " dollars!")
        return player_bet
    elif player_choice != result:
        print("You have lost the coin toss, and lost " + str(player_bet) + " dollars :(")
        player_bet = player_bet - (player_bet * 2)
        return player_bet
        
    
def cho_han(player_choice, player_bet):
    dice_1 = random.randint(1, 6)
    print("The first dice has rolled a ")
    time.sleep(2)
    print(str(dice_1) + "!")
    time.sleep(1)
    dice_2 = random.randint(1, 6)
    print("The second dice has rolled a ")
    time.sleep(2)
    print(str(dice_2) + "!")
    sum_of_dice = dice_1 + dice_2   
    result = None

    if sum_of_dice % 2 == 0:
        result = "Even"
    elif sum_of_dice % 2 != 0:
        result = "Odd"
    else:
        print("There has been an error calculating the result. Please try again")

    print("The sum of the dice is " + str(sum_of_dice) + ", and is therefore " + result + "!")

    if player_choice == result:
        player_bet = (player_bet * 1.5)
        print("You have won, and won " + str(player_bet) + " dollars!")
        return player_bet
    elif player_choice != result:
        print("You have lost, and lost " + str(player_bet) + " dollars :(")
        player_bet = player_bet - (player_bet * 2)
        return player_bet

def war(player_bet):
    deck = Deck()
    print(deck.deck[4])
    

#Call your game of chance functions here

war(100)
print("your new balance is " + str(money) + " dollars.")