import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

##### Name: Anandita Aggarwal       #####
##### Uniqname:aanandit#####

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_club(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_king_of_spades(self):
        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")

    # Test that if you create a deck instance, 
    # it will have 52 cards in its cards instance variable
    def test_4_52_cards(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_5_return_card(self):
        deck = cards.Deck()
        self.assertIsInstance(deck.deal_card(), cards.Card)
    
    def test_6_return_fewer(self):
        deck = cards.Deck()
        fewer = len(deck.cards) - 1
        deck.deal_card()
        self.assertEqual(len(deck.cards), fewer)
    
    def test_7_return_more(self):
        deck = cards.Deck()
        deal = deck.deal_card()
        more = len(deck.cards) + 1
        deck.replace_card(card = deal)
        self.assertEqual(len(deck.cards), more)
    
    def test_8_return_more(self):
        deck = cards.Deck()
        num_cards = len(deck.cards)
        for i in deck.cards:
            deck.replace_card(card=i)
            self.assertEqual(len(deck.cards),num_cards)

# 8. Test that if you invoke the replace_card method with a card that is already in the deck, 
# the deck size is not affected.
# (The function must silently ignore it if you try to add a card that’s already in the deck)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()