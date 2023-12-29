# Importing the necessary modules
import random

# Creating a class for deck 
class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        # Creating the deck of cards
        for suit in self.suits:
            for value in self.values:
                self.cards.append((suit, value))
    
    # Shuffling the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
    
    # Dealing a card from the deck
    def deal_card(self):
        return self.cards.pop()
    
# Creating a class for the player
class Player:
    def __init__(self):
        self.hand = []
    
    # Adding a card to the player's hand
    def add_card(self, card):
        self.hand.append(card)
    
    # Calculating the total value of the player's hand
    def calculate_hand_value(self):
        total_value = 0
        for card in self.hand:
            if card[1] in ['Jack', 'Queen', 'King']:
                total_value += 10
            elif card[1] == 'Ace':
                if total_value + 11 <= 21:
                    total_value += 11
                else:
                    total_value += 1
            else:
                total_value += int(card[1])
        return total_value
    
# Creating a class
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
    
    # Starting Game
    def start_game(self):
        print("Welcome to Blackjack!")
        self.deck.shuffle()
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.show_initial_cards()
        self.player_turn()
    
    # Showing the first cards
    def show_initial_cards(self):
        print("Player's cards:")
        for card in self.player.hand:
            print(card)
        print("Dealer's cards:")
        print(self.dealer.hand[0])
    
    # Player's go
    def player_turn(self):
        while True:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == 'hit':
                self.player.add_card(self.deck.deal_card())
                self.show_initial_cards()
                if self.player.calculate_hand_value() > 21:
                    print("Bust! You lose.")
                    break
            elif choice.lower() == 'stand':
                self.dealer_turn()
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")
    
    # Dealer's go
    def dealer_turn(self):
        print("Dealer's cards:")
        for card in self.dealer.hand:
            print(card)
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())
            print("Dealer hits.")
            print("Dealer's cards:")
            for card in self.dealer.hand:
                print(card)
        if self.dealer.calculate_hand_value() > 21:
            print("Dealer busts! You win.")
        else:
            self.compare_hands()
    
    # Comparing the hands 
    def compare_hands(self):
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()
        print("Player's hand value:", player_value)
        print("Dealer's hand value:", dealer_value)
        if player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose.")
        else:
            print("It's a tie.")
