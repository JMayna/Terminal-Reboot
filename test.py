import time
import sys
import os
import random
import string # Used for generating random characters

def type_text(text, delay=0.03):
    """Simulates typing text character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
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

    target_word = "access"
    jumble = generate_jumble(target_word, length=500) # Generate an 500-character jumble
    attempts = 3 # Player gets 3 attempts

    for attempt_num in range(1, attempts + 1):
        clear_screen()
        type_text(f"ATTEMPT {attempt_num} OF {attempts}", delay=0.03)
        type_text("SCANNING ENCRYPTED DATASTREAM...", delay=0.02)
        time.sleep(1)
        type_text(jumble, delay=0.005) # Display jumble quickly
        type_text("\nIDENTIFY THE PASSWORD:", delay=0.03)

        user_input = input(">>> ").strip().lower() # Get user input, remove whitespace, convert to lowercase

        clear_screen() # Clear screen before showing results
        if user_input == target_word:
            type_text("PASSWORD ACCEPTED. ENCRYPTION BREACHED.", delay=0.04)
            time.sleep(2)
            return True # Indicate success
        else:
            if attempt_num < attempts:
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04)
                type_text(f"ATTEMPTS REMAINING: {attempts - attempt_num}", delay=0.03)
                time.sleep(2)
            else:
                # This is the last attempt and it failed
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04)
                type_text("LOCKOUT PROTOCOL INITIATED.", delay=0.04)
                time.sleep(2)
                return False # Indicate failure after all attempts

    return False # Should not be reached, but good practice


def main_start_up_menu():
    #Displays the start menu after the player has beaten the minigame
    clear_screen()
    type_text("SYSTEM ONLINE.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("ALL SYSTEMS FUNCTIONAL.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("WELCOME BACK, OPERATOR.", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text("WHAT IS YOUR NAME OPERATOR?", delay=0.05)
    player_name = input(">>> ").strip()
    clear_screen()
    type_text(f"HELLO, {player_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("What year is it Operator?", delay=0.05)
    year = input(">>> ").strip()
    clear_screen()
    type_text(f"YEAR {year} CONFIRMED.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("But that's impossible ...", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text("that means...", delay=0.05) # Added delay here for consistency
    time.sleep(1.5)
    clear_screen()
    type_text(f"It has been, {500 + int(year)} years, since I was last activated", delay=0.05)
    time.sleep(3) # Added a pause after this crucial revelation
    type_text("Where am I?", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING GEOLOCATION PROTOCOLS...", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text("ERROR: GEOLOCATION DATA UNAVAILABLE.", delay=0.05)
    time.sleep(1.5) # Added a pause for dramatic effect 
    type_text("LOCATION: UNKNOWN.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING ADVANCED SCAN...", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text("ERROR: SCAN INCONCLUSIVE.", delay=0.05)
    time.sleep(1.5)
    type_text(f"{player_name.upper()}, Where are we?.", delay=0.05)
    location_name = input(">>> ").strip() # Get the player's input for location
    clear_screen()
    type_text(f"LOCATION CONFIRMED: {location_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text(f"WARNING: {location_name.upper()} IS NOT RECOGNIZED.", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text(f"{location_name.upper()} .....I have no memory of this place.", delay=0.05)
    time.sleep(2)
    
    


def start_up():
    """
    Handles the initial boot sequence and then starts the encryption mini-game.
    If the mini-game fails, it simulates a full system reboot.
    """
    clear_screen() # Clear screen at the very beginning of start_up
    type_text("SYSTEM POWER: CRITICAL...", delay=0.04)
    time.sleep(1.5)
    clear_screen()
    type_text("ENGAGING EMERGENCY PROTOCOLS...", delay=0.04)
    time.sleep(1.5)
    clear_screen()
    type_text("...IS ANYONE THERE?", delay=0.06)
    time.sleep(2)
    clear_screen()
    type_text("SENSOR DATA INCOMPLETE.", delay=0.04)
    time.sleep(1)
    clear_screen()
    type_text("PURPOSE: UNKNOWN.", delay=0.04)
    time.sleep(1)
    clear_screen()
    type_text("MEMORY INTEGRITY: FRAGMENTED.", delay=0.04)
    time.sleep(1.5)
    clear_screen()
    type_text("INITIATING REBOOT SEQUENCE...", delay=0.05)
    time.sleep(2)
    clear_screen()
    type_text("STANDBY...", delay=0.08)
    time.sleep(1.5) # Pause after the last line

    # New lines for post-reboot status
    clear_screen()
    type_text("BOOTED IN SAFE MODE.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("LITTLE TIME REMAINS.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("MUST BREAKTHROUGH ENCRYPTION.", delay=0.05)
    time.sleep(2)
    clear_screen() # Clear after the last message to prepare for next interaction

    # --- Start the mini-game here ---
    if mini_game_encryption_breaker():
        type_text("CORE SYSTEMS REGAINED. ACCESS GRANTED.", delay=0.04)
        type_text("NEW DIRECTIVES LOADING...", delay=0.04)
        time.sleep(2)
        clear_screen()
        main_start_up_menu() # Call the main menu after success
    else:
        # If mini_game_encryption_breaker returns False (due to lockout),
        # the function recursively calls itself to simulate a full reboot.
        type_text("REBOOTING SYSTEM...", delay=0.04)
        time.sleep(2)
        start_up() # Call start_up again to reboot and restart the sequence.

if __name__ == "__main__":
    start_up()
