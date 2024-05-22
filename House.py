from Globals import (
    make_deck,
    shuffle_deck,
    is_ace,
    face_value,
)

class House():
    
    def __init__(self,num_decks):
        self.pid = 0
        self.decks = []
        self.hand = []
        # create num_decks decks and shuffle each deck
        for deck in range(num_decks):
            new_deck = make_deck()
            shuffle_deck(new_deck)
            self.decks.append(new_deck)
        # final shuffle
        shuffle_deck(self.decks)

    def deal(self,player):
        card_1 = self.decks[0].pop(0)
        card_2 = self.decks[0].pop(0)
        hand = (card_1,card_2)
        player.hand.append(hand)

    def hit(self,player):
        card = self.decks[0].pop(0)
        player_hand = player.hand[0]
        player.hand.pop(0)
        new_hand = player_hand + (card,)
        player.hand.append(new_hand)

    def calc_hidden_hand(self):
        shown_sum = 0
        hand_sum = 0
        alt_sum = 0
        dealer_ace = False
        if len(self.hand) != 0:
            n = 0
            for hand in self.hand:
                for card in hand:
                    if is_ace(card):
                        hand_sum += 1
                        alt_sum += 11
                        if n == 0:
                            dealer_ace = True
                            shown_sum = 11 
                    else:
                        x = face_value(card)
                        if x == 10:
                            hand_sum += x
                            alt_sum += x
                            if n == 0:
                                shown_sum = 10
                        else:
                            try:
                                if card[2] == '0':
                                    hand_sum += 10
                                    alt_sum += 10
                                    if n == 0:
                                        shown_sum = 10
                            except:
                                hand_sum += int(card[1])
                                alt_sum += int((card[1]))
                                if n == 0:
                                    shown_sum = hand_sum
                    # increment card count
                    n += 1
        # save sum state
        self.hand_sum = hand_sum
        self.alt_sum = alt_sum
        # output sum, but hide face-down card value
        if dealer_ace:
            return f'1/11'
        else:
            return f'{shown_sum}'
