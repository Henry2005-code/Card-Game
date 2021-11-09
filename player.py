import random
import time


def print_user_manual():
  
    """
    Shows the user manual of the HENRYS SWEGG to the user
    """
    file = open("README.md", "r")
    print(file.read())
  

def card_generator(deck):
    """
    This function generates the deck of cards. The deck of cards is a 2d-list that has each card as a list on its own.
    
    Args:
        deck: the deck contains every other cards in the game that are not in the base cards, in the players pouch or in the computers pouch.
    
    Returns:
        None.
    """
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    suites = ['★', '◍', '■', '▲', '✚']
    for number in numbers:
        for suite in suites:
            deck.append([number, suite])
    # add the swegg cards
    deck.append(['1', 'SW'])
    deck.append(['2', 'SW'])
    deck.append(['3', 'SW'])
    deck.append(['4', 'SW'])
    

def deal_single_card(pouch, opp_pouch, deck):
    """
    This function deals a single random card from the deck and adds it to either the computer pouch or the user pouch.
    
    Args:
        pouch: either the player's pouch or computer's pouch
        deck: the deck contains every other cards in the game that are not in the base cards, in the players pouch or in the computers pouch.
    
    Returns:
        None.
    """
    if not empty_deck(deck):
        card = random.choice(deck)
        pouch.append(card)
        deck.remove(card)
    else:
        end_of_game(pouch, opp_pouch, deck)

def display(player_pouch, comp_pouch, base):
    print("-------------------")
    print("BASE -->  |  " + base[0] + '-' + base[1] + "  |")
    print("-------------------")
    print()
    print("Number of Cards in opponent's pouch: "+ str(len(comp_pouch)))
    print("----------")
    print("Your Cards")
    print("----------")
    for i, card in enumerate(player_pouch):
        print("CARD " + str(i + 1) + " -->  |  "+ card[0] + '-' + card[1] + "  |")


def play_card(pouch, opp_pouch, card, base_cards, deck):
    """
    This function removes a card from the user or computer pouch and adds it to the base card list and the card becomes the new base card.
    
    Args:
        pouch: either the player's pouch or computer's pouch
        deck: the deck is a list that contains every other cards in the game that are not in the base cards, in the players pouch or in the computers pouch.
        base_cards: the base cards is a list of cards that contains a random card from the deck 
    
    Returns:
        None.

    """
    special_card(card, pouch, opp_pouch, deck)
    pouch.remove(card)
    base_cards.append(card)
    count_card()


def comp_play(pouch, opp_pouch, base, base_cards, deck):
    prev = base
    """
    This function plays a card from the computer's pouch if the card has similar parts with the current base card.
    
    Args:
        pouch: computer's pouch that contains its cards
        deck: the deck is a list that contains every other cards in the game that are not in the base cards, in the players pouch or in the computers pouch.
        base_cards: the base cards is a list of cards that contains a random card from the deck 
        base: The most recent card added to the base cards list and it now serves as the base card to be played upon.
    Returns:
        None.
    """
    
    for card in pouch:
        if card[0] == base[0] or card[1] == base[1]:
            play_card(pouch, opp_pouch, card, base_cards, deck)
            base = base_cards[-1]
            time.sleep(0.5)
            print("-------------------")
            print("COMPUTER PLAYED -->  |  " + base[0] + '-' + base[1] + "  |")
            print("-------------------")
            time.sleep(0.5)
            comp_play(pouch, opp_pouch, base, base_cards, deck)
            break
   
    for card in pouch:
        if card[1] == 'SW':
            play_card(pouch, opp_pouch, card, base_cards, deck)
            base = base_cards[-1]            
            print("-------------------")
            print("COMPUTER PLAYED -->  |  " + base[0] + '-' + base[1] + "  |")
            print("-------------------")
            time.sleep(0.5)
            break
    if base[1] == 'SW':
        try:
            play_card(pouch, opp_pouch, random.choice(pouch), base_cards, deck)
            base = base_cards[-1]
            print("-------------------")
            print("COMPUTER PLAYED -->  |  " + base[0] + '-' + base[1] + "  |")
            print("-------------------")
            time.sleep(0.5)
        except:
            pass
    if count == 0:
        print()
        print("Computer drew a card")
        print()
        deal_single_card(pouch, opp_pouch, deck)
        return()
    base = base_cards[-1]
    if prev == base:
        return()
    comp_play(pouch, opp_pouch, base, base_cards, deck)

def user_play(pouch, opp_pouch, base, base_cards, deck):
    display(pouch, opp_pouch, base)
    """
    This function allows the user to play a card from his card depending on the base card and the number of the cards in the user_pouch.
     Args:
        pouch: a list which is the player's pouch that contains the users cards
        deck: the deck is a list that contains every other cards in the game that are not in the base cards, in the players pouch or in the computers pouch.
        base_cards: the base cards is a list of cards that contains a random card from the deck 
        base: The most recent card added to the base cards list and it now serves as the base card to be played upon.
    Returns:
        None.
    """
    print()
    print("Type the position of the card you want to play (1,2,...). Put 0 to draw a card")
    try:
        choice = int(input("--> "))
        if choice == 0:
            if count == 0:
                deal_single_card(pouch, opp_pouch, deck)
                return()
            else:
                return()
        # the user plays zero to draw a new card from the deck
        elif pouch[choice-1][1] =='SW':
            play_card(pouch, opp_pouch, pouch[choice-1], base_cards, deck)
        elif base[1] == 'SW':
            play_card(pouch, opp_pouch, pouch[choice-1], base_cards, deck)
        elif pouch[choice-1][0] != base[0] and pouch[choice-1][1] != base[1]:
            print("That Card Cannot be played")
        else:
            play_card(pouch, opp_pouch, pouch[choice-1], base_cards, deck)
        base = base_cards[-1] 
        user_play(pouch, opp_pouch, base, base_cards, deck)
    except:
        print("That Card Cannot be played")
        user_play(pouch, opp_pouch, base, base_cards, deck)


def end_of_game(player_pouch, comp_pouch, deck):
    """
    This function determines who wins after the game ends.
    """
    if len(player_pouch) == 0:
        print("You Win!")
        return 1
    elif len(comp_pouch) == 0:
        print("You Lose!")
        return 2
    elif len(deck) == 0:
        if len(player_pouch) > len(comp_pouch):
            print("Deck Exhausted")
            print("You Lose!")
            return 2
        elif len(comp_pouch) > len(player_pouch):
            print("Deck Exhausted")
            print("You Win!")
            return 1
        elif len(comp_pouch) == len(player_pouch):
            print("Deck Exhausted")
            print("You Tie!")
            return 3
    else:
        return 0

def special_card(card, current_pouch, opp_pouch, deck):
    """
    This function contains the special cards.
    """
    try:
        if card[0] == '2':
            print("PICK TWO")
            deal_single_card(opp_pouch, current_pouch, deck)
            deal_single_card(opp_pouch, current_pouch, deck)
        elif card[0] == '5':
            print("PICK THREE")
            deal_single_card(opp_pouch, current_pouch, deck)
            deal_single_card(opp_pouch, current_pouch, deck)
            deal_single_card(opp_pouch, current_pouch, deck)
        elif card[0] == '10':
            print("GENERAL MARKET")
            deal_single_card(opp_pouch, current_pouch, deck)
            deal_single_card(current_pouch, opp_pouch, deck)
    except:
        pass

def refresh():
    global count
    count = 0

def count_card():
    global count
    count += 1

def play(turn_decider,player_pouch, comp_pouch, base, base_cards, deck):
    if turn_decider == "yes":    
        refresh()
        base = base_cards[-1]
        user_play(player_pouch, comp_pouch, base, base_cards, deck)
        refresh()
        base = base_cards[-1]
        comp_play(comp_pouch, player_pouch, base, base_cards, deck)
        continue_code = not end_of_game(player_pouch, comp_pouch, deck)
        print()
        print()
        print()
    else:   
        refresh()
        base = base_cards[-1]
        comp_play(comp_pouch, player_pouch, base, base_cards, deck)
        refresh()
        base = base_cards[-1]
        user_play(player_pouch, comp_pouch, base, base_cards, deck)
        continue_code = not end_of_game(player_pouch, comp_pouch, deck)
        print()
        print()
        print()
    return continue_code

def empty_deck(deck):
    return len(deck) == 0