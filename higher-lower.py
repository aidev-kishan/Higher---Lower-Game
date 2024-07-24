from art import logo_1, logo_2
from game_data import data
from random import randint

def get_random_profile():
    """Returns a random profile from the database"""
    return randint(0,len(data) - 1)

def print_profiles(profile, label):
    """Print profile details."""
    print(f"{label}: {data[profile]['name']}, a {data[profile]['description']}, from {data[profile]['country']}")

def main():
    user_points = 0 
    is_game_over = False
    print(logo_1)
    random_profile_a = get_random_profile()
    random_profile_b = get_random_profile()
    while random_profile_a == random_profile_b:
        random_profile_b = get_random_profile()
    while not is_game_over:
        print(f"Your score : {user_points}")
        print_profiles(random_profile_a, "Compare A")
        print(logo_2)
        print_profiles(random_profile_b, "Against B")

        user_moves = input("Who has more followers on Instagram? Type 'A' or 'B' ").upper()

        if user_moves == "A" or user_moves == "B":

            if (user_moves == "A" and data[random_profile_a]['follower_count'] > data[random_profile_b]['follower_count']) or \
            (user_moves == "B" and data[random_profile_b]['follower_count']> data[random_profile_a]['follower_count']):
                user_points += 1
                print("You got it The right one ! \nguess again!") 

                if user_moves == "A":
                    random_profile_b = get_random_profile()
                    while random_profile_a == random_profile_b:
                        random_profile_b = get_random_profile()

                else:
                    random_profile_a = random_profile_b
                    random_profile_b = get_random_profile()
                    while random_profile_a == random_profile_b:
                        random_profile_b = get_random_profile()

            else:
                is_game_over = True

        else:
            print("Invalid input. Please type 'A' or 'B'")

        if is_game_over:
            print(f"Game over! Your Final score is: {user_points} ")

if __name__ == "__main__":
    main()