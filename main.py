import random

# vytvořený balík karet
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
colors = ["♥", "♦", "♠", "♣"]
pack = [{"Rank": rank, "Suit": color} for rank in ranks for color in colors]
random.shuffle(pack)


# nastavení limitu, součtu a žetonu
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

# dealování karet
def deal_card_player(pack):
    card = pack.pop()
    player_cards.append(card)

def deal_card_dealer(pack):
    card = pack.pop()
    dealer_cards.append(card)

# výhry a prohry
def loose(chips):
    chips = chips - int(bet)
    print(chips)
    print("YOU LOST!")
def win(chips):
    chips = chips + int(bet) + int(bet)
    print("Your chips: ", chips)
    print("YOU WON!")

def double(chips):
    chips = chips + int(bet) + int(bet)
    print("Your chips: ", chips)
    print("YOU WON!")
def double_loose(chips):
    chips = chips - int(bet) - int(bet)
    print("Your chips: ", chips)
    print("YOU LOST")
def blackjack(chips):
    chips = chips + int(bet) + int(bet) / 2
    print("Your chips: ", chips)
    print("BLACKJACK!")

# ukládání karet

player_cards = []
dealer_cards = []

# menu
menu = print("██████  ██       █████   ██████ ██   ██      ██  █████   ██████ ██   ██\n██   ██ ██      ██   ██ ██      ██  ██       ██ ██   ██ ██      ██  ██ \n██████  ██      ███████ ██      █████        ██ ███████ ██      █████  \n██   ██ ██      ██   ██ ██      ██  ██  ██   ██ ██   ██ ██      ██  ██ \n██████  ███████ ██   ██  ██████ ██   ██  █████  ██   ██  ██████ ██   ██ \n")
menu_text = input("1 - Play\n2 - Ladder\n3 - Rules\n4 - About\n5 - End game\n")


menuloop = True
gameloop = False
ladderloop = False
rulesloop = False
aboutloop = False


while menuloop == True:
    print(menu)
    print(menu_text)
    if menu_text == "1":
        gameloop = True
        menuloop = False
    elif menu_text == "2":
        ladderloop = True
        menuloop = False
    elif menu_text == "3":
        rulesloop = True
        menuloop = False
    elif menu_text == "4":
        aboutloop = True
        menuloop = False
    elif menu_text == "5":
        quit()
    else:
        print("You chose wrong number!")
        menuloop = False


# žebříček


# pravidla
while rulesloop == True:
    rulesloop = False
    print("•At start you get 2 cards\n•Your goal is to get sum of 21 or less\n•If you have more than 21 you loose\n•If you have 21 or less and the dealer has less than you, you win\n•If dealer has more than you but it's 21 or less, you loose\n\n")

# about
while aboutloop == True:
    aboutloop = False
    print("Something about...........")
