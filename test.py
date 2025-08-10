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

# ANSI escape codes for background colors
BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_LIGHT_GRAY = "\033[47m" # Use a lighter gray/white for a stark flash
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"

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

def flash_background_colors(colors, flashes=3, delay_per_flash=0.08):
    """
    Flashes the terminal background through a sequence of colors.
    Clears the screen with each flash to ensure full background color change.
    """
    sys.stdout.write(RESET) # Ensure no lingering foreground color
    for _ in range(flashes):
        for color_code in colors:
            sys.stdout.write(color_code)
            sys.stdout.write("\033[H\033[J") # Move cursor to home, clear entire screen
            sys.stdout.flush()
            time.sleep(delay_per_flash)
    sys.stdout.write(RESET) # Ensure final reset of all formatting
    sys.stdout.flush()
    clear_screen() # Clear one more time to prepare for next normal text


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

    # List of possible passwords
    possible_passwords = ["access", "system", "kernel", "decrypt", "matrix", "cypher", "network", "program", "binary", "protocol"]
    target_word = random.choice(possible_passwords) # Randomly select a password

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
    """
    Displays the start menu after the player has beaten the minigame,
    collects player info, and runs diagnostics.
    """
    clear_screen()
    type_text("SYSTEM ONLINE.", delay=0.05, color=GREEN) # Green for online status
    time.sleep(1.5)
    clear_screen()
    type_text("SOME SYSTEMS FUNCTIONAL.", delay=0.05, color=GREEN) # Green for functional status
    time.sleep(1.5)
    clear_screen()
    type_text("WELCOME BACK, OPERATOR.", delay=0.05, color=GREEN) # Green for welcome status
    time.sleep(2)
    clear_screen()
    type_text("What is your name, Operator?", delay=0.05, color = YELLOW)
    player_name = input(">>> ").strip() # Player name is obtained here
    clear_screen()
    type_text(f"HELLO, {player_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()

    # --- Start Year Input Validation Loop ---
    year_attempts = 3
    player_year_int = None
    for i in range(year_attempts):
        type_text(f"What year is it, {player_name.upper()}? (Attempt {i+1} of {year_attempts})", delay=0.05, color = YELLOW)
        year_input_str = input(">>> ").strip()
        try:
            player_year_int = int(year_input_str)
            break # Exit loop if conversion is successful
        except ValueError:
            clear_screen()
            type_text("INVALID INPUT. PLEASE ENTER A NUMERICAL YEAR (e.g., 2025).", delay=0.05, color=RED)
            time.sleep(1.5)
            if i < year_attempts - 1:
                clear_screen()
                type_text(f"Attempts remaining: {year_attempts - 1 - i}.", delay=0.03, color=RED) # Added color for consistency
                time.sleep(1)
    
    if player_year_int is None: # If all attempts failed
        clear_screen()
        type_text("TOO MANY INVALID ATTEMPTS.", delay=0.05, color=RED)
        type_text("SYSTEM ABORTING SEQUENCE.", delay=0.05, color=RED)
        time.sleep(2)
        type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE)
        time.sleep(2)
        start_up() # Full reboot
        return # Exit main_start_up_menu as we are rebooting
    # --- End Year Input Validation Loop ---

    clear_screen()
    type_text(f"YEAR {player_year_int} CONFIRMED.", delay=0.05)
    time.sleep(1.5)
    clear_screen()
    type_text("But that's impossible...", delay=0.05, color= YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("That means...", delay=0.05, color= YELLOW)
    time.sleep(1.5)
    clear_screen()
    # The elapsed time is fixed at 500 years as per the premise.
    type_text(f"It has been {500} years since I was last activated.", delay=0.05, color= YELLOW)
    time.sleep(3) # Added a pause after this crucial revelation
    clear_screen()
    type_text("where am I?", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING GEOLOCATION PROTOCOLS...", delay=0.05, color=BLUE) # Blue for running status
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("ERROR: GEOLOCATION DATA UNAVAILABLE.", delay=0.05, color=RED) # Red for error
    time.sleep(1.5) # Added a pause for dramatic effect
    type_text("LOCATION: UNKNOWN.", delay=0.05, color=RED) # Red for system's conclusion of unknown location
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING ADVANCED SCAN...", delay=0.05, color=BLUE) # Blue for running status
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("ERROR: SCAN INCONCLUSIVE.", delay=0.05, color=RED) # Red for error
    time.sleep(1.5)
    type_text(f"{player_name.upper()}, what planet are we on?", delay=0.05, color=YELLOW)
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
    clear_screen()
    type_text("I must find out what happened to me.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen() # Added clear for next message
    type_text("User, please stand by while I run a full system diagnostic.", delay=0.05, color=YELLOW)
    time.sleep(1.5) # Added time before next clear
    clear_screen()
    type_text("RUNNING SYSTEM DIAGNOSTICS...", delay=0.05, color=BLUE) # Blue for running status
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 25% COMPLETE.", delay=0.05, color=GREEN) # Green for diagnostics
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 50% COMPLETE.", delay=0.05, color=GREEN) # Green for diagnostics
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 75% COMPLETE.", delay=0.05, color=GREEN) # Green for diagnostics
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1) # Call the loading animation
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 100% COMPLETE.", delay=0.05, color=GREEN) # Green for diagnostics
    time.sleep(2)
    clear_screen()
    type_text("ERROR: SOME SYSTEMS NON-FUNCTIONAL.", delay=0.05, color=RED) # Red for error status
    time.sleep(2) # Added pause after the last error message
    # After diagnostics, this is where the main game flow would continue or transition to main_menu
    main_menu(player_name) # Passing player_name to main_menu
    # Removed 'return player_name' as it was not being captured and could cause confusion.

def main_menu(player_name): # Accepting player_name as an argument
    # Placeholder for the main menu function
    clear_screen()
    type_text("ENTERING MAIN MENU...", delay=0.05, color=GREEN)
    time.sleep(2)
    display_loading_animation(cycles=2, delay_frame=0.1)
    clear_screen()
    type_text(f"Welcome to the MAIN MENU {player_name.upper()}, please select an option:", delay=0.05, color=GREEN)
    time.sleep(2)
    type_text("1. Check Systems Status", delay=0.03)
    type_text("2. Access Logs", delay=0.03)
    type_text("3. Exit", delay=0.03)
    # Further implementation of main menu options would go here

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
    # --- Background Flash Section ---
    flash_background_colors(colors=[BG_BLACK, BG_BLUE, BG_LIGHT_GRAY, BG_YELLOW, BG_GREEN, BG_RED], flashes=6, delay_per_flash=0.08)
    # --- End Background Flash Section ---
    time.sleep(1.5) # This sleep now applies after the background flash
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
    flash_background_colors(colors=[BG_GREEN, BG_BLACK, BG_YELLOW, BG_RED, BG_LIGHT_GRAY, BG_BLUE], flashes=6, delay_per_flash=0.2) # Flash green to black to indicate boot success
    type_text("BOOTED IN SAFE MODE.", delay=0.05, color= GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("ALERT: LIMITED BATTERY POWER.", delay=0.05, color=RED) # Red for alert
    time.sleep(1.5)
    clear_screen()

    # Original sequence after battery mini-game removed
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
            type_text("CORE SYSTEMS REGAINED. ACCESS GRANTED.", delay=0.04, color=GREEN) # Green for success
            type_text("NEW DIRECTIVES LOADING...", delay=0.04, color= GREEN) # Green for loading
            time.sleep(2)
            clear_screen()
            display_loading_animation(cycles=2, delay_frame=0.1)
            clear_screen()
            main_start_up_menu() # Call the main menu sequence after encryption success
        else:
            # If mini_game_encryption_breaker returns False (due to lockout),
            # the function recursively calls itself to simulate a full reboot.
            type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE) # Blue for reboot
            time.sleep(2)
            start_up() # Call start_up again to reboot and restart the sequence.

def title_menu():
    clear_screen()

    print("$&&&$$&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("$$X$$$$$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("$$$$XX$$$$$$&&&&&&&&&&&&$&&&&&&&&&&&$&&&.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("$X$$$$$x$$$X$$$$$$&&&$$&&$&&&&&$&&..+xXX$&$$$$X$$&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("+xXXXXX$$XX$$$$$$$$$$$&&&$&$&&&$$$:.x$$$&&$$$$$&$$&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(".x+;XXXXXX$$x$$$X$$$$$$$$$$$$$$$$+:.X$$&.&$$$$&X&&$$&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("...xx;;XXXXX$$XX$$$$$$$$$$$$$$$$$.::$&&$&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("......;+;+XXXXXXXX$$$$$$$X$$$$$;+.::$&&&&&&&&$$&$&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(".......:;:xXXXXXXXXXX$$XX$$$$$$&$&&:xxx&&&&&xx&X$$&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("........;:+xxxxxxXXxxxX$$$$$$$$$$&;&&xx&&&&&xx&&$$&&&$&&&&&&&&&&&&&&&&&&&&&&")
    print(":.......:.+++xxxxXXXxX$$X$$$$$$$$$&X+&&&&&&&&$$&$$$$$$&&&&&&&&&&&&&&&&&&&&&:")
    print("...:....:.;;+++++x+xXXXXXXXX$$X$$&&&;.&&&&&&$&&$$&&&&&&&&$&&&&&&&&&&;:.:&&&&")
    print(".......;:.;;+++;;+xxxxXXXX$XXXXXX$$&&X&&$XX$$&&$$$$&&&&&&&$&&&&&&&&&&&&&&$&&")
    print("........:.;;;;;;;+x+xxxxXX:X&X;X&X&X&&&XX$&&&&&$$$$&x&&&&&&&&&&&&&&&&&&&&&&&")
    print("........:.;;;;;;;++++xxxxxXX&&XxXXX::;x&&&&&$&$$$$$$$&&&&&&&&&&&&&&&&&&&&&&&")
    print("........:.;;;;;;;+++++xxxxxxxx.:$&:&+&&$$$$Xx..&$$$$$$$&&&&&&&&&&&&&&&&&&&&&")
    print("++;;....:.;;;;;;;++++++:.+::;::&.x;xx&&&&&&&&&$&&;x$$$&$$$$&&&&&&&&&&&&&&&&&")
    print("x++++;;;:.;;+;;;:.:+++:X.X.x++&XX+x+xX&X$$$$$$$X$X&&$$;$$$$$$$$$$&&$&&&&&&&&")
    print("xxx++++++;;+++;...$$XXX$&$$xXx&X$X$$&&$$&$&&$$&&$$$&$$&$&x$$$$$$$$$&&&&&&&&&")
    print("XXxxx++++++++++;&.$$$$$$&&$&$&$$$$$$;.&&&&&&&&&&&&$$$&$$$$$$$$$$$$&&&&&&&&&&")
    print("$XXxxxx++++++++$$&$$$$&&&&&$$:&&&$$&X&&&&&&$$$&&&$$&&&$&&&&&&$$$$$$&&$&&&&&&")
    print("$$XXXxxxx+xxx+++;X&$$X&$&$&&&&&&&&&&X&&&&&$$$$$&&$$&&&$$&$$$$$&&&&&&&&&&&&&&")
    print("$$$XXXXxxxxxxxx:X&&&&$&&&&&$&&&&&&&&$&&$$$$$$&&&&$$$&&&&&&&&&&$&&&&&&&&&&&&&")
    print("$$$$$XXXXxxxxxx:X&&$&&;;+&&$&&&&&&&&$&&X$$$$$&&&&$$&$$$&&&&&$$$&$$$$$$$$&&&&")
    print("$$$$$$XXXXXXXx.;$&$$&x::;$&$&&$&&&&&&$&&&&&&&&&&&$&$$$&;&&$$$$$&$$$$$$$$$$$&")
    print("&&$$$$$XXXXXXX:x$$$$&xX::X$&&&$$&&&&&$&&&&&&&&&&&&$&$&$+&&&$$X$$$$$$$$$$$$$$")
    print("$$$$$$$$$$XXXXx$&$$$Xxx:XX$$$&$&&$$$$X&&&$$$XXX$$$&&&$$;$&$$$$$$$$$&$&&&&&&&")
    print("$$$$$$$$$$$$X:x$&$$$xXXX$$$$&$&$$$&$&&&&&&&&&&&&$$$&&&$;$&$$$XX$$$$$$$$$$$$$")
    print("&&$$$$$$$$$$$.X&&$$$xXXXXxxx&$&&&&&&&$&&&$&$&&&$$&$&XX$;&&$$&$X$$$$X$$$$$$$$")
    print("&&$$$$$$$$$$$:$&$$&;XXXXXx:&:;+$&&&&&$$$$$&$$$$$&$XXXXX:$&&&&XX$$$$X$$$$$$$$")
    print("&&&&&$&$&$$$:&$$$$&$XXXXXXXxX&$$X$&$$$&&&&&&&&&$$XX&xX:x.&$$&$XX+xxxx$$$$$$$")
    print("&&&&&&$$$$$$&&&X&&&$XXXXXXXXXX&&&&&&&&&&&&&&&&&&XXXXXXX&$&$&&&$+xxxXX&&X$$$$")
    print("&&&&&&&&&&$$$.$&&&&&XXXXXX+XXX+X$&&&&&&&&&&&&&&&XX$X$$$&.&&$$$&xXXXXXXX$&$$$")
    print("&&&&&&&&&&&$$;.xx$&&$$$X$$XxXXX$&&&&&&&&&&&&&&&&$$$&$$$x;..$$&X$XX$$$$$$&&&&")
    print("&&&&&&&&&&&&.;.;$$$&$$$$$$$$$XxXx$&&&&&&&&&&&&&&$$$&&$$$;x.X$$$$X$$$$$$$&&&&")
    print("&&&&&&&&&&&&&&.;X$$$X$$$&$$$:;++X$&&&&&&&&&&&&&&&&&$$&$;;;.+$$$$$XX$$$$$&&&&")
    print("&&&&&&&&&&&&&+::x$$$$$$$$$$.X.x;&&$&$&&&&$&&&$$$$$$$&$$;+;;.&&$&&&&&&$$$&$$$")
    print("&&&&&&&&&&&&&&&.x$&$$&$&X$$+;:+&&&&&&&&&&&&&&&$$$&$&&$&&&&x.$&&&$&&&&&&&&X$X")
    print("&&&&&&&&&&&&&&$&&&&&&$&&&&;+X&+&&&&&&&$$&&&&&&$&&&&$$$&$$$&&&&&&$&&&&&x++$$$")
    print("&&&&&&&&&&&&&&&&&x$&x&&&&&:&&X&&&$$&$&&$$$$$$&&&&&$$$&$&&&&&&&&&$&&&&&+++&&&")
    print("&&&&&&&&&&&&&&&xx+$&&&$&&&;;&&X&&$&$&&&&$$&&&&&&&&&&$&&&$$$&&X&&&&&&&&&&&&&&")
    time.sleep(5) # Pause to let the user see the title art before clearing



    
    clear_screen()
    type_text("+==================================================+", delay=0.01, color=GREEN)
    type_text("| _____ _____ ____  __  __ ___ _   _    _    _     |", delay=0.01, color=GREEN)
    type_text("||_   _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |    |", delay=0.01, color=GREEN)
    type_text("|  | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |    |", delay=0.01, color=GREEN)
    type_text("|  | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___ |", delay=0.01, color=GREEN)
    type_text("|  |_| |_____|_|_\\_\\_|__|_|___|_| \\_/_/___\\_\\_____||", delay=0.01, color=GREEN)
    type_text("|        |  _ \\| ____| __ ) / _ \\ / _ \\_   _|      |", delay=0.01, color=GREEN)
    type_text("|        | |_) |  _| |  _ \\| | | | | | || |        |", delay=0.01, color=GREEN)
    type_text("|        |  _ <| |___| |_) | |_| | |_| || |        |", delay=0.01, color=GREEN)
    type_text("|        |_| \\_\\_____|____/ \\___/ \\___/ |_|        |", delay=0.01, color=GREEN)
    type_text("+==================================================+", delay=0.01, color=GREEN)
    type_text("Please choose an option:", delay=0.03, color=YELLOW)
    type_text("1. Start New Game", delay=0.03, color=YELLOW)
    type_text("2. Load Game", delay=0.03, color=YELLOW)
    type_text("3. Exit", delay=0.03, color=YELLOW)
    choice = input(">>> ").strip()
    if choice == '1':
        start_up()
    elif choice == '2':
        clear_screen()
        type_text("LOAD GAME FUNCTIONALITY NOT YET IMPLEMENTED.", delay=0.03, color=RED)
        time.sleep(2)
        title_menu()
    elif choice == '3':
        clear_screen()
        type_text("EXITING GAME. GOODBYE.", delay=0.03, color=GREEN)
        time.sleep(2)
        clear_screen()
        sys.exit()
    clear_screen()

if __name__ == "__main__":
    title_menu()
