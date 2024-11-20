# importing modules
import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw a card
drawn_card = deck.pop()
print(f"Drawn card: {drawn_card[0]} of {drawn_card[1]}")