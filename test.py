from art import logo_1, logo_2
from game_data import data
from random import randint

def get_random_profile():
    """Return a random profile from the data."""
    return randint(0, len(data) - 1)

def print_profile(profile, label):
    """Print profile details."""
    print(f"Compare {label}: {data[profile]['name']}, a {data[profile]['description']}, from {data[profile]['country']}")

def main():
    user_points = 0
    is_game_over = False

    print(logo_1)

    random_number_1 = get_random_profile()
    random_number_2 = get_random_profile()
    while random_number_1 == random_number_2:
        random_number_2 = get_random_profile()

    while not is_game_over:
        print(f"Your score is: {user_points}")
        print_profile(random_number_1, "A")
        print(logo_2)
        print_profile(random_number_2, "B")

        user_move = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_move == "A" or user_move == "B":
            if (user_move == "A" and data[random_number_1]['follower_count'] > data[random_number_2]['follower_count']) or \
               (user_move == "B" and data[random_number_2]['follower_count'] > data[random_number_1]['follower_count']):
                user_points += 1
                print("You got the right one! Guess again.")
                if user_move == "A":
                    random_number_2 = get_random_profile()
                    while random_number_1 == random_number_2:
                        random_number_2 = get_random_profile()
                else:
                    random_number_1 = random_number_2
                    random_number_2 = get_random_profile()
                    while random_number_1 == random_number_2:
                        random_number_2 = get_random_profile()
            else:
                is_game_over = True
        else:
            print("Invalid input. Please type 'A' or 'B'.")

        if is_game_over:
            print(f"Game over! Your final score is: {user_points}")

if __name__ == "__main__":
    main()

# user_points = 0
# is_game_over = False

# print(logo_1)

# random_number_1 = randint(0,49)
# random_number_2 = randint(0,49)
# while random_number_1 == random_number_2:
#     random_number_2 = randint(0,49)

# while not is_game_over:
#     print(f"Your score is : {user_points}")
#     print(f"Compare A: {data[random_number_1]['name']}, a {data[random_number_1]['description']} , from {data[random_number_1]['country']}")
#     print(logo_2)
#     print(f"Compare B: {data[random_number_2]['name']}, a {data[random_number_2]['description']} , from {data[random_number_2]['country']}")

#     user_move = input("Who has more followers? Type 'A' or 'B': >> ").upper()

#     if user_move == "A":
#         if data[random_number_1]['follower_count'] > data[random_number_2]['follower_count']:
#             user_points += 1
#             print("You Got The Right One. \nguess again.")
#             random_number_2 = randint(0,49)
#             while random_number_1 == random_number_2:
#                 random_number_2 = randint(0,49)
#         else: 
#             is_game_over = True
#     elif user_move == "B":
#         if data[random_number_2]['follower_count'] > data[random_number_1]['follower_count']:
#             user_points += 1
#             random_number_1 = random_number_2
#             random_number_2 = randint(0,49)
#             while random_number_1 == random_number_2:
#                 random_number_2 = randint(0,49)
#             print("You Got The Right One. \nguess again.")
#         else:
#             is_game_over = True
#     if is_game_over:
#         print(f"Your finel score is : {user_points}")
