import random

#vytvořený balík karet
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
colors = ["Hearts", "Diamonds", "Spades", "Clubs"]
pack = [{"Rank": rank, "Color": color} for rank in ranks for color in colors]
random.shuffle(pack)

card_count = 0
#nastavení limitu a součtu a žetonu
count = 0
limit = 21
chips = 1000

#převod slov na hodnoty
def value_of_card(card):
    if card.isnumeric():
        return int(card)
    elif card == "Jack" or card == "Queen" or card == "King":
        return 10
    elif card == "Ace":
        if count > limit:
            return 1
        else:
            return 11

def deal_card(pack):
    card = pack.pop()
    player_cards.append(card)


#ukládání karet

player_cards = []
dealer_cards = []


gameloop = True

#while gameloop == True:

#první tah

if card_count == 0:
    deal_card(pack)
    card_count = card_count + 1
    card = pack.pop()
    dealer_cards.append(card)
if card_count == 1:
    deal_card(pack)
    card_count = card_count + 1
    card = pack.pop()
    dealer_cards.append(card)
    print(player_cards)
    print(dealer_cards)


#druhý tah




print(card_count)