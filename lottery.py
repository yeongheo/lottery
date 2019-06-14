import random


def menu():
    # Ask player for numbers
    user_numbers = get_player_numbers()

    # Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}. Yon won ${}".format(
        matched_numbers, 100 ** len(matched_numbers)))


# User can pick 6 numbers


def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    # Create a set of intergers from this number_csv
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set


# Lottery calculates 6 random numbers (between 1 and 50)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 50))
    return values


# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched


menu()