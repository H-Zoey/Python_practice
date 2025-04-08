#-*- coding: utf-8 -*-

#print("Hello " + input("What is your name?"))

#print(len(input("What is your name?")))

#变量交换
'''glass1 = "milk"
glass2 = "juice"
name = glass1
glass1 = glass2
glass2 = name
print(glass1)'''

#str vs int
'''print("123"+"456")
print(123 + 456)
print(6 / 3)
print(6 // 3)'''

#calculator
'''print("Welcome to the tip calculator!")
total_amount = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give?10, 12, or 15?"))
people_numbers = int(input("How many people to split the bill?"))
bill_per_person = round(total_amount * (1 + tip / 100) / people_numbers,2)
print(f"Each person should pay: {bill_per_person}")'''

#treasure
'''print("Welcome to Treasure Island./nYour mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go?\n"    
"Type \"left\" or \"right\"").lower()

if direction == "left":
    lake_approach = input("You've come to a lake. There is an island in the middle of the lake.\n" 
    "Type 'wait' to wait for a boat.Type 'swim' to swim across.").lower()
    if lake_approach == "wait":
        color = input("You've found boxes. Which one do you choose?\n" 
        "Type 'yellow' or 'green' or 'blue'.").lower()
        if color == "yellow":
            print("You Win!")
        elif color == "green":
            print("Game Over!")
        elif color == "blue":
            print("Game Over!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
elif direction == "right":
    print("Game Over!")'''

#nested list
'''list1 = ["a" , "b" , "c"]
list2 = ["d" , "e" , "f"]
list3 = [list1 , list2]
print(list3)
print(list3[1][1])'''

#Rock, Paper, Scissors Game
'''import random 

game_choice = ['Rock', 'Paper', 'Scissors']
player_number = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors'))
print(f'Your choice is: {game_choice[player_number]}')
#print('Your choice is: ' + game_choice[player_number]) 可替换66行
number_computer = random.randint(0, 2)
print(f"Computer's choice is: {game_choice[number_computer]}")
if player_number >= 3 or player_number <= 0:
    print('You typed an invalid number. You lose!')
elif player_number == 2 and number_computer == 0:
    print('You lose!')
elif player_number > number_computer:
    print('You win!')
elif player_number == number_computer:
    print("It's a draw!")
elif player_number == 0 and number_computer == 2:
    print('You win!')
elif player_number < number_computer:
    print('You lose!')'''

#寻找最大值
'''scores = [23,87,43,98,67]

max_score = 23
for score in scores:
    if score > max_score:
        max_score = score

print(max_score)'''

#在1到100中找到能被3或5整除的数
'''for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0 and number % 5 != 0:
        print('Fizz')
    elif number % 3 != 0 and number % 5 == 0:   
        print('Buzz')
    else:
        print(number)'''

#PyPassword Genertator
'''import random
letters = ['a','b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))

Password = ''
for word in range(1, nr_letters + 1):
    Password += random.choice(letters)
for word in range(1, nr_numbers + 1):
    Password += random.choice(numbers)
for word in range(1, nr_symbols + 1):
    Password += random.choice(symbols)

Password_random = ''
for word in range(1, nr_letters + nr_numbers + nr_symbols + 1):
    Password_random += random.choice(Password)
print(Password_random)'''


#Guess word
'''import random
word_list = ['aardvasrk', 'baboon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
temp_display = []
while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            temp_display.append(letter)
        elif letter in temp_display:
            display += letter
        else:
            display += "_"
    #display = display 这里的问题是不知道如何刷新已经有变化的display
    #解决方式：创建一个列表来临时储存更新后的字母
    print(display)
    print(temp_display)
    if "_" not in display:
        game_over = True
        print("You Win!")'''



# def

'''def greet():
    print("hello")
    print("caesar cipher")
    print("today is a completely new day.")
greet()'''

'''def greet_with_name(name):
    print(f"hello {name}")
    print(f"caeser cipher {name}")
greet_with_name("carrie")'''

'''#Functions with more than 1 input
def greet_with(name,location):
    print(f"hello {name}")
    print(f"Is weather good in {location}")
greet_with("Carrie","Shanghai")
可以按照顺序写parameter，也可以指定parameter，
eg. greet_with("Carrie","Shanghai")=greet_with(name = "Carrie", location = "Shanghai")'''

   
'''def calculate_love_score(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)
    for letter in list(name1_list):
        if letter in "TRUE" or "LOVE":
            occur_time = name1_list.count(letter)
            print(f"{letter} occurs {occur_time} times.")

calculate_love_score("ANGELA", "CARRIE")'''

'''target1 = list("true")
target2 = list("love")

def calculate_love_score(name1, name2):
    occur_time_for1 = 0
    occur_time_for2 = 0
    name1 = list(name1.lower())
    name2 = list(name2.lower())
    for letter in target1:
        if letter in name1:
            occur_time1 = name1.count(letter)
            occur_time_for1 += occur_time1
            print(f"{letter} occurs {occur_time1} times.")
        elif letter in name2:
            occur_time2 = name2.count(letter)
            occur_time_for1 += occur_time2
            print(f"{letter} occurs {occur_time2} times.")
        elif letter not in name1 and name2:
            print(f"{letter} occurs 0 times.")
    print(f"total1 = {occur_time_for1}")

    for letter in target2:
        if letter in name1:
            occur_time1 = name1.count(letter)
            occur_time_for2 += occur_time1
            print(f"{letter} occurs {occur_time1} times.")
        elif letter in name2:
            occur_time2 = name2.count(letter)
            occur_time_for2 += occur_time2
            print(f"{letter} occurs {occur_time2} times.")
        elif letter not in name1 and name2:
            print(f"{letter} occurs 0 times.")
    print(f"total2 = {occur_time_for2}")
    print("love score = " + str(occur_time_for1) + str(occur_time_for2))

calculate_love_score("Kanye West", "Kim Kardashian")'''
    


#caeser cipher

'''alphabet = ['a','b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        if shifted_position > 25:
            new_letter = alphabet[shifted_position - 26]
        else:
            new_letter = alphabet[shifted_position]
        #更简洁的写法是shifted_position %= len(alphabet)，得到余数
        cipher_text += new_letter
    print("Here is the encoded result: " + cipher_text)

def decrypt(original_text, shift_amount):
    decode_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        new_letter = alphabet[shifted_position]
        decode_text += new_letter
    print("Here is the encoded result: " + decode_text)

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            new_letter = alphabet[shifted_position]
            output_text += new_letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    caeser(text, shift, direction)
    continue_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if continue_or_not == "no":
        should_continue = False
        print("Goodbye!")'''



#the secret auction
'''def find_highest_winner(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

#max_price = max(name_price.values())
#for name in name_price:
#    if name_price[name] == max_price:
#         print(f"{name} wins!") #找最大值的简便写法1
# or max_name = max(name_price, key = name_price.get)#找最大值的简便写法2

name_price = {}
start_or_end = True
while start_or_end:
    name = input("What is your name:")
    price = int(input("What is your bid:"))
    name_price[name] = price
    
    other_person = input("Are there other users want to bid? Please type 'yes' or'no'.").lower()
    if other_person == "no":
        start_or_end = False
        find_highest_winner(name_price)
    elif other_person == "yes":
        print("\n" * 20) #clean the screen to keep secret'''



# the calculator project

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print("This is a new calculation.")
    should_continue = True
    num1 = float(input("What is the first number?"))

    while should_continue:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input(" Pick an operation:")
        num2 = float(input("What is the next number?"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.").lower()
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()


    
   
        



