import random
import json

# Options for white balls and red balls
white_possibilities = list(range(1, 70))
red_possibilities = list(range(1, 27))

# how many tickets we want to buy each time there is a drawing
tickets_per_drawing = 100

# how many drawings we want to simulate
num_drawings = 15600

total_spent = 0
earnings = 0


# contant to keep track of how many times we have hit each category of winning
times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0,
}

def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0

    # access the whites for both dictionaries
    # since these are sets we can perform intersection
    # we want to know how many matches so we use length

    whites_matches = len(my_numbers['whites'].intersection(winning_numbers['whites']))
    power_match = my_numbers['red'] == winning_numbers['red']

    if whites_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won['5+P'] += 1
        else:
            win_amt = 1_000_000
            times_won['5'] += 1
    elif whites_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won['4+P'] += 1
        else:
            win_amt = 100
            times_won['4'] += 1
    elif whites_matches == 3:
        if power_match:
            win_amt = 100
            times_won['3+P'] += 1
        else:
            win_amt = 7
            times_won['3'] += 1
    elif whites_matches == 2 and power_match:
        win_amt = 7
        times_won['2+P'] += 1
    elif whites_matches == 1 and power_match:
        win_amt = 4
        times_won['1+P'] += 1
    elif power_match:
        win_amt = 4
        times_won['P'] += 1
    else:
        times_won['0'] += 1

    return win_amt


for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibilities, k=5)) # 5 samples from the white list
    red_drawing = random.choice(red_possibilities)

    winning_numbers = {
        'whites': white_drawing,
        'red': red_drawing
    }

    for ticket in range(tickets_per_drawing):
        total_spent += 2 # each ticket is $2
        my_whites = set(random.sample(white_possibilities, k=5))
        my_red = random.choice(red_possibilities)

        my_numbers = {
        'whites': my_whites,
        'red': my_red
        }

        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt

print(f'Spent: ${total_spent}')
print(f'Earnings: ${earnings}')

# good way to print dictionary
print(json.dumps(times_won, indent=2))