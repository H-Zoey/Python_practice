# the blackjack game
'''import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:#总和大于21时，ace代表的11会变成1
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_cards, c_cards):
    if c_cards == 0:
        print("Opponent has blackjack! You lose!")
    elif u_cards == 0:
        print("You win with blackjack!")
    elif calculate_score(u_cards) > 21:
        print("You went over! You lose!")
    elif calculate_score(c_cards) > 21:
        print("Opponent went over! You win!")
    elif calculate_score(u_cards) == calculate_score(c_cards):
        print("Draw!")
    elif calculate_score(u_cards) > calculate_score(c_cards):
        print("You win!")
    else:
        print("You lose!")

def play_blackjack():
    user_card = []
    computer_card = []
    for whatever in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, card_score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        while computer_score != 0 and computer_score < 17:#computer总和小于17时会自动抽牌至总和大于17
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_or_stand == "y":
                    user_card.append(deal_card())
            else:
                print(f"Your final hand: {user_card}, final score: {user_score}")
                print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
                
                is_game_over = True
        compare(user_card, computer_card)

while input("Do you want to play blackjack? Type 'y' to start or 'n'.") == 'y':
    print("Start!")
    play_blackjack()
'''



#prime number
''''
def is_num_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_num_prime(73))
print(is_num_prime(75))'
'''



#the guess game
'''
import random

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
    if level == 'easy':
        attempt_chance = 10
    else:
        attempt_chance = 5
    return attempt_chance


def compare(answer, guess, attempt_chance):
    if guess < answer:
        print("Too low.\nGuess again.")
        return attempt_chance - 1
    elif guess > answer:
        print("Too high.\nGuess again.")
        return attempt_chance - 1
    else:
        print("You got this!")

def guess_number_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    correct_number = random.randint(1, 100)
    print(correct_number)
    guess_number = 0
    
    turns = set_difficulty() 

    while guess_number != correct_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess:"))
        turns = compare(correct_number, guess_number, turns)
        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return

guess_number_game()
'''


'''
import random
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 8])
'''



#Coffee Machine
'''
MENU = {
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18,}, "cost": 1.5}, 
    "latte": {"ingredients": {"water": 200, "milk": 150,"coffee": 24,}, "cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}   
}

original = {
    "Water": 300,  
    "Milk": 200, 
    "Coffee": 100, 
    "Money": 0
}



def check_report():
    for i in original:
        print(f"{i}: {original[i]}")

 
#check resources sufficient?
def check_resources():

    if original["Water"] - water_source < 0:
        print("Sorry there is not enough water.")
    elif original["Coffee"] - coffee_source < 0:
        print("Sorry there is not enough coffee.")
    elif original["Milk"] - milk_source <0:
        print("Sorry there is not enough milk.")

    if original["Water"] > water_source and original["Milk"] >milk_source and original["Coffee"] > coffee_source:
        original["Money"] += MENU[user_choice]["cost"]
        original["Water"] -= water_source
        original["Coffee"] -= coffee_source
        original["Milk"] -= milk_source
    
    #for i in original:
       # if i == "money":
       #     continue
       # else:
       #     if original[i] < MENU[user_choice]["ingredients"][i]:
       #         print(f"Sorry there is not enough {i}.")
       #     else:
       #         return True


def calcualte_coins(choice):
    print("Please insert coins.")
    sum_amount = int(input("How many quarters?")) * 0.25
    sum_amount += int(input("How many dimes?")) * 0.10
    sum_amount += int(input("How many nickles?")) * 0.05
    sum_amount += int(input("How many pennies?")) * 0.01
    
    if sum_amount > MENU[choice]["cost"]:
        change_amount = round(sum_amount - MENU[choice]["cost"],2)
        print(f"Here is {change_amount} in change.\nHere is your {choice}.")
    elif sum_amount == MENU[choice]["cost"]:
        print(f"Here is your {choice}.")
    else:
        print("Sorry that's not enough money. Money refunded.")

order_or_not = True
while order_or_not:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        check_report()
    elif user_choice == "off":
        print("Quit order.")
        order_or_not = False
    else:
        water_source =  MENU[user_choice]["ingredients"]["water"]
        coffee_source = MENU[user_choice]["ingredients"]["coffee"]
        milk_source = MENU[user_choice]["ingredients"]["milk"]

        check_resources()
        calcualte_coins(user_choice)
'''
