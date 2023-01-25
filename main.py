import random

#vytvořený balík karet
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
colors = ["Hearts", "Diamonds", "Spades", "Clubs"]
pack = [{"Rank": rank, "Suit": color} for rank in ranks for color in colors]
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
    count = count + value_of_card(card['Rank'])
if card_count == 1:
    deal_card(pack)
    card_count = card_count + 1
    card = pack.pop()
    dealer_cards.append(card)
    print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'])
    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
    count = count + value_of_card(card['Rank'])
    print("Your sum: ", count, "\n", "________________________________")
#druhý tah
input("Do you want to take a card?  1 - yes / 2 - no")


# print(card_count)


