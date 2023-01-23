import random

#vytvořený balík karet
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
color = ["Hearts", "Diamonds", "Spades", "Clubs"]

#nastavení limitu a součtu
count = 0
limit = 21

#převod slov na hodnoty
def value_of_card(card_rank):
    if card_rank.isnumeric():
        return int(card_rank)
    elif card_rank == "Jack" or card_rank == "Queen" or card_rank == "King":
        return 10
    elif card_rank == "Ace":
        if count > limit:
            return 1
        else:
            return 11



pack = [{"Value": rank, "Color": color} for hodnota in rank for barva in color]

#dealování karet

card_rank = random.choice(rank)
card_color = random.choice(color)


print(card_rank)
print(card_color)

print(value_of_card(card_rank))