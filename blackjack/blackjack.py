"""
My implementation of blackjack by Al Sweigart
"""

import random, sys

# Constants setup
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print("Blackjack: A classic card game.")
    print("""
          Rules:
            Try to get as close to 21 points without going over.
            King, Queens, and Jacks are worth 10 points.
            Ace are worth either 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)stand to stop taking cards.
            (D)ouble down to increase your bet but under two conditions:
                1. On your first play
                2. Must hit exactly oe more time before standing
            The dealer stops hitting at 17.
            In case of a tie, the bet is returned to the player.
          """)

    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing this is just a program, huh?")
            print("Thanks for playing :)")
            sys.exit()

        print("Money: ", money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Bet: ", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()  # A blank line

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            # Player actions
            if move == 'D':  # Double down
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}".format(bet))

            if move in ('H', 'D'):  # Hit/doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}".format(rank, suit))
                playerHand.append(newCard)

            if move in ('S', 'D'):
                break

            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:
                    print("Dealer Hits...")
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)

                    if getHandValue(dealerHand) > 21:
                        break
                    input("Pres enter to continue...")
                    print()
                    print()

            displayHands(playerHand, dealerHand, True)
            
            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            if dealerValue > 21:
                print("Dealer busts! You win ${}!".format(bet))
                money += bet
            elif playerValue > 21 or playerValue < dealerValue:
                print("You lost!")
                money -= bet
            elif playerValue > dealerValue:
                print("You won ${}!".format(bet))
            elif playerValue == dealerValue:
                print("It's a tie.")

            input("Press enter to continue...")
            print()
            print()


def getBet(max):
    while True:
        print("How much do you want to bet? (1-{}), or (Q)uit)".format(max))
        bet = input('> ').upper().strip()
        if bet == 'Q':
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            aces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

        value += aces
        for i in range(aces):
            if value + 10 <= 21:
                value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += " ___   "
        if card == BACKSIDE:
            rows[1] += "|## |  "
            rows[2] += "|###|  "
            rows[3] += "|_##|  "
        else:
            rank, suit = card
            rows[1] += "|{} |  ".format(rank.ljust(2))  # left-align string and use space as padding
            rows[2] += "| {} |  ".format(suit)
            rows[3] += "|_{}|  ".format(rank.rjust(2, "_"))  # right-align string and use '_' as padding

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ["(H)it, (S)tand"]

        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()
