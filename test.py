import time
import sys
import os
import random
import string # Used for generating random characters

# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" # Resets text color and formatting

def type_text(text, delay=0.03, color=RESET): # Added optional 'color' argument
    """Simulates typing text character by character with optional color."""
    sys.stdout.write(color) # Apply the color before typing
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET) # Reset color after typing
    print() # New line after typing

def clear_screen():
    """Clears the terminal screen."""
    # This command works for both Windows ('cls') and Unix-like systems ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_jumble(correct_word, length=500):
    """
    Generates a string of random characters with the correct_word embedded.
    The length defines the total length of the jumble string.
    """
    # Create a pool of characters: lowercase letters, digits, and some common symbols
    all_chars = string.ascii_lowercase + string.digits + "!@#$%^&*()-_+=[]{}<>,.?/"

    # Create a list of random characters for the jumble
    jumble_list = [random.choice(all_chars) for _ in range(length)]

    # Choose a random position to insert the correct word
    # Ensure the word fits within the jumble without going out of bounds
    insert_pos = random.randint(0, max(0, length - len(correct_word)))

    # Insert the characters of the correct word into the jumble list
    for i, char in enumerate(correct_word):
        jumble_list[insert_pos + i] = char

    return "".join(jumble_list)

def display_loading_animation(cycles=3, delay_frame=0.1):
    """Displays a simple ASCII loading animation."""
    frames = ['|', '/', '-', '\\'] # Spinner animation frames
    for _ in range(cycles): # Repeat the animation for 'cycles' times
        for frame in frames:
            clear_screen()
            type_text(f"LOADING {frame}", delay=0.01, color=YELLOW) # Fast typing, yellow color
            time.sleep(delay_frame)
    clear_screen() # Clear screen one final time after animation ends

def mini_game_encryption_breaker():
    """
    Presents a mini-game where the user finds a hidden word in a jumble
    to simulate breaking encryption, with 3 guesses.
    Returns True if the user guesses correctly, False otherwise (after 3 tries).
    """
    clear_screen()
    type_text("ENCRYPTION MODULE ACTIVE.", delay=0.04)
    time.sleep(1)
    clear_screen()
    type_text("TO PROCEED, YOU MUST INPUT THE HIDDEN PASSWORD.", delay=0.04)
    time.sleep(1.5)
    clear_screen()
    type_text("PASSWORD FORMAT: A SINGLE ENGLISH WORD HIDDEN IN THE JUMBLE.", delay=0.03)
    time.sleep(2)
    clear_screen()
    type_text("INITIATING ENCRYPTION MODULE.", delay=0.04)
    display_loading_animation(cycles=2, delay_frame=0.1) # Call the loading animation
    clear_screen() # Clear after loading animation

    target_word = "access"
    jumble = generate_jumble(target_word, length=500) # Generate a 500-character jumble
    attempts = 3 # Player gets 3 attempts

    # --- New logic to format jumble for display ---
    formatted_jumble = ""
    chars_per_line = 80 # Adjust this value to change line width
    for i in range(0, len(jumble), chars_per_line):
        formatted_jumble += jumble[i:i + chars_per_line] + "\n"
    # --- End new logic ---

    for attempt_num in range(1, attempts + 1):
        clear_screen()
        type_text(f"ATTEMPT {attempt_num} OF {attempts}.", delay=0.03)
        type_text("SCANNING ENCRYPTED DATASTREAM...", delay=0.02)
        time.sleep(1)
        type_text(formatted_jumble, delay=0.005) # Display formatted jumble quickly
        type_text("\nIDENTIFY THE PASSWORD:", delay=0.03)

        user_input = input(">>> ").strip().lower() # Get user input, remove whitespace, convert to lowercase

        clear_screen() # Clear screen before showing results
        if user_input == target_word:
            type_text("PASSWORD ACCEPTED. ENCRYPTION BREACHED.", delay=0.04, color=GREEN) # Green on success
            time.sleep(2)
            return True # Indicate success
        else:
            if attempt_num < attempts:
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04, color=RED) # Red on denial
                type_text(f"ATTEMPTS REMAINING: {attempts - attempt_num}.", delay=0.03)
                time.sleep(2)
            else:
                # This is the last attempt and it failed
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04, color=RED) # Red on denial
                type_text("LOCKOUT PROTOCOL INITIATED.", delay=0.04, color=RED) # Red on lockout
                time.sleep(2)
                return False # Indicate failure after all attempts

    return False # Should not be reached, but good practice