# hra
nickname = ""
while gameloop == True:
    nickname = input("Nickname: ")
    # první tah

    deal_card_dealer(pack)
    deal_card_player(pack)
    count_dealer = count_dealer + value_of_card(dealer_cards[0]['Rank'])
    count = count + value_of_card(player_cards[0]['Rank'])

    deal_card_dealer(pack)
    deal_card_player(pack)
    count_dealer = count_dealer + value_of_card(dealer_cards[1]['Rank'])
    print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'])
    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
    count = count + value_of_card(player_cards[1]['Rank'])
    print("Your sum: ", count, "\n", "________________________________")
    print("Your chips: ", chips)
    bet = input("Your bet: ")
    if count == 21:
        if count_dealer <= 16:
            deal_card_dealer(pack)
            count_dealer = count_dealer + value_of_card(dealer_cards[2]['Rank'])
            if count_dealer <= 16:
                deal_card_dealer(pack)
                count_dealer = count_dealer + value_of_card(dealer_cards[3]['Rank'])
                if count_dealer <= 16:
                    deal_card_dealer(pack)
                    count_dealer = count_dealer + value_of_card(dealer_cards[4]['Rank'])
                    if count_dealer > 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                              dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                              dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        blackjack(chips)
                    elif count_dealer == 21:
                        if count == 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  "|", dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("SPLIT!")
                        elif count < 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'],
                                  "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            loose(chips)
                    else:
                        if count < count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'],
                                  "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            loose(chips)
                        elif count > count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'],
                                  "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            blackjack(chips)
                if count_dealer > 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    blackjack(chips)
                elif count_dealer == 21:
                    if count == 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        print("SPLIT!")
                    elif count < 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        loose(chips)
                else:
                    if count < count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        loose(chips)
                    elif count > count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        blackjack(chips)
            if count_dealer > 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                      dealer_cards[2]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                blackjack(chips)
            elif count_dealer == 21:
                if count == 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    print("SPLIT!")
                elif count < 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
            else:
                if count < count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
                elif count > count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    blackjack(chips)
        else:
            if count_dealer > 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                      dealer_cards[2]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                blackjack(chips)
            elif count_dealer == 21:
                if count == 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                          dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    print("SPLIT!")
                elif count < 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
            else:
                if count < count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
                elif count > count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    blackjack(chips)
    # druhý tah

    take_card = input("Do you want to take a card?  1 - yes / 2 - no / 3 - double down")

    if take_card == "1":
        deal_card_player(pack)
        print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'])
        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
        count = count + value_of_card(player_cards[2]['Rank'])
        print("Your sum: ", count, "\n", "________________________________")
        if count > 21:
            loose(chips)
        elif count < 21:
            take_card = input("Do you want to take a card?  1 - yes / 2 - no")
            # třetí tah
            if take_card == "1":
                deal_card_player(pack)
                print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'], "|", player_cards[3]['Rank'], player_cards[3]['Suit'])
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
                count = count + value_of_card(player_cards[3]['Rank'])
                print("Your sum: ", count, "\n", "________________________________")
                if count > 21:
                    loose(chips)
                elif count < 21:
                    take_card = input("Do you want to take a card?  1 - yes / 2 - no")
                    # čtvrtý tah
                    if take_card == "1":
                        deal_card_player(pack)
                        print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'], "|", player_cards[3]['Rank'], player_cards[3]['Suit'], "|", player_cards[4]['Rank'], player_cards[4]['Suit'])
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "| Unknown")
                        count = count + value_of_card(player_cards[4]['Rank'])
                        print("Your sum: ", count, "\n", "________________________________")
                        if count > 21:
                            loose(chips)
                        elif count <= 21:
                            print("SPLIT!")
                    elif take_card == "2":
                        if count_dealer <= 16:
                            deal_card_dealer(pack)
                            count_dealer = count_dealer + value_of_card(dealer_cards[2]['Rank'])
                            if count_dealer <= 16:
                                deal_card_dealer(pack)
                                count_dealer = count_dealer + value_of_card(dealer_cards[3]['Rank'])
                                if count_dealer <= 16:
                                    deal_card_dealer(pack)
                                    count_dealer = count_dealer + value_of_card(dealer_cards[4]['Rank'])
                                    if count_dealer > 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'],
                                              dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                              dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                              dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                              dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                              dealer_cards[4]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        win(chips)
                                    elif count_dealer == 21:
                                        if count == 21:
                                            print("_______________________________")
                                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], "|",
                                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                                  dealer_cards[4]['Suit'])
                                            print("Dealer's sum: ", count_dealer)
                                            print("_______________________________")
                                            print("SPLIT!")
                                        elif count < 21:
                                            print("_______________________________")
                                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                                  dealer_cards[4]['Suit'])
                                            print("Dealer's sum: ", count_dealer)
                                            print("_______________________________")
                                            loose(chips)
                                    else:
                                        if count < count_dealer:
                                            print("_______________________________")
                                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                                  dealer_cards[4]['Suit'])
                                            print("Dealer's sum: ", count_dealer)
                                            print("_______________________________")
                                            loose(chips)
                                        elif count > count_dealer:
                                            print("_______________________________")
                                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                                  dealer_cards[4]['Suit'])
                                            print("Dealer's sum: ", count_dealer)
                                            print("_______________________________")
                                            win(chips)
                                if count_dealer > 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                          "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'],
                                          dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                                elif count_dealer == 21:
                                    if count == 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'],
                                              dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                              dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                              dealer_cards[3]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("SPLIT!")
                                    elif count < 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'],
                                              dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                              dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                              dealer_cards[3]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                else:
                                    if count < count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'],
                                              dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                              dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                              dealer_cards[3]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                    elif count > count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'],
                                              dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                              dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                              dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                              dealer_cards[3]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        win(chips)
                                if count_dealer > 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                                elif count_dealer == 21:
                                    if count == 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("SPLIT!")
                                    elif count < 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                else:
                                    if count < count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                    elif count > count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        win(chips)
                            else:
                                if count_dealer > 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                                elif count_dealer == 21:
                                    if count == 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("SPLIT!")
                                    elif count < 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)

                                else:
                                    if count < count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                    elif count > count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        win(chips)
                        else:
                            if count_dealer > 21:
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                win(chips)
                            elif count_dealer == 21:
                                if count == 21:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("SPLIT!")
                                elif count < 21:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    loose(chips)
                            else:
                                if count < count_dealer:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    loose(chips)
                                elif count > count_dealer:
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                elif take_card == "2":
                    if count_dealer <= 16:
                        deal_card_dealer(pack)
                        count_dealer = count_dealer + value_of_card(dealer_cards[2]['Rank'])
                        if count_dealer <= 16:
                            deal_card_dealer(pack)
                            count_dealer = count_dealer + value_of_card(dealer_cards[3]['Rank'])
                            if count_dealer <= 16:
                                deal_card_dealer(pack)
                                count_dealer = count_dealer + value_of_card(dealer_cards[4]['Rank'])
                                if count_dealer > 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|",
                                          dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                                          dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                                elif count_dealer == 21:
                                    if count == 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], "|", dealer_cards[2]['Suit'], "|",
                                              dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                                              dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        print("SPLIT!")
                                    elif count < 21:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|",
                                              dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                                              dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                else:
                                    if count < count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|",
                                              dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                                              dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        loose(chips)
                                    elif count > count_dealer:
                                        print("_______________________________")
                                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                              dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|",
                                              dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|",
                                              dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                                        print("Dealer's sum: ", count_dealer)
                                        print("_______________________________")
                                        win(chips)

                            if count_dealer > 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'], dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                win(chips)
                            elif count_dealer == 21:
                                if count == 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                          dealer_cards[3]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    print("SPLIT!")
                                elif count < 21:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                          dealer_cards[3]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    loose(chips)
                            else:
                                if count < count_dealer:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                          dealer_cards[3]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    loose(chips)
                                elif count > count_dealer:
                                    print("_______________________________")
                                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                          dealer_cards[3]['Suit'])
                                    print("Dealer's sum: ", count_dealer)
                                    print("_______________________________")
                                    win(chips)
                        if count_dealer > 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            win(chips)
                        elif count_dealer == 21:
                            if count == 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                print("SPLIT!")
                            elif count < 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                loose(chips)
                        else:
                            if count < count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                loose(chips)
                            elif count > count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                win(chips)
                    else:
                        if count_dealer > 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                  dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            win(chips)
                        elif count_dealer == 21:
                            if count == 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                print("SPLIT!")
                            elif count < 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                loose(chips)
                        else:
                            if count < count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                loose(chips)
                            elif count > count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                                      dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                win(chips)
            else:
                win(chips)
    elif take_card == "2":
        if count_dealer <= 16:
            deal_card_dealer(pack)
            count_dealer = count_dealer + value_of_card(dealer_cards[2]['Rank'])
            if count_dealer <= 16:
                deal_card_dealer(pack)
                count_dealer = count_dealer + value_of_card(dealer_cards[3]['Rank'])
                if count_dealer <= 16:
                    deal_card_dealer(pack)
                    count_dealer = count_dealer + value_of_card(dealer_cards[4]['Rank'])
                    if count_dealer > 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        win(chips)
                    elif count_dealer == 21:
                        if count == 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], "|", dealer_cards[2]['Suit'],"|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("SPLIT!")
                        elif count < 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            loose(chips)
                    else:
                        if count < count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            loose(chips)
                        elif count > count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'],  "|", dealer_cards[4]['Rank'], dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            win(chips)
                if count_dealer > 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    win(chips)
                elif count_dealer == 21:
                    if count == 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        print("SPLIT!")
                    elif count < 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        loose(chips)
                else:
                    if count < count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        loose(chips)
                    elif count > count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'], "|",dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        win(chips)
            if count_dealer > 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                win(chips)
            elif count_dealer == 21:
                if count == 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    print("SPLIT!")
                elif count < 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
            else:
                if count < count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
                elif count > count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'] , "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    win(chips)
        else:
            if count_dealer > 21:
                print("_______________________________")
                print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                print("Dealer's sum: ", count_dealer)
                print("_______________________________")
                win(chips)
            elif count_dealer == 21:
                if count == 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    print("SPLIT!")
                elif count < 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
            else:
                if count < count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    loose(chips)
                elif count > count_dealer:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    win(chips)
    elif take_card == "3":
        deal_card_player(pack)
        print("__________________________________", "\n", "Your cards: ", player_cards[0]['Rank'], player_cards[0]['Suit'], "|", player_cards[1]['Rank'], player_cards[1]['Suit'], "|", player_cards[2]['Rank'], player_cards[2]['Suit'])
        count = count + value_of_card(player_cards[2]['Rank'])
        print("Your sum: ", count, "\n", "________________________________")
        if count > 21:
            double_loose(chips)
        elif count <= 21:
            if count_dealer <= 16:
                deal_card_dealer(pack)
                count_dealer = count_dealer + value_of_card(dealer_cards[2]['Rank'])
                if count_dealer <= 16:
                    deal_card_dealer(pack)
                    count_dealer = count_dealer + value_of_card(dealer_cards[3]['Rank'])
                    if count_dealer <= 16:
                        deal_card_dealer(pack)
                        count_dealer = count_dealer + value_of_card(dealer_cards[4]['Rank'])
                        if count_dealer > 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                  dealer_cards[4]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            double(chips)
                        elif count_dealer == 21:
                            if count == 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'],
                                      dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                      dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'], "|",
                                      dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                      dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                      dealer_cards[4]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                print("SPLIT!")
                            elif count < 21:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'],
                                      dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                      dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                      dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                      dealer_cards[4]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                double_loose(chips)
                        else:
                            if count < count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'],
                                      dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                      dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                      dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                      dealer_cards[4]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                double_loose(chips)
                            elif count > count_dealer:
                                print("_______________________________")
                                print("Dealer cards: ", dealer_cards[0]['Rank'],
                                      dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                      dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                      dealer_cards[2]['Suit'], "|", dealer_cards[3]['Rank'],
                                      dealer_cards[3]['Suit'], "|", dealer_cards[4]['Rank'],
                                      dealer_cards[4]['Suit'])
                                print("Dealer's sum: ", count_dealer)
                                print("_______________________________")
                                double(chips)
                    if count_dealer > 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'],
                              dealer_cards[3]['Rank'], dealer_cards[3]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double(chips)
                    elif count_dealer == 21:
                        if count == 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            print("SPLIT!")
                        elif count < 21:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            double_loose(chips)
                    else:
                        if count < count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            double_loose(chips)
                        elif count > count_dealer:
                            print("_______________________________")
                            print("Dealer cards: ", dealer_cards[0]['Rank'],
                                  dealer_cards[0]['Suit'], "|", dealer_cards[1]['Rank'],
                                  dealer_cards[1]['Suit'], "|", dealer_cards[2]['Rank'],
                                  dealer_cards[2]['Suit'], dealer_cards[3]['Rank'],
                                  dealer_cards[3]['Suit'])
                            print("Dealer's sum: ", count_dealer)
                            print("_______________________________")
                            double(chips)
                if count_dealer > 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    double(chips)
                elif count_dealer == 21:
                    if count == 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        print("SPLIT!")
                    elif count < 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double_loose(chips)
                else:
                    if count < count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double_loose(chips)
                    elif count > count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double(chips)
            else:
                if count_dealer > 21:
                    print("_______________________________")
                    print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'], "|",
                          dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                          dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                    print("Dealer's sum: ", count_dealer)
                    print("_______________________________")
                    double(chips)
                elif count_dealer == 21:
                    if count == 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'], "|",
                              dealer_cards[2]['Rank'], dealer_cards[2]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        print("SPLIT!")
                    elif count < 21:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double_loose(chips)
                else:
                    if count < count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double_loose(chips)
                    elif count > count_dealer:
                        print("_______________________________")
                        print("Dealer cards: ", dealer_cards[0]['Rank'], dealer_cards[0]['Suit'],
                              "|", dealer_cards[1]['Rank'], dealer_cards[1]['Suit'])
                        print("Dealer's sum: ", count_dealer)
                        print("_______________________________")
                        double(chips)

    else:
        print("You need to pick 1 - yes / 2 - no / 3 - double down")
