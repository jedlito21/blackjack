import random

# vytvořený balík karet
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
colors = ["♥", "♦", "♠", "♣"]
pack = [{"Rank": rank, "Suit": color} for rank in ranks for color in colors]
random.shuffle(pack)

card_count = 0
card_count_dealer = 0
# nastavení limitu a součtu a žetonu
count = 0
count_dealer = 0
limit = 21
chips = 1000

# převod slov na hodnoty
def value_of_card(card):
    if card.isnumeric():
        return int(card)
    elif card == "Jack" or card == "Queen" or card == "King":
        return 10
    elif card == "Ace":
        if count + 11 > limit:
            return 1
        else:
            return 11

def deal_card_player(pack):
    card = pack.pop()
    player_cards.append(card)

def deal_card_dealer(pack):
    card = pack.pop()
    dealer_cards.append(card)


# ukládání karet

player_cards = []
dealer_cards = []


gameloop = True

while gameloop == True:

    # první tah
    if card_count == 0:
        deal_card_dealer(pack)
        deal_card_player(pack)
        count_dealer = count_dealer + value_of_card(dealer_cards[0]['Rank'])
        card_count = card_count + 1
        card_count_dealer = card_count_dealer + 1
        count = count + value_of_card(player_cards[0]['Rank'])
    if card_count == 1:
        deal_card_dealer(pack)
        deal_card_player(pack)
        count_dealer = count_dealer + value_of_card(dealer_cards[1]['Rank'])
        card_count = card_count + 1
        card_count_dealer = card_count_dealer + 1
        print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'])
        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
        count = count + value_of_card(player_cards[1]['Rank'])
        print("Your sum: ", count, "\n", "________________________________")
        if count == 21:
            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
            print(count_dealer)
            print("BLACKJACK!")
            break
    # druhý tah

    take_card = input("Do you want to take a card?  1 - yes / 2 - no")

    if take_card == "1":
        if card_count == 2:
            deal_card_player(pack)
            card_count = card_count + 1
            print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'])
            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
            count = count + value_of_card(player_cards[2]['Rank'])
            print("Your sum: ", count, "\n", "________________________________")
            if count > 21:
                print("YOU LOST!")
                break
            elif count < 21:
                take_card = input("Do you want to take a card?  1 - yes / 2 - no")
                if take_card == "1":
                    if card_count == 3:
                        deal_card_player(pack)
                        card_count = card_count + 1
                        print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'], "|", player_cards[3]['Rank'], player_cards[3]['Suit'])
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
                        count = count + value_of_card(player_cards[3]['Rank'])
                        print("Your sum: ", count, "\n", "________________________________")
                        if count > 21:
                            print("YOU LOST!")
                            break
                        elif count < 21:
                            take_card = input("Do you want to take a card?  1 - yes / 2 - no")
                            if take_card == "1":
                                if card_count == 4:
                                    deal_card_player(pack)
                                    card_count = card_count + 1
                                    print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'], "|", player_cards[3]['Rank'], player_cards[3]['Suit'], "|", player_cards[4]['Rank'], player_cards[4]['Suit'])
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
                                    count = count + value_of_card(player_cards[4]['Rank'])
                                    print("Your sum: ", count, "\n", "________________________________")
                                    if count > 21:
                                        print("YOU LOST!")
                                        break
                                    elif count <= 21:
                                        print("SPLIT!")
                                        break
                            elif take_card == "2":
                                if count_dealer > 21:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("YOU WON!")
                                    break
                                elif count_dealer == 21:
                                    if count == 21:
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("SPLIT!")
                                        break
                                    elif count < 21:
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("YOU LOST!")
                                        break
                                else:
                                    if count < count_dealer:
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("YOU LOST!")
                                        break
                                    elif count > count_dealer:
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("YOU WON!")
                                        break
                        else:
                            if count_dealer > 21:
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                print("YOU WON!")
                                break
                            elif count_dealer == 21:
                                if count == 21:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("SPLIT!")
                                    break
                                elif count < 21:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("YOU LOST!")
                                    break
                            else:
                                if count < count_dealer:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("YOU LOST!")
                                    break
                                elif count > count_dealer:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("YOU WON!")
                                    break
                elif take_card == "2":
                    if count_dealer > 21:
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        print("YOU WON!")
                        break
                    elif count_dealer == 21:
                        if count == 21:
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("SPLIT!")
                            break
                        elif count < 21:
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("YOU LOST!")
                            break
                    else:
                        if count < count_dealer:
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("YOU LOST!")
                            break
                        elif count > count_dealer:
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("YOU WON!")
                            break
                    break
            else:
                print("YOU WON!")
    elif take_card == "2":
        if count_dealer > 21:
            print("_______________________________")
            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
            print("Dealer's sum: ", count_dealer)
            print("_______________________________")
            print("YOU WON!")
            break
        elif count_dealer == 21:
            if count == 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                print("SPLIT!")
                break
            elif count < 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                print("YOU LOST!")
                break
        else:
            if count < count_dealer:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                print("YOU LOST!")
                break
            elif count > count_dealer:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                print("YOU WON!")
                break
        break
    else:
        print("You need to pick 1 - yes or 2 - no")
        break