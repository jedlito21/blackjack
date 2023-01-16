import random

def card_value(card_rank):
    for key, value in values.items():
        print(value)

#vytvořený balík karet
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
color = ["Hearts", "Diamonds", "Spades", "Clubs"]

values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

pack = [{"Value": rank, "Color": color} for hodnota in rank for barva in color]

#dealování karet

card_rank = random.choice(rank)
card_color = random.choice(color)

print(card_rank)
print(card_color)

card_value(card_rank)