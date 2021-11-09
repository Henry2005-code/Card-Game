'''Driver for playing Henry's SweGG.'''

from player import card_generator, deal_single_card,print_user_manual, play

def main():
    '''Runs a full game of Henry's SweGG.'''
    print("Welcome to Henry's SweGG!!!")
    first_timer = input('Is this your first time playing Henrys SweGG (yes/no) : ')
    first_timer = first_timer.lower()
    if first_timer == 'yes':
        print('')
        user_manual = input('Do you want to read the user manual(yes/no): ')
        user_manual = user_manual.lower()
        if user_manual == 'yes':
            print('')
            print_user_manual()
            print('\n\n\n')
    else:
        print('')
        user_manual = input('Do you want to read the user manual(yes/no): ')
        user_manual = user_manual.lower()
        if user_manual == 'yes':
            print('')
            print_user_manual()
            print('\n\n\n')
    
    deck = []
    player_pouch = []
    comp_pouch = []
    base_cards = []
    space = [0]
    card_generator(deck)
    deal_single_card(base_cards, space , deck)
    
    # the base is variable is for the card at the top of the base cards which is the last element of the list
    base = base_cards[-1]
    
    for i in range(5):
        deal_single_card(player_pouch, space, deck)
        deal_single_card(comp_pouch, space, deck)
    
    continue_code = 1
    turn_decider = input("Do you want to go first? ")
    
    while continue_code:
        continue_code = play(turn_decider,player_pouch, comp_pouch, base, base_cards, deck)
        
if __name__ == "__main__":
    main()