import random
import time

money = 100

#Write your game of chance functions here
class Deck:
    def __init__(self):
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace"]
        self.names = ['hearts', 'diamonds', 'spades', 'clubs']
        self.deck = []
        for value in self.values:
            for name in self.names:
                self.deck.append('{value} of {name}'.format(value=value, name=name))

def get_card_value(p_card):
    card_value = p_card.split(' ', 1)[0]
    if card_value == "Ace":
        card_value = 1
    elif card_value == "Jack":
        card_value = 11
    elif card_value == "Queen":
        card_value = 12
    elif card_value == "King":
        card_value = 13
    else:
        card_value = int(card_value)
    return card_value

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
    def print_player_cards(p1_card, p2_card):
        print("You have drawn a:")
        time.sleep(1)
        print(p1_card)
        time.sleep(1)
        print("Player 2 has drawn a:")
        time.sleep(1)
        print(p2_card)
        time.sleep(1)

    game_deck = Deck()
    p1_choice = random.randint(0, 51)
    p1_card = game_deck.deck[p1_choice]
    game_deck.deck.remove(p1_card)
    p2_choice = random.randint(0, 50)
    p2_card = game_deck.deck[p2_choice]

    print_player_cards(p1_card, p2_card)

    p1_value = get_card_value(p1_card)
    p2_value = get_card_value(p2_card)

    if p1_value == p2_value:
        print("There has been a tie! You have gotten your money back.")
        return player_bet
    elif p1_value > p2_value:
        print("You have won! You have doubled your money.")
        return player_bet
    elif p1_value < p2_value:
        print("You have lost. You have lost your bet. :(")
        player_bet = player_bet * -1
        return player_bet
    else:
        print("There has been an error. Your money has been returned.")
    

    

    
    
    

#Call your game of chance functions here

money += war(100)


time.sleep(0.5) 
print("your new balance is " + str(money) + " dollars.")