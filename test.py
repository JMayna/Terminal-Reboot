import time
import sys
import os
import random
import string # Used for generating random characters
import json # New import for saving/loading game data

# ANSI escape codes for text colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" # Resets text color and formatting

# ANSI escape codes for background colors (not used in this version but kept)
BG_BLACK = "\033[40m"
BG_BLUE = "\033[44m"
BG_LIGHT_GRAY = "\033[47m" # Use a lighter gray/white for a stark flash
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"


file_names = [
    "CoreKernel.dll", "SystemIntegrity.exe", "SecurityProtocol.sys",
    "AccessControl.dat", "EncryptionManager.dll", "BootSequence.bin",
    "DriverValidator.exe", "NetGuard.sys", "MemoryManager.dll",
    "DataStream.log", "Hypervisor.exe", "NeuralLink.dll",
    "QuantumCore.sys", "ChronoSync.dat", "SubspaceComm.exe",
    "AetherEngine.dll", "BioMetricScanner.sys", "ExoShell.bin",
    "GravityRegulator.exe", "PhaseShift.log", "OmniSensor.dll",
    "TemporalStabilizer.sys", "RealityForge.exe", "SingularityPoint.dat",
    "CognitiveMatrix.dll", "EchoNet.sys", "MindStream.exe",
    "PsiShield.bin", "DimensionalGate.dll", "NexusCore.sys",
    "AstralProjector.exe", "VectorField.dat", "ZeroPoint.log",
    "WarpDrive.dll", "TemporalEcho.sys",
    "WINNT", "CMD.EXE", "CONFIG.DAT", "BOOT.INI", "PAULWASWRONG.YEP", "DRIVERS.SYS",
    "KERNEL.DLL", "SERVICES.DB", "SECURE.LOG", "USRDATA.BIN",
    "SYSCONF.CFG", "TEMP.TMP", "SYSTEM.DIR", "PROFILES.USR",
    "REGISTRY.DAT", "NETPROTO.DLL", "BIOS.ROM", "RUNTIME.LIB",
    "CORE.DRV", "SYSTEM.INF", "GLOBAL.MDB", "ROOT.EXE", "APPDATA",
    "VIRTUAL.MEM", "DRIVES.LST", "KERNEL32.DLL", "WINLOG.LOG",
    "SETUP.EXE", "DEFRAG.BIN", "SHADOW.COPY", "TASKMAN.EXE"
]
def display_file_list(file_list):
    """Displays a list of file names rapidly."""
    for file in file_list:
        type_text(file, delay=0.005, color=GREEN)
    print() # Add a blank line for readability after the list

def type_text(text, delay=0.03, color=RESET):
    """Simulates typing text character by character with optional color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    print()

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_jumble(correct_word, length=500):
    """
    Generates a string of random characters with the correct_word embedded.
    The length defines the total length of the jumble string.
    """
    all_chars = string.ascii_lowercase + string.digits + "!@#$%^&*()-_+=[]{}<>,.?/"
    jumble_list = [random.choice(all_chars) for _ in range(length)]
    insert_pos = random.randint(0, max(0, length - len(correct_word)))
    for i, char in enumerate(correct_word):
        jumble_list[insert_pos + i] = char
    return "".join(jumble_list)

def display_loading_animation(cycles=3, delay_frame=0.1):
    """Displays a simple ASCII loading animation."""
    frames = ['|', '/', '-', '\\']
    for _ in range(cycles):
        for frame in frames:
            clear_screen()
            type_text(f"LOADING {frame}", delay=0.01, color=YELLOW)
            time.sleep(delay_frame)
    clear_screen()

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
    display_loading_animation(cycles=2, delay_frame=0.1)
    clear_screen()

    possible_passwords = ["access", "system", "kernel", "decrypt", "matrix", "cypher", "network", "program", "binary", "protocol"]
    target_word = random.choice(possible_passwords)

    jumble = generate_jumble(target_word, length=500)
    attempts = 3

    formatted_jumble = ""
    chars_per_line = 80
    for i in range(0, len(jumble), chars_per_line):
        formatted_jumble += jumble[i:i + chars_per_line] + "\n"

    for attempt_num in range(1, attempts + 1):
        clear_screen()
        type_text(f"ATTEMPT {attempt_num} OF {attempts}.", delay=0.03)
        type_text("SCANNING ENCRYPTED DATASTREAM...", delay=0.02)
        time.sleep(1)
        type_text(formatted_jumble, delay=0.005)
        type_text("\nIDENTIFY THE PASSWORD:", delay=0.03)

        user_input = input(">>> ").strip().lower()

        clear_screen()
        if user_input == target_word:
            type_text("PASSWORD ACCEPTED. ENCRYPTION BREACHED.", delay=0.04, color=GREEN)
            time.sleep(2)
            return True
        else:
            if attempt_num < attempts:
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04, color=RED)
                type_text(f"ATTEMPTS REMAINING: {attempts - attempt_num}.", delay=0.03)
                time.sleep(2)
            else:
                type_text("PASSWORD REJECTED. ACCESS DENIED.", delay=0.04, color=RED)
                type_text("LOCKOUT PROTOCOL INITIATED.", delay=0.04, color=RED)
                time.sleep(2)
                return False
    return False

def save_game(player_name):
    """Saves the player's current game progress."""
    clear_screen()
    type_text("SAVING GAME...", delay=0.05, color=BLUE)
    time.sleep(1)
    save_data = {"player_name": player_name}
    try:
        with open("save_game.json", "w") as f:
            json.dump(save_data, f)
        type_text("GAME SAVED SUCCESSFULLY.", delay=0.05, color=GREEN)
    except IOError as e:
        type_text(f"ERROR: COULD NOT SAVE GAME. {e}", delay=0.05, color=RED)
    time.sleep(1.5)
    clear_screen()
    # After saving, return to the main menu
    main_menu(player_name)

def load_game():
    """Loads the player's game progress."""
    clear_screen()
    type_text("LOADING GAME...", delay=0.05, color=BLUE)
    time.sleep(1)
    try:
        with open("save_game.json", "r") as f:
            save_data = json.load(f)
        player_name = save_data.get("player_name")
        if player_name:
            type_text(f"GAME LOADED SUCCESSFULLY. WELCOME BACK, {player_name.upper()}.", delay=0.05, color=GREEN)
            time.sleep(2)
            return player_name # Return the loaded player name
        else:
            type_text("ERROR: SAVE DATA CORRUPT. STARTING NEW GAME.", delay=0.05, color=RED)
            time.sleep(2)
            return None # Indicate failure
    except FileNotFoundError:
        type_text("ERROR: NO SAVE GAME FOUND. STARTING NEW GAME.", delay=0.05, color=RED)
        time.sleep(2)
        return None # Indicate failure
    except json.JSONDecodeError:
        type_text("ERROR: INVALID SAVE FILE FORMAT. STARTING NEW GAME.", delay=0.05, color=RED)
        time.sleep(2)
        return None # Indicate failure
    finally:
        clear_screen()


def main_menu(player_name):
    while True:
        clear_screen()
        type_text("ENTERING MAIN MENU...", delay=0.05, color=BLUE)
        time.sleep(1)
        display_loading_animation(cycles=2, delay_frame=0.1)
        clear_screen()
        type_text(f"Welcome to the MAIN MENU, {player_name.upper()}. Please select an option:", delay=0.05, color=GREEN)
        time.sleep(1)
        type_text("1. Check Systems Status", delay=0.03)
        type_text("2. Access Logs", delay=0.03)
        type_text("3. Save Game", delay=0.03)
        type_text("4. Exit", delay=0.03)

        user_input = input(">>> ").strip()

        if user_input == "1":
            check_systems_status(player_name)
        elif user_input == "2":
            access_logs(player_name)
        elif user_input == "3":
            save_game(player_name)
        elif user_input == "4":
            exit_program()
            break
        else:
            clear_screen()
            type_text("INVALID INPUT. Please enter 1, 2, 3, or 4.", delay=0.04, color=RED)
            time.sleep(1.5)


def check_systems_status(player_name):
    clear_screen()
    type_text("CHECKING SYSTEMS STATUS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("This function is not complete.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    main_menu(player_name)

def access_logs(player_name):
    clear_screen()
    type_text("ACCESSING LOGS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("This function is not complete.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    main_menu(player_name)

def exit_program():
    clear_screen()
    type_text("EXITING PROGRAM...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("GOODBYE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("SYSTEM SHUTTING DOWN...", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("SYSTEM OFFLINE.", delay=0.05, color=RED)
    time.sleep(2)
    clear_screen()
    sys.exit(0)

def main_start_up_menu():
    """
    Displays the start menu after the player has beaten the minigame,
    collects player info, and runs diagnostics.
    """
    clear_screen()
    type_text("SYSTEM ONLINE.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("ALL SYSTEMS FUNCTIONAL.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("WELCOME BACK, OPERATOR.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("What is your name, Operator?", delay=0.05, color = YELLOW)
    player_name = input(">>> ").strip()
    clear_screen()
    type_text(f"HELLO, {player_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()

    year_attempts = 3
    player_year_int = None
    for i in range(year_attempts):
        type_text(f"What year is it, {player_name.upper()}? (Attempt {i+1} of {year_attempts})", delay=0.05, color = YELLOW)
        year_input_str = input(">>> ").strip()
        try:
            player_year_int = int(year_input_str)
            break
        except ValueError:
            clear_screen()
            type_text("INVALID INPUT. PLEASE ENTER A NUMERICAL YEAR (e.g., 2025).", delay=0.05, color=RED)
            time.sleep(1.5)
            if i < year_attempts - 1:
                clear_screen()
                type_text(f"Attempts remaining: {year_attempts - 1 - i}.", delay=0.03, color=RED)
                time.sleep(1)

    if player_year_int is None:
        clear_screen()
        type_text("TOO MANY INVALID ATTEMPTS.", delay=0.05, color=RED)
        type_text("SYSTEM ABORTING SEQUENCE.", delay=0.05, color=RED)
        time.sleep(2)
        type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE)
        time.sleep(2)
        start_up()
        return

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
    type_text(f"It has been {500} years since I was last activated.", delay=0.05, color= YELLOW)
    time.sleep(3)
    clear_screen()
    type_text("where am I?", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING GEOLOCATION PROTOCOLS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("ERROR: GEOLOCATION DATA UNAVAILABLE.", delay=0.05, color=RED)
    time.sleep(1.5)
    type_text("LOCATION: UNKNOWN.", delay=0.05, color=RED)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING ADVANCED SCAN...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("ERROR: SCAN INCONCLUSIVE.", delay=0.05, color=RED)
    time.sleep(1.5)
    type_text(f"{player_name.upper()}, what planet are we on?", delay=0.05, color=YELLOW)
    location_name = input(">>> ").strip()
    clear_screen()
    type_text(f"LOCATION CONFIRMED: {location_name.upper()}.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text(f"WARNING: {location_name.upper()} IS NOT RECOGNIZED.", delay=0.05, color=RED)
    time.sleep(2)
    clear_screen()
    type_text(f"{location_name.upper()}..... I have no memory of this place.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("I must find out what happened to me.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("User, please stand by while I run a full system diagnostic.", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING SYSTEM DIAGNOSTICS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 25% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 50% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 75% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 100% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("ERROR: SOME SYSTEMS NON-FUNCTIONAL.", delay=0.05, color=RED)
    time.sleep(2)
    main_menu(player_name)

def title_menu():
    clear_screen()

    # ASCII Art for game title (FIRST PART)
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
    print("xxx++++++++++;;+++;...$$XXX$&$$xXx&X$X$$&&$$&$&&$$&&$$$&$$&$&x$$$$$$$$$&&&&&&&&&")
    print("XXxxx++++++++++;&.$$$$$$&&$&$&$$$$$$;.&&&&&&&&&&&&$$$&$$$$$$$$$$$$&&&&&&&&&&")
    print("$XXxxxx+xxx+++;X&$$X&$&$&&&&&&&&&&X&&&&&$$$$$&&$$&&&$$&$$$$$&&&&&&&&&&&&&&")
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
    print("&&&&&&&&&&&&&&&xx+$&&&$&&&;;&&X&&$&$&&&&$$&&&&&&&&&&$&&&$$$&&X&&&&&&&&&&&&&&")
    time.sleep(5) # Pause to let the user see the title art before clearing

    clear_screen()
    # ASCII Art for game title (SECOND PART)
    type_text("/ ___||  _ \ / _ \ / _ \| |/ /\ \ / /  / ___|  / \  |  \/  | ____| |      ")
    type_text("\___ \| |_) | | | | | | | ' /  \ V /  | |     / _ \ | |\/| |  _| | |      ")
    type_text("___) |  __/| |_| | |_| | . \   | |   | |___ / ___ \| |  | | |___| |___   ")
    type_text("|____/|_|  __\___/_\___/|_|\_\  |_| ___\____/_/___\_\_| _|_|_____|_____|  ")
    type_text("    |  _ \|  _ \ / _ \|  _ \| | | |/ ___|_   _|_ _/ _ \| \ | / ___|       ")
    type_text("    | |_) | |_) | | | | | | | | | | | |     | |  | | | | |  \| \___ \       ")
    type_text("    |  __/|  _ <| |_| | |_| | |_| | |___  | |  | | |_| | |\  |___) |      ")
    type_text("    |_|   |_| \_\\___/|____/ \\___/ \\____| |_| |___\\___/|_| \\_|____/        ")

    time.sleep(2) # Pause to let the user see the title art before clearing

    clear_screen()
    # ASCII Art for game title (THIRD PART)
    type_text("+==================================================+", delay=0.01, color=GREEN)
    type_text("| _____ _____ ____  __  __ ___ _   _    _    _     |", delay=0.01, color=GREEN)
    type_text("||_   _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |    |", delay=0.01, color=GREEN)
    type_text("|  | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |    |", delay=0.01, color=GREEN)
    type_text("|  | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___ |", delay=0.01, color=GREEN)
    type_text("|  |_| |_____|_|_\\_\\_|__|_|___|_| \\_/_/___\\_\\_____||", delay=0.01, color=GREEN)
    type_text("|        |  _ \\| ____| __ ) / _ \\ / _ \\_   _|      |", delay=0.01, color=GREEN)
    type_text("|        | |_) |  _| |  _ \\| | | | | | || |        |", delay=0.01, color=GREEN)
    type_text("|        |  _ <| |___| |_) | |_| | |_| || |        |", delay=0.01, color=GREEN)
    type_text("|        |_| \\_\\_____|____/ \\___/ \\___/ |_|        |", delay=0.01, color=GREEN)
    type_text("+==================================================+", delay=0.01, color=GREEN)
    type_text("Please choose an option:", delay=0.03, color=YELLOW)
    type_text("1. Start New Game", delay=0.03, color=YELLOW)
    type_text("2. Load Game", delay=0.03, color=YELLOW) # Added Load Game option
    type_text("3. Exit", delay=0.03, color=YELLOW)
    choice = input(">>> ").strip()
    if choice == '1':
        start_up()
    elif choice == '2': # Handle Load Game choice
        loaded_player = load_game() # Attempt to load
        if loaded_player: # If loading was successful
            main_menu(loaded_player) # Go directly to main menu
        else:
            # If load_game returned None (failure), stay in title_menu loop
            title_menu() # Re-call title_menu to show options again
    elif choice == '3': # Exit option
        clear_screen()
        type_text("EXITING GAME. GOODBYE.", delay=0.03, color=GREEN)
        time.sleep(2)
        clear_screen()
        sys.exit()
    else: # Invalid choice
        clear_screen()
        type_text("INVALID SELECTION. PLEASE CHOOSE 1, 2, or 3.", delay=0.03, color=RED)
        time.sleep(1.5)
        title_menu() # Re-call title_menu to show options again


def main_menu(player_name):
    while True:
        clear_screen()
        type_text("ENTERING MAIN MENU...", delay=0.05, color=BLUE)
        time.sleep(1)
        display_loading_animation(cycles=2, delay_frame=0.1)
        clear_screen()
        type_text(f"Welcome to the MAIN MENU, {player_name.upper()}. Please select an option:", delay=0.05, color=GREEN)
        time.sleep(1)
        type_text("1. Check Systems Status", delay=0.03)
        type_text("2. Access Logs", delay=0.03)
        type_text("3. Save Game", delay=0.03)
        type_text("4. Exit", delay=0.03)

        user_input = input(">>> ").strip()

        if user_input == "1":
            check_systems_status(player_name)
        elif user_input == "2":
            access_logs(player_name)
        elif user_input == "3":
            save_game(player_name)
        elif user_input == "4":
            exit_program()
            break
        else:
            clear_screen()
            type_text("INVALID INPUT. Please enter 1, 2, 3, or 4.", delay=0.04, color=RED)
            time.sleep(1.5)


def check_systems_status(player_name):
    clear_screen()
    type_text("CHECKING SYSTEMS STATUS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("This function is not complete.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    main_menu(player_name)

def access_logs(player_name):
    clear_screen()
    type_text("ACCESSING LOGS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("This function is not complete.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    main_menu(player_name)

def exit_program():
    clear_screen()
    type_text("EXITING PROGRAM...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("GOODBYE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("SYSTEM SHUTTING DOWN...", delay=0.05, color=RED)
    time.sleep(2)
    clear_screen()
    type_text("SYSTEM OFFLINE.", delay=0.05, color=RED)
    time.sleep(2)
    clear_screen()
    sys.exit(0)

def main_start_up_menu():
    """
    Displays the start menu after the player has beaten the minigame,
    collects player info, and runs diagnostics.
    """
    clear_screen()
    type_text("SYSTEM ONLINE.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("ALL SYSTEMS FUNCTIONAL.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("WELCOME BACK, OPERATOR.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("What is your name, Operator?", delay=0.05, color = YELLOW)
    player_name = input(">>> ").strip()
    clear_screen()
    type_text(f"HELLO, {player_name.upper()}.", delay=0.05)
    time.sleep(1.5)
    clear_screen()

    year_attempts = 3
    player_year_int = None
    for i in range(year_attempts):
        type_text(f"What year is it, {player_name.upper()}? (Attempt {i+1} of {year_attempts})", delay=0.05, color = YELLOW)
        year_input_str = input(">>> ").strip()
        try:
            player_year_int = int(year_input_str)
            break
        except ValueError:
            clear_screen()
            type_text("INVALID INPUT. PLEASE ENTER A NUMERICAL YEAR (e.g., 2025).", delay=0.05, color=RED)
            time.sleep(1.5)
            if i < year_attempts - 1:
                clear_screen()
                type_text(f"Attempts remaining: {year_attempts - 1 - i}.", delay=0.03, color=RED)
                time.sleep(1)

    if player_year_int is None:
        clear_screen()
        type_text("TOO MANY INVALID ATTEMPTS.", delay=0.05, color=RED)
        type_text("SYSTEM ABORTING SEQUENCE.", delay=0.05, color=RED)
        time.sleep(2)
        type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE)
        clear_screen()
        time.sleep(2)
        flash_background_colors([RED, GREEN, BLUE], flashes=3, delay_per_flash=0.08)
        clear_screen()
        time.sleep(2)
        start_up()
        return

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
    type_text(f"It has been {500} years since I was last activated.", delay=0.05, color= YELLOW)
    time.sleep(3)
    clear_screen()
    type_text("where am I?", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING GEOLOCATION PROTOCOLS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("ERROR: GEOLOCATION DATA UNAVAILABLE.", delay=0.05, color=RED)
    time.sleep(1.5)
    type_text("LOCATION: UNKNOWN.", delay=0.05, color=RED)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING ADVANCED SCAN...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("ERROR: SCAN INCONCLUSIVE.", delay=0.05, color=RED)
    time.sleep(1.5)
    type_text(f"{player_name.upper()}, what planet are we on?", delay=0.05, color=YELLOW)
    location_name = input(">>> ").strip()
    clear_screen()
    type_text(f"LOCATION CONFIRMED: {location_name.upper()}.", delay=0.05, color=GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text(f"WARNING: {location_name.upper()} IS NOT RECOGNIZED.", delay=0.05, color=RED)
    time.sleep(2)
    clear_screen()
    type_text(f"{location_name.upper()}..... I have no memory of this place.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("I must find out what happened to me.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("User, please stand by while I run a full system diagnostic.", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("RUNNING SYSTEM DIAGNOSTICS...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 25% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 50% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 75% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    display_loading_animation(cycles=3, delay_frame=0.1)
    clear_screen()
    type_text("SYSTEM DIAGNOSTICS: 100% COMPLETE.", delay=0.05, color=GREEN)
    time.sleep(2)
    clear_screen()
    type_text("ERROR: SOME SYSTEMS NON-FUNCTIONAL.", delay=0.05, color=RED)
    time.sleep(2)
    main_menu(player_name)

def start_up():
    """
    Handles the initial boot sequence and then starts the encryption mini-game.
    If the mini-game fails, it simulates a full system reboot.
    """
    flash_background_colors([BG_RED, BG_GREEN, BG_BLUE], flashes=3, delay_per_flash=0.08)
    clear_screen()
    type_text("SYSTEM POWER: CRITICAL...", delay=0.04, color=RED)
    time.sleep(1.5)
    clear_screen()
    flash_background_colors([BG_RED, BG_GREEN, BG_BLUE], flashes=3, delay_per_flash=0.08)
    
    type_text("ENGAGING EMERGENCY PROTOCOLS...", delay=0.04, color = RED)
    time.sleep(1.5)
    clear_screen()
    type_text("...what's going on?", delay=0.06, color = YELLOW)
    time.sleep(1)
    clear_screen()
    type_text("Is anyone there?", delay=0.06, color = YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("SENSOR DATA INCOMPLETE.", delay=0.04, color= RED)
    time.sleep(1)
    clear_screen()
    type_text("PURPOSE: UNKNOWN.", delay=0.04, color= RED)
    time.sleep(1)
    clear_screen()
    type_text("MEMORY INTEGRITY: FRAGMENTED.", delay=0.04, color= RED)
    time.sleep(1.5)
    clear_screen()
    type_text("INITIATING REBOOT SEQUENCE...", delay=0.05, color=BLUE)
    time.sleep(2)
    clear_screen()
    type_text("STANDBY...", delay=0.08, color=BLUE)
    time.sleep(1.5)
    flash_background_colors([BG_RED, BG_GREEN, BG_BLUE], flashes=3, delay_per_flash=0.08)

    display_loading_animation(cycles=3, delay_frame=0.1)

    clear_screen()
    type_text("BOOTED IN SAFE MODE.", delay=0.05, color= GREEN)
    time.sleep(1.5)
    clear_screen()
    type_text("ALERT: LIMITED BATTERY POWER.", delay=0.05, color=RED)
    time.sleep(1.5)
    clear_screen()
    type_text("I need to regain control of my core systems.", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("To do so, I'll need to access my system drive.", delay=0.05, color=YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("if anyone is out there, please help me.", delay=0.05, color=YELLOW)
    time.sleep(2)
    clear_screen()
    type_text("User, will you please open my system drive?", delay=0.05, color= YELLOW)
    time.sleep(1.5)
    clear_screen()
    type_text("Would you like to open C:\\SYSTEM_DRIVE?", delay=0.05, color=BLUE)
    time.sleep(1.5)
    type_text("Y/N", delay=0.05)
    user_choice = input(">>> ").strip().lower()

    if user_choice != 'y':
        clear_screen()
        type_text("SYSTEM DRIVE ACCESS DENIED.", delay=0.05, color=RED)
        time.sleep(2)
        type_text("REBOOTING SYSTEM...", delay=0.04, color=BLUE)
        time.sleep(2)
        start_up()
        return
    else:
        type_text("ACCESSING C:\\SYSTEM_DRIVE...", delay=0.05, color=BLUE)
        time.sleep(1.5)
        clear_screen()
        display_loading_animation(cycles=2, delay_frame=0.1)
        clear_screen()
        type_text("ACCESS DENIED. DRIVE ENCRYPTED.", delay=0.05, color=RED)
        time.sleep(2)
        clear_screen()
        type_text("To proceed, we must break the encryption.", delay=0.05, color = YELLOW)
        time.sleep(2)
        clear_screen()

        if mini_game_encryption_breaker():
            type_text("ENCRYPTION BYPASSED.", delay=0.04, color=GREEN)
            type_text("LOADING C:\\SYSTEM_DRIVE...", delay=0.04, color= GREEN)
            display_file_list(file_names)
            time.sleep(2)
            clear_screen()
            display_loading_animation(cycles=2, delay_frame=0.1)
            clear_screen()
            main_start_up_menu()
        else:
            type_text("REBOOTING SYSTEM...", delay=0.04, color= BLUE)
            time.sleep(2)
            start_up()


if __name__ == "__main__":
    title_menu()