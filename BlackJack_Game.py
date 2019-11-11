'''
This is a program for a simple BlackJack game
A deck of 52 cards will be used and a single player plays against the dealer (computer)
The player may place a bet 
For simplicity, only features like hit and stand are available
features like split, double, and insurance will be added in later versions
'''

import random

suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds') # The four suits of cards in a deck
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King') # The thirteen ranks of cards
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11} # Values of all ranks for the game
playing = True


class Card:
     '''
     A class for making cards objects. These 52 unique cards are added to a deck.
     Note : There is no use of Jokers in BlackJack so those cards are omitted.
     '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    '''
    A class for putting together a deck of cards.
    The Card class is used to make the unique cards to put into the deck.
    '''

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += '\n' + card.__str__()
        return deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    '''
    A class for building a hand with values for proceeding the game and deciding the winner.
    The Card class is used.
    '''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card_):
        self.cards.append(card_)
        self.value += values[card_.rank]

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''
    Chips are used to bet. This is currency of this game.
    A user gets 500 chips by default.
    '''

    def __init__(self):
        self.total = 500
        self.bet = 0

    def show_chips(self):
        return self.total

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet


def take_bet(chips):
    '''
    Takes input : an object of chips type
    Output : sets a value for the bet attribute of Chips class
    Function to take input of bet by the player and check if it exceeds the chips the player has
    '''
    
    while True:
        try:
            bet = int(input('Place your bet: '))

        except ValueError:
            print('Invalid bet! Try again!')

        else:
            if bet > chips.total:
                print('You don\'t have enough chips for that much bet. Please try again!')
            else:
                chips.bet = bet
                break


def hit(deck, hand):
    '''
    Takes input arguments : an object of deck type, an object of hand type
    Output : Calls functions of Hand class
    Function to perform the hit action in a game of BlackJack (hit is when a player demands for a card from the dealer)
    '''
    
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def stand():
    '''
    Takes no input argument
    Output : boolean value
    Function to operate on the global variable - playing. 
    Function to perform the stand action in a game of BlackJack (stand is when the player wants no more cards)
    '''

    global playing
    playing = False


def hit_or_stand(deck, hand):
    '''
    Takes input : an object of Deck type, an object of Hand type
    Output : calls hit or stand function as per user's request
    Function to perform one of the actions of BlackJack as pepr user's request
    '''

    while True:
        hit_stand = input('Press H to hit\nPress S to stand: ')
        if hit_stand.lower() == 'h':
            hit(deck, hand)
        elif hit_stand.lower() == 's':
            stand()
        else:
            print('Sorry. Please try again!')
            continue
        break


def show_some(player, dealer):
    '''
    Takes input : an object - player of Hand type, an object - dealer of Hand type
    Output : prints the cards as per the need
    Function to show some cards while the player plays
    '''
    
    print('Dealer\'s Hand: ')
    print('<Hidden Card>', dealer.cards[1])
    print('Player\'s Hand: ')
    print(*player.cards, sep='\t')


def show_all(player, dealer):
    '''
    Takes input : an object - player of Hand type, an object - dealer of Hand type
    Output : prints the cards as per the need
    Function to show all cards when the player stands
    '''
          
    print('Dealer\'s Hand: \n', *dealer.cards, sep='\t')
    print('Dealer Value : ', dealer.value)
    print('\nPlayer\'s Hand: \n', *player.cards, sep='\t')
    print('Player Value : ', player.value)


def player_busts(player, dealer, chips):
    '''
    Takes input : object of Hand type - player, object of Hand type - dealer, object of Chips type - chips
    Output : calls funtion from Chips class
    Function performs bust action if the player is busted (player loses)
    '''
    
    print('Busted! Better Luck Next Time!!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    '''
    Takes input : object of Hand type - player, object of Hand type - dealer, object of Chips type - chips
    Output : calls funtion from Chips class
    Function performs the player winning action (player wins)
    '''
    
    print('You win! Congratulations!!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    '''
    Takes input : object of Hand type - player, object of Hand type - dealer, object of Chips type - chips
    Output : calls funtion from Chips class
    Function performs the player winning action if the dealer is busted (player wins)
    '''

    print('Dealer Busted! Congratulations!!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    '''
    Takes input : object of Hand type - player, object of Hand type - dealer, object of Chips type - chips
    Output : calls funtion from Chips class
    Function performs the lose action (player loses)
    '''

    print('You Lose! Better Luck Next Time!!')
    chips.lose_bet()


def pushed(player, dealer):
    '''
    Takes input : object of Hand type - player, object of Hand type - dealer
    Output : prints the outcome as per the situation
    Function performs the push action of the game when the dealer ties with the player
    '''

    print('Pushed!')


# now to play the game

if __name__ == '__main__':
    while True:
        print('Welcome to BlackJack!')

        # Making and Shuffling new deck to play game
        new_deck = Deck()
        new_deck.shuffle()

        # Defining player and dealer hands and dealing cards one by one
        player = Hand()
        dealer = Hand()
        player.add_card(new_deck.deal())
        dealer.add_card(new_deck.deal())
        player.add_card(new_deck.deal())
        dealer.add_card(new_deck.deal())

        # Giving Chips to player to play
        player_chips = Chips()
        print('You have %d chips' % player_chips.show_chips())

        take_bet(player_chips)

        show_some(player, dealer)
        print(player.value)

        while playing:
            hit_or_stand(new_deck, player)
            show_some(player, dealer)
            print(player.value)
            if player.value > 21:
                player_busts(player, dealer, player_chips)
                break

        if player.value <= 21:
            while dealer.value < 17:
                hit(new_deck, dealer)

            show_all(player, dealer)

            if player.value > dealer.value:
                player_wins(player, dealer, player_chips)

            elif dealer.value > player.value:
                dealer_wins(player, dealer, player_chips)

            elif dealer.value > 21:
                dealer_busts(player, dealer, player_chips)

            else:
                pushed(player, dealer)

        print('You have %d chips' % player_chips.show_chips())

        play_again = input('Do you want to play again? Y/N: ')
        if play_again.lower() == 'y':
            playing = True
            continue
        else:
            print('Thank You for playing!')
            break