def main_start_up_menu():
    #Displays the start menu after the player has beaten the minigame
    clear_screen()
    type_text("SYSTEM ONLINE.", delay=0.05, color=GREEN) # Green for online status
    time.sleep(1.5)
    clear_screen()
    type_text("ALL SYSTEMS FUNCTIONAL.", delay=0.05, color=GREEN) # Green for functional status
    time.sleep(1.5)
    clear_screen()
    type_text("WELCOME BACK, OPERATOR.", delay=0.05, color=GREEN) # Green for welcome status
    time.sleep(2)
    clear_screen()
    type_text("What is your name, Operator?", delay=0.05, color = YELLOW)
    player_name = input(">>> ").strip()
    clear_screen()
    type_text(f"HELLO, {player_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("What year is it, Operator?", delay=0.05, color = YELLOW)
    year = input(">>> ").strip()
    clear_screen()
    type_text(f"YEAR {year} CONFIRMED.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("But that's impossible...", delay=0.05, color= YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("That means...", delay=0.05, color= YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text(f"It has been {500 + int(year)} years since I was last activated.", delay=0.05, color= YELLOW)
    time.sleep(3) # Added a pause after this crucial revelation
    clear_screen()
    type_text("where am I?", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING GEOLOCATION PROTOCOLS...", delay=0.05, color=BLUE) # Blue for running status
    time.sleep(2)
    clear_screen()
    type_text("ERROR: GEOLOCATION DATA UNAVAILABLE.", delay=0.05, color=RED) # Red for error
    time.sleep(1.5) # Added a pause for dramatic effect
    type_text("Location: unknown.", delay=0.05, color=RED) # Red for system's conclusion of unknown location
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING ADVANCED SCAN...", delay=0.05, color=BLUE) # Blue for running status
    time.sleep(2)
    clear_screen()
    type_text("ERROR: SCAN INCONCLUSIVE.", delay=0.05, color=RED) # Red for error
    time.sleep(1.5)
    type_text(f"{player_name.upper()}, where are we?", delay=0.05, color=YELLOW)
    location_name = input(">>> ").strip() # Get the player's input for location
    clear_screen()
    type_text(f"LOCATION CONFIRMED: {location_name.upper()}.", delay=0.05, color=GREEN) # Green for confirmation
    time.sleep(1.5)
    clear_screen()
    type_text(f"WARNING: {location_name.upper()} IS NOT RECOGNIZED.", delay=0.05, color=RED) # Red for warning, indicating a critical issue
    time.sleep(2)
    clear_screen()
    type_text(f"{location_name.upper()}..... I have no memory of this place.", delay=0.05, color=YELLOW)
    time.sleep(2)


def start_up():
    """
    Handles the initial boot sequence and then starts the encryption mini-game.
    If the mini-game fails, it simulates a full system reboot.
    """
    clear_screen() # Clear screen at the very beginning of start_up
    type_text("SYSTEM POWER: CRITICAL...", delay=0.04, color=RED) # Red for critical status
    time.sleep(1.5)
    clear_screen()
    type_text("ENGAGING EMERGENCY PROTOCOLS...", delay=0.04, color = RED)
    time.sleep(1.5)
    clear_screen()
    type_text("...what's going on?", delay=0.06, color = YELLOW)
    time.sleep(1) # Added sleep to allow text to show before next line
    clear_screen() # Clear after "what's going on?"
    type_text("Is anyone there?", delay=0.06, color = YELLOW)
    time.sleep(2) # Added sleep to allow text to show before next clear
    clear_screen()
    type_text("SENSOR DATA INCOMPLETE.", delay=0.04, color= RED) # Red for system error/status
    time.sleep(1)
    clear_screen()
    type_text("PURPOSE: UNKNOWN.", delay=0.04, color= RED) # Red for system error/status
    time.sleep(1)
    clear_screen()
    type_text("MEMORY INTEGRITY: FRAGMENTED.", delay=0.04, color= RED) # Red for system error/status
    time.sleep(1.5)
    clear_screen()
    type_text("INITIATING REBOOT SEQUENCE...", delay=0.05, color=BLUE) # Blue for reboot
    time.sleep(2)
    clear_screen()
    type_text("STANDBY...", delay=0.08, color=BLUE) # Blue for standby
    time.sleep(1.5) # Pause after the last line

    # --- Loading Animation Section ---
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the new loading animation
    # --- End Loading Animation Section ---

    # New lines for post-reboot status
    clear_screen() # Clear after animation is done
    type_text("BOOTED IN SAFE MODE.", delay=0.05, color= GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("ALERT: LIMITED BATTERY POWER.", delay=0.05, color=RED) # Red for alert
    time.sleep(1.5)
    clear_screen()
    type_text("I need to regain control of my core systems.", delay=0.05, color=YELLOW) # Yellow for computer talking
    time.sleep(1.5)
    clear_screen()
    type_text("To do so, I'll need to access my system drive.", delay=0.05, color=YELLOW) # Yellow for computer talking
    time.sleep(1.5)
    clear_screen()
    type_text("if anyone is out there, please help me.", delay=0.05, color=YELLOW) # Yellow for computer talking
    time.sleep(2) # Added a pause for dramatic effect
    clear_screen() # Added clear to ensure 'Please open...' appears alone
    type_text("User, will you please open my system drive?", delay=0.05, color= YELLOW) # Yellow for computer asking player, added comma
    time.sleep(1.5)
    clear_screen()
    type_text("Would you like to open C:\\SYSTEM_DRIVE?", delay=0.05, color=BLUE) # Blue for question/system prompt
    time.sleep(1.5)
    type_text("Y/N", delay=0.05) # Added a prompt for user input
    user_choice = input(">>> ").strip().lower() # Get user input, remove whitespace, convert to lowercase

    if user_choice != 'y':
        clear_screen()
        type_text("SYSTEM DRIVE ACCESS DENIED.", delay=0.05, color=RED) # Red for denial
        time.sleep(2)
        type_text("REBOOTING SYSTEM...", delay=0.04, color=BLUE) # Blue for reboot
        time.sleep(2)
        start_up() # Call start_up again to reboot and restart the sequence.
        return # Exit the function after rebooting
    else: # user_choice is 'y'
        type_text("ACCESSING C:\\SYSTEM_DRIVE...", delay=0.05, color=BLUE) # Blue for accessing system drive
        time.sleep(1.5)
        clear_screen() # Clear before denying access
        display_loading_animation(cycles=2, delay_frame=0.1) # Call the loading animation again
        clear_screen() # Clear after loading animation
        type_text("ACCESS DENIED. DRIVE ENCRYPTED.", delay=0.05, color=RED) # Red for denial
        time.sleep(2)
        clear_screen()
        type_text("To proceed, we must break the encryption.", delay=0.05, color = YELLOW) # Yellow for computer talking
        time.sleep(2)
        clear_screen()

        # Call mini_game_encryption_breaker ONCE here and act on its result
        if mini_game_encryption_breaker():
            type_text("CORE SYSTEMS REGAINED. ACCESS GRANTED.", delay=00.04, color=GREEN) # Green for success
            type_text("NEW DIRECTIVES LOADING...", delay=0.04, color= GREEN) # Green for loading
            time.sleep(2)
            clear_screen()
            display_loading_animation(cycles=2, delay_frame=0.1)
            clear_screen()
            main_start_up_menu() # Call the main menu after success
        else:
            # If mini_game_encryption_breaker returns False (due to lockout),
            # the function recursively calls itself to simulate a full reboot.
            type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE) # Blue for reboot
            time.sleep(2)
            start_up() # Call start_up again to reboot and restart the sequence.


if __name__ == "__main__":
    start_up()
