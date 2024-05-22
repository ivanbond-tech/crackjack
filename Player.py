from Globals import (
    is_ace,
    face_value,
    player_id,
)

class Player():

    def __init__(self,starting_cash):
        global player_id
        self.pid = player_id
        self.cash = starting_cash
        self.hand = []
        self.can_split = False
        self.is_split = False
        self.can_double = False
        self.is_double = False
        self.is_insured = False
        self.last_bet = 0
        player_id += 1

    def wager(self,amount):
        if amount < 0:
            print('You cannot wager a negative amount')
            return False
        if amount - self.cash < 0:
            print(f'You cannot wager more than your balance: ${format(self.cash,","):.2f}')
            return False
        # wager amount from cash
        self.last_bet = amount
        self.cash -= self.last_bet
        return True

    def calc_hand(self):
        hand_sum = 0
        alt_sum = 0
        if len(self.hand) != 0:
            # get tuples from list
            for hand in self.hand:
                # get card from tuple
                for card in hand:
                    # check if card is an ace
                    if is_ace(card):
                        hand_sum += 1
                        alt_sum += 11
                    else:
                        # check if face card (set = 10)
                        x = face_value(card)
                        if x == 10:
                            hand_sum += x
                            alt_sum += x
                        # extract suit out of card value
                        else:
                            try:
                                if card[2] == '0':
                                    hand_sum += 10
                                    alt_sum += 10
                            except:
                                hand_sum += int(card[1])
                                alt_sum += int(card[1])
            # save hand's current sum
            self.hand_sum = hand_sum
            self.alt_sum = alt_sum
            # return string of sums
            if alt_sum != hand_sum and alt_sum <= 21:
                return f'{hand_sum}/{alt_sum}'
            else:
                return f'{hand_sum}'

    def split_pairs(self):
        # wager equal amount on second hand
        if self.can_split and self.wager(self.last_bet):
            # remove current hand tuple
            current_hand = self.hand.pop(0)
            # extract cards from current hand
            card_1 = current_hand[0]
            card_2 = current_hand[1]
            # split single tuple in player hand to two tuples
            self.hand.append((card_1,))
            self.hand.append((card_2,))
            # save player state
            self.is_split = True

    def double_down(self):
        # wager equal amount on second hand
        if self.can_double and self.wager(self.last_bet):
            # dealer must draw only one more card for this hand
            self.is_double = True

    def accept_insurance(self):
        if self.wager(int(self.last_bet/2)):
            self.is_insured = True

    def reset_hand(self):
        self.hand = []
        self.can_split = False
        self.is_split = False
        self.can_double = False
        self.is_double = False
        self.is_insured = False