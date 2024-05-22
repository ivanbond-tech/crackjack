from Globals import *
from House import House
from Player import Player

def print_banner():
    clear_screen()
    s = '\nWelcome to,\n'
    s += '.------..------..------..------..------..------..------..------..------.\n'
    s += '|C.--. ||R.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |\n'
    s += '| :(): || :/\\: || (\\/) || :/\\: || :/\\: || :(): || (\\/) || :/\\: || :/\\: |\n'
    s += '| ()() || (__) || :\\/: || :\\/: || :\\/: || ()() || :\\/: || :\\/: || :\\/: |\n'
    s += "| \'--\'C|| \'--\'R|| \'--\'A|| \'--\'C|| \'--\'K|| \'--\'J|| \'--\'A|| \'--\'C|| \'--\'K|\n"
    s += "`------'`------'`------'`------'`------'`------'`------'`------'`------'\n"
    s += 'A Blackjack emulator to help you \'quasi-learn\' to count cards!\n'
    print(s)

def read_rules():
    text = [] 
    fmt_text = []
    with open('rules.txt','r') as f:
        text = f.readlines()
    for line in text:
        if line[:3] == '###':
            line = line.replace('### ',f'{YELLOW}')
            line = line.replace('\n',f'{RESET}\n')
        # append line to formatted text
        fmt_text.append(line)
    new_text = ''.join(fmt_text)
    print(f'{new_text}')

def menu():
    def print_menu():
        s = '=== Main Menu ===\n\n'
        s += '[1] Start New Game\n'
        s += '[2] Read Game Rules\n'
        s += '[3] Adjust Game Settings\n'
        s += '\nEnter \'q\' to quit program\n'
        print(s)
    # main menu event loop
    while True:
        # print menu screen
        print_menu()
        # handle user prompt (menu selection)
        select = prompt_user('Enter a value (1-3): ', [1,2,3,'q'])
        # adjust game settings
        if select == 1:
            pass
        # read game rules
        elif select == 2:
            clear_screen()
            read_rules()
        # start new game
        elif select == 3:
            settings()
            clear_screen()
        # quit program
        elif select == 'q':
            clear_screen()
            break

def settings():
    global start_cash,min_bet,num_decks,num_players,dealer_stands
    # helper method
    def print_settings():
        global start_cash,min_bet,num_decks,num_players,dealer_stands
        clear_screen()
        s = '=== Game Settings ===\n\n'
        s += f'[1] Starting Cash: ${float(start_cash):.2f}\n'
        s += f'[2] Minimum Bet: ${float(min_bet):.2f}\n'
        s += f'[3] Number of Decks: {num_decks}\n'
        s += f'[4] Number of Players: {num_players}\n'
        s += f'[5] Dealer Stands at: {dealer_stands}\n'
        s += f'\nEnter \'q\' to return to Main Menu\n'
        print(s)
    # settings event loop
    while True:
        # print settings prompt
        print_settings()
        # handle user prompt
        select = prompt_user('Enter a value (1-4): ', [1,2,3,4,5,'q'])
        # adjust settings
        if select == 1:
            new_value = prompt_user('New starting cash: ')
            start_cash = new_value
        elif select == 2:
            new_value = prompt_user('New minimum bet: ')
            min_bet = new_value
        elif select == 3:
            new_value = prompt_user('New number of decks: ')
            num_decks = new_value
        elif select == 4:
            new_value = prompt_user('New number of players: ')
            num_players = new_value
        elif select == 5:
            new_value = prompt_user('New dealer stands at: ')
            dealer_stands = new_value
        # quit settings
        elif select == 'q':
            break

def prompt_user(prompt='text',values=[]):
    resp = input(prompt)
    if values != []:
        while resp not in values:
            if isinstance(values[0],int):
                try: 
                    resp = int(resp)
                    break
                except: resp = input(prompt)
            else: resp = input(prompt)
    else:
        while True:
            try:
                resp = int(resp)
                if resp < 0:
                    print('You must specify a positive value')
                    resp = input(prompt)
                else: break
            except: continue
    return resp

def main():
    print_banner()
    menu()
    '''
    starting_cash = 500
    num_decks = 8 
    num_players = 8
    players = []
    remove_players = []
    house = House(num_decks)
    for i in range(num_players):
        p = Player(500)
        players.append(p)
    print(f'{YELLOW}Dealing cards...{RESET}')
    for p in players:
        house.deal(p)
        p_hand = p.calc_hand()
        p_card_1 = p.hand[0][0]
        p_card_2 = p.hand[0][1]
        if p.alt_sum == 21:
            print(f'Player #{p.pid}: {p.hand} = {GREEN}BLACKJACK!{RESET}')
            remove_players.append(p)
        else:
            print(f'Player #{p.pid}: {p.hand} = {p.calc_hand()}')
        # check for splits or double
        if can_split(p_card_1,p_card_2):
            p.can_split = True
            print(f'{CYAN}Player #{p.pid} can split{RESET}')
        if can_double(p_card_1,p_card_2):
            p.can_double = True
            print(f'{CYAN}Player #{p.pid} can double{RESET}')
    # dealer's play
    house.deal(house)
    dealer_face_up_card = house.hand[0][0]
    print(f'Dealer has: [(\'{dealer_face_up_card}\', \'?\')] = {house.calc_hidden_hand()}')
    print(f'{PURPLE}Dealer actually has: {house.hand_sum}/{house.alt_sum}{RESET}')
    if is_ace(dealer_face_up_card):
        print(f'{CYAN}Dealer is offering insurance...{RESET}')
    # test hit
    print(f'{YELLOW}Testing hit...{RESET}')
    for p in players:
        if p not in remove_players:
            house.hit(p)
            p_hand = p.calc_hand()
            if p.hand_sum > 21:
                print(f'Player #{p.pid} {RED}busted!{RESET}')
            else:
                print(f'Player #{p.pid}: {p.hand} = {p_hand}')
    '''
    return

if __name__ == '__main__':
    main()
