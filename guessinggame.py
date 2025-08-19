import random
import time
import os

# For colorful text (works in most terminals)
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except:
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game banner
def banner():
    print(Fore.CYAN + Style.BRIGHT + """
   ██████╗ ██╗   ██╗███████╗███████╗██╗███████╗███╗   ██╗
  ██╔═══██╗██║   ██║██╔════╝██╔════╝██║██╔════╝████╗  ██║
  ██║   ██║██║   ██║█████╗  █████╗  ██║█████╗  ██╔██╗ ██║
  ██║▄▄ ██║██║   ██║██╔══╝  ██╔══╝  ██║██╔══╝  ██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║     ██║     ██║███████╗██║ ╚████║
   ╚══▀▀═╝  ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝
    """)
    print(Fore.YELLOW + "🎯 Welcome to the Ultimate Number Guessing Game 🎯\n")

# Difficulty settings
def choose_difficulty():
    print(Fore.MAGENTA + "Choose a difficulty level:")
    print("1. Easy (1-20, 6 attempts)")
    print("2. Medium (1-50, 8 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    
    while True:
        choice = input(Fore.CYAN + "Enter 1, 2, or 3: ")
        if choice == "1":
            return 20, 6
        elif choice == "2":
            return 50, 8
        elif choice == "3":
            return 100, 10
        else:
            print(Fore.RED + "⚠ Invalid choice, please select again.")

# Game logic
def play_game():
    clear_screen()
    banner()
    
    limit, attempts = choose_difficulty()
    secret = random.randint(1, limit)
    score = 100
    
    print(Fore.GREEN + f"\nI have chosen a number between 1 and {limit}.")
    print(f"You have {attempts} attempts. Let's go! 🚀\n")

    for attempt in range(1, attempts+1):
        try:
            guess = int(input(Fore.CYAN + f"Attempt {attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print(Fore.RED + "⚠ Please enter a valid number.")
            continue

        if guess == secret:
            print(Fore.GREEN + Style.BRIGHT + f"\n🎉 Congratulations! You guessed it in {attempt} attempts!")
            print(Fore.YELLOW + f"🏆 Your Score: {score}\n")
            break
        elif guess < secret:
            print(Fore.BLUE + "🔼 Too low! Try a higher number.")
        else:
            print(Fore.MAGENTA + "🔽 Too high! Try a lower number.")

        score -= 10  # Reduce score for each wrong attempt

    else:
        print(Fore.RED + Style.BRIGHT + f"\n❌ Game Over! The number was {secret}.")
        print(Fore.YELLOW + f"Your Score: {score}\n")

# Main loop
def main():
    while True:
        play_game()
        again = input(Fore.CYAN + "Do you want to play again? (y/n): ").lower()
        if again != "y":
            print(Fore.YELLOW + "\n👋 Thanks for playing! See you next time!")
            break
        clear_screen()

if __name__ == "__main__":
    main()
