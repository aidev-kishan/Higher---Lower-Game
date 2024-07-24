# Higher---Lower-Game
Instagram Follower Comparison Game A text-based game where you guess which of two popular Instagram accounts has more followers. Features the top 50 accounts, tracks your score, and provides an educational and fun way to learn about popular Instagram personalities. Clone, run, and start guessing!

# Instagram Follower Comparison Game

This is a simple text-based game where you guess which of two popular Instagram accounts has more followers. The game features the top 50 Instagram accounts, and your goal is to accumulate as many correct guesses as possible before making a mistake.

## Features
- Compare the follower counts of the 50 most popular Instagram accounts.
- Simple and intuitive user interface.
- Tracks and displays your score throughout the game.
- Fun and educational way to learn about popular Instagram personalities.

## How to Play
1. When you start the game, you will see a randomly selected Instagram account (Profile A) and another randomly selected account (Profile B).
2. Your task is to guess which account has more followers.
3. Type 'A' if you think Profile A has more followers or 'B' if you think Profile B has more followers.
4. If you guess correctly, your score increases by one, and the game continues with Profile B becoming the new Profile A and a new Profile B being selected.
5. If you guess incorrectly, the game ends, and your final score is displayed.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/aidev-kishan/Higher---Lower-Game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd instagram-follower-comparison-game
   ```
3. Ensure you have Python installed. If not, download and install Python from [python.org](https://www.python.org/).
4. Run the game:
   ```sh
   python game.py
   ```

## Example Gameplay
```
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
Against B: Selena Gomez, a Singer and Actress, from USA

Who has more followers on Instagram? Type 'A' or 'B': A
You got it right! Guess again!

Your score: 1
Compare A: Selena Gomez, a Singer and Actress, from USA
Against B: Dwayne Johnson, an Actor and Wrestler, from USA

Who has more followers on Instagram? Type 'A' or 'B': B
Game over! Your final score is: 1
```

## Files in the Repository
- **game.py**: Main game logic.
- **art.py**: Contains ASCII art for the game.
- **game_data.py**: Contains data for the top 50 Instagram accounts.

## Contributing
Feel free to submit pull requests or issues if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License.
