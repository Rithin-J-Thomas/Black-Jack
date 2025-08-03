import random

#both two lines is to clear the console and last calling 'clear()'
import os
clear = lambda: os.system('clear')

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
user_card = []
comp_card = []
game_over = True
comp_score_limit = True
restart_game = True


#This while loop is for restart the game if user needs
while restart_game is True:
    #loop is for picking first two cards
    for i in range(2):
        user_card_random = random.choice(cards)
        user_card.append(user_card_random)

    #loop is for picking first two cards
    for i in range(2):
        comp_card_random = random.choice(cards)
        comp_card.append(comp_card_random)

    #Taking sum of two cards if the sum is 21 game over who ever has 21 will win
    user_card_score = sum(user_card)
    comp_card_score = sum(comp_card)

    #showing first two cards of both players
    print(f"User's hand {user_card} score is {user_card_score} ")
    print(f"Dealer's hand [{comp_card[0]}] score is {comp_card[0]}\n")


    #setting a flag to check it is gameover
    while game_over != False:
        #checking if card is numbers gone more than 21
        if user_card_score > 21:
            print("'Bust' You Lose Dealer Won!!! ")
            game_over = False

        #checking user's card for score
        elif comp_card_score == 21:
            print("Blackjack You Lose Dealer Won!!!")
            game_over = False

        #checking computer's card for score
        elif user_card_score == 21:
            print("Blackjack You Won!!!")
            game_over = False

        else:
            #asking user for cards
            draw_card_option = input("Do you need any cards \"Yes\" or \"no\" \n".title())
            draw_card_option = draw_card_option.lower()
            if draw_card_option == "yes":
                draw_card = random.choice(cards)
                user_card.append(draw_card)
                user_card_score = sum(user_card)
                print(f"User's hand {user_card} score is {user_card_score}")


                #checking if the score is over 21
                user_card_score = sum(user_card)
                if user_card_score > 21:
                    print("'Bust' You Lose Dealer Won!!! ")
                    game_over = False
                elif user_card_score == 21:
                    print("Blackjack You Won!!!")
                    game_over = False
            else:
                print(f"your total score is {user_card_score}".title())
                game_over = False


    #drawing card for computer/dealer if card score is below 16
    while comp_score_limit != False:
        if comp_card_score < 16:
            comp_card_random = random.choice(cards)
            comp_card.append(comp_card_random)
            comp_card_score = sum(comp_card)
            print(comp_card)
            print(comp_card_score)

            if comp_card_score > 21:
                print("you win dealer has scored over 21".title())
                comp_score_limit = False
            elif comp_card_score == 21:
                print("Blackjack dealer won!!!".title())
                comp_score_limit = False
        else:
            comp_score_limit = False


    #printing out the final hand or score of both players
    print(f"\nyour score is {user_card_score}".title())
    print(f"Deal's score is {comp_card_score}".title())


    #comparing the scores from both players to decide win , loss or draw
    while game_over is False:
        if user_card_score > 21:
            print(f"you lost dealer won the match".title())
            game_over = True
        elif comp_card_score > 21:
            print(f"you win the match \" congrats\" ".title())
            game_over = True
        elif comp_card_score == user_card_score:
            print(f"\"PUSH\" it's a draw".title())
            game_over = True
        elif comp_card_score > user_card_score:
            print(f"you lost dealer has more points".title())
            game_over = True
        elif comp_card_score < user_card_score:
            print(f"you win the match \" congrats\" ".title())
            game_over = True



    restart_game = False

#asking user to restart the game or not
    restart = input("Do you need play again \"yes\" or \"no\" \n".title()).lower()
    if restart == "yes":
        restart_game = True
        user_card = []
        comp_card = []
        game_over = True
        comp_score_limit = True
        clear()
    else:
        clear()
        print("see you later".title())
        restart_game = False
