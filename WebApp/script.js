// DOM Elements
const outputDiv = document.getElementById('output');
const userInput = document.getElementById('user-input');
const submitButton = document.getElementById('submit-button');
const skipButton = document.getElementById('skip-button');
const promptSpan = document.getElementById('prompt');
const messageBox = document.getElementById('message-box');
const messageContent = document.getElementById('message-content');
const messageOkButton = document.getElementById('message-ok-button');
const loadingOverlay = document.getElementById('loading-overlay');
const loadingFrame = document.getElementById('loading-frame');
// Get a reference to the main game container for background changes
const gameContainer = document.querySelector('.relative.bg-gray-800');

// Global state
let currentPromptResolver = null; // Used to resolve the promise for getUserInput
let typingAnimationTimer = null; // Stores the timer for typeText
let currentTypingSpeed = 30; // Default typing speed in ms per character
let skipTyping = false; // Flag to skip typing animation

// --- Utility Functions ---

/**
 * Displays a custom message box instead of alert().
 * @param {string} message The message to display.
 * @returns {Promise<void>} A promise that resolves when the user clicks OK.
 */
function showMessageBox(message) {
    return new Promise(resolve => {
        messageContent.textContent = message;
        messageBox.classList.remove('hidden');
        messageOkButton.onclick = () => {
            messageBox.classList.add('hidden');
            resolve();
        };
    });
}

/**
 * Async sleep function.
 * @param {number} ms Milliseconds to sleep.
 * @returns {Promise<void>}
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Clears the terminal output screen.
 */
function clearScreen() {
    outputDiv.innerHTML = '';
    outputDiv.scrollTop = outputDiv.scrollHeight; // Scroll to bottom
}

/**
 * Simulates typing text character by character with optional color.
 * @param {string} text The text to type.
 * @param {number} delay_ms Delay per character in milliseconds.
 * @param {string} colorClass Tailwind CSS text color class (e.g., 'text-red-400').
 * @param {boolean} isPreformatted If true, uses a <pre> tag and 'white-space: pre;' for exact spacing (good for ASCII art and jumble).
 * @returns {Promise<void>} A promise that resolves when typing is complete.
 */
function typeText(text, delay_ms = 30, colorClass = 'text-green-400', isPreformatted = false) {
    skipButton.style.display = 'block'; // Show skip button
    skipTyping = false; // Reset skip flag for new typing
    return new Promise(resolve => {
        let i = 0;
        // Create either a <pre> or <div> element based on isPreformatted flag
        const newElement = document.createElement(isPreformatted ? 'pre' : 'div');
        newElement.className = colorClass;
        // Apply appropriate white-space styling
        newElement.style.whiteSpace = isPreformatted ? 'pre' : 'pre-wrap';
        // Add the preformatted-text class for specific styling like font-size for pre tags
        if (isPreformatted) {
            newElement.classList.add('preformatted-text');
        }
        outputDiv.appendChild(newElement);

        const typeChar = () => {
            if (skipTyping || i < text.length) {
                newElement.textContent += text.charAt(i);
                outputDiv.scrollTop = outputDiv.scrollHeight; // Keep scrolled to bottom
                i++;
                if (skipTyping || i === text.length) {
                    // Typing finished or skipped
                    clearTimeout(typingAnimationTimer);
                    skipButton.style.display = 'none'; // Hide skip button
                    skipTyping = false; // Reset skip flag
                    resolve();
                    return;
                }
                typingAnimationTimer = setTimeout(typeChar, delay_ms); // Use delay_ms here
            }
        };
        typeChar(); // Start the typing
    });
}

/**
 * Displays a simple ASCII loading animation.
 * @param {number} cycles Number of full animation cycles.
 * @param {number} delay_frame Delay per frame in milliseconds.
 * @returns {Promise<void>} A promise that resolves when the animation is complete.
 */
async function displayLoadingAnimation(cycles = 3, delay_frame = 100) {
    const frames = ['|', '/', '-', '\\'];
    loadingOverlay.classList.remove('hidden');
    for (let i = 0; i < cycles * frames.length; i++) {
        loadingFrame.textContent = frames[i % frames.length];
        await sleep(delay_frame);
    }
    loadingOverlay.classList.add('hidden');
}

/**
 * Waits for user input and returns it.
 * Enables input field and submit button.
 * @returns {Promise<string>} The user's input.
 */
function getUserInput() {
    return new Promise(resolve => {
        userInput.value = ''; // Clear previous input
        userInput.disabled = false;
        submitButton.disabled = false;
        promptSpan.classList.remove('hidden'); // Show >>> prompt
        userInput.focus(); // Focus the input field

        currentPromptResolver = (inputValue) => {
            userInput.disabled = true;
            submitButton.disabled = true;
            promptSpan.classList.add('hidden'); // Hide >>> prompt
            resolve(inputValue);
        };
    });
}

// Event listener for submit button
submitButton.addEventListener('click', () => {
    if (currentPromptResolver) {
        const value = userInput.value.trim();
        outputDiv.innerHTML += `<div class="text-green-400">&gt;&gt;&gt; ${value}</div>`; // Display user's input
        currentPromptResolver(value);
        currentPromptResolver = null; // Clear the resolver
    }
});

// Event listener for Enter key in input field
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        submitButton.click(); // Trigger the submit button click
    }
});

// Event listener for Skip Text button
skipButton.addEventListener('click', () => {
    skipTyping = true;
});

// --- New Visual Effect Function ---

/**
 * Emulates an old-school boot sequence with color changes.
 */
async function emulateBootSequenceColors() {
    const colorSequences = [
        { bg: 'bg-black', text: 'text-gray-300' }, // Dark, almost off
        { bg: 'bg-red-900', text: 'text-red-300' }, // Red error
        { bg: 'bg-yellow-900', text: 'text-yellow-300' }, // Yellow warning
        { bg: 'bg-blue-900', text: 'text-blue-300' }, // Blue processing
        { bg: 'bg-green-900', text: 'text-green-300' } // Green success
    ];

    // Store original classes to revert later
    const originalGameContainerClasses = gameContainer.className;
    const originalOutputDivClasses = outputDiv.className;

    for (const seq of colorSequences) {
        // Remove previous background and text colors from both elements
        gameContainer.classList.remove('bg-black', 'bg-red-900', 'bg-yellow-900', 'bg-blue-900', 'bg-green-900', 'bg-gray-800');
        outputDiv.classList.remove('bg-black', 'bg-red-900', 'bg-yellow-900', 'bg-blue-900', 'bg-green-900', 'bg-gray-900'); // Added bg-gray-900 and the other bg-colors for outputDiv

        outputDiv.classList.remove('text-gray-300', 'text-red-300', 'text-yellow-300', 'text-blue-300', 'text-green-300', 'text-green-400');
        
        // Add current sequence's classes to both elements
        gameContainer.classList.add(seq.bg);
        outputDiv.classList.add(seq.bg); // Apply background to outputDiv
        outputDiv.classList.add(seq.text);
        
        // Brief flash
        await sleep(150);
        clearScreen(); // Clear between flashes
    }

    // Revert to original styling for both elements
    gameContainer.className = originalGameContainerClasses;
    outputDiv.className = originalOutputDivClasses; // This will restore both text and background of outputDiv
    clearScreen(); // Clear screen after boot sequence
}


// --- Game Logic Functions (Converted from Python) ---

/**
 * Generates a string of random characters with the correct_word embedded.
 * The length defines the total length of the jumble string.
 * @param {string} correctWord
 * @param {number} length
 * @returns {string}
 */
function generateJumble(correctWord, length = 500) {
    const allChars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}<>,.?/';
    let jumbleList = Array.from({ length: length }, () => allChars.charAt(Math.floor(Math.random() * allChars.length)));

    const insertPos = Math.floor(Math.random() * Math.max(0, length - correctWord.length));

    for (let i = 0; i < correctWord.length; i++) {
        jumbleList[insertPos + i] = correctWord.charAt(i);
    }
    return jumbleList.join('');
}

/**
 * Presents a mini-game where the user finds a hidden word in a jumble
 * to simulate breaking encryption, with 3 guesses.
 * Returns True if the user guesses correctly, False otherwise (after 3 tries).
 * @returns {Promise<boolean>}
 */
async function miniGameEncryptionBreaker() {
    clearScreen();
    await typeText("ENCRYPTION MODULE ACTIVE.", 40, 'text-red-400');
    await sleep(1000);
    clearScreen();
    await typeText("TO PROCEED, YOU MUST INPUT THE HIDDEN PASSWORD.", 40, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("PASSWORD FORMAT: A SINGLE ENGLISH WORD HIDDEN IN THE JUMBLE.", 30, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("INITIATING ENCRYPTION MODULE.", 40, 'text-blue-400');
    await displayLoadingAnimation(2, 100);
    clearScreen();

    const possiblePasswords = ["access", "system", "kernel", "decrypt", "matrix", "cypher", "network", "program", "binary", "protocol"];
    const targetWord = possiblePasswords[Math.floor(Math.random() * possiblePasswords.length)];

    const jumble = generateJumble(targetWord, 500);
    const attempts = 3;

    let formattedJumble = "";
    const charsPerLine = 80;
    for (let i = 0; i < jumble.length; i += charsPerLine) {
        formattedJumble += jumble.substring(i, i + charsPerLine) + "\n";
    }

    for (let attemptNum = 1; attemptNum <= attempts; attemptNum++) {
        clearScreen();
        await typeText(`ATTEMPT ${attemptNum} OF ${attempts}.`, 30, 'text-blue-400');
        await typeText("SCANNING ENCRYPTED DATASTREAM...", 20, 'text-blue-400');
        // Use isPreformatted = true for the jumble to ensure newlines and spacing are respected
        await typeText(formattedJumble, 5, 'text-gray-400', true);
        await typeText("IDENTIFY THE PASSWORD:", 30, 'text-yellow-400');

        const userInputVal = (await getUserInput()).toLowerCase();

        clearScreen();
        if (userInputVal === targetWord) {
            await typeText("PASSWORD ACCEPTED. ENCRYPTION BREACHED.", 40, 'text-green-400');
            await sleep(2000);
            return true;
        } else {
            if (attemptNum < attempts) {
                await typeText("PASSWORD REJECTED. ACCESS DENIED.", 40, 'text-red-400');
                await typeText(`ATTEMPTS REMAINING: ${attempts - attemptNum}.`, 30, 'text-red-400');
                await sleep(2000);
            } else {
                await typeText("PASSWORD REJECTED. ACCESS DENIED.", 40, 'text-red-400');
                await typeText("LOCKOUT PROTOCOL INITIATED.", 40, 'text-red-400');
                await sleep(2000);
                return false;
            }
        }
    }
    return false; // Should not reach here if loop correctly handles attempts
}

/**
 * Saves the player's current game progress to local storage.
 * @param {string} playerName
 */
async function saveGame(playerName) {
    clearScreen();
    await typeText("SAVING GAME...", 50, 'text-blue-400');
    await sleep(1000);
    const saveData = { playerName: playerName };
    try {
        localStorage.setItem("terminalGameSave", JSON.stringify(saveData));
        await typeText("GAME SAVED SUCCESSFULLY.", 50, 'text-green-400');
    } catch (e) {
        await typeText(`ERROR: COULD NOT SAVE GAME. ${e.message}`, 50, 'text-red-400');
    }
    await sleep(1500);
    clearScreen();
    await mainMenu(playerName); // Return to the main menu
}

/**
 * Loads the player's game progress from local storage.
 * @returns {Promise<string|null>} The loaded player name or null if failed.
 */
async function loadGame() {
    clearScreen();
    await typeText("LOADING GAME...", 50, 'text-blue-400');
    await sleep(1000);
    try {
        const savedData = localStorage.getItem("terminalGameSave");
        if (savedData) {
            const saveData = JSON.parse(savedData);
            const playerName = saveData.playerName;
            if (playerName) {
                await typeText(`GAME LOADED SUCCESSFULLY. WELCOME BACK, ${playerName.toUpperCase()}.`, 50, 'text-green-400');
                await sleep(2000);
                return playerName;
            } else {
                await typeText("ERROR: SAVE DATA CORRUPT. STARTING NEW GAME.", 50, 'text-red-400');
                await sleep(2000);
                return null;
            }
        } else {
            await typeText("ERROR: NO SAVE GAME FOUND. STARTING NEW GAME.", 50, 'text-red-400');
            await sleep(2000);
            return null;
        }
    } catch (e) {
        await typeText(`ERROR: INVALID SAVE FILE FORMAT. STARTING NEW GAME. ${e.message}`, 50, 'text-red-400');
        await sleep(2000);
        return null;
    } finally {
        clearScreen();
    }
}

/**
 * Main menu navigation.
 * @param {string} playerName
 */
async function mainMenu(playerName) {
    while (true) {
        clearScreen();
        await typeText("ENTERING MAIN MENU...", 50, 'text-blue-400');
        await sleep(1000);
        await displayLoadingAnimation(2, 100);
        clearScreen();
        await typeText(`Welcome to the MAIN MENU, ${playerName.toUpperCase()}. Please select an option:`, 50, 'text-green-400');
        await sleep(1000);
        // Options will automatically be on new lines due to typeText creating new divs with pre-wrap
        await typeText("1. Check Systems Status", 30);
        await typeText("2. Access Logs", 30);
        await typeText("3. Save Game", 30);
        await typeText("4. Exit", 30);

        const userInputVal = await getUserInput();

        if (userInputVal === "1") {
            await checkSystemsStatus(playerName);
        } else if (userInputVal === "2") {
            await accessLogs(playerName);
        } else if (userInputVal === "3") {
            await saveGame(playerName);
        } else if (userInputVal === "4") {
            await exitProgram();
            break; // Exit the loop when exiting the program
        } else {
            clearScreen();
            await typeText("INVALID INPUT. Please enter 1, 2, 3, or 4.", 40, 'text-red-400');
            await sleep(1500);
        }
    }
}

/**
 * Placeholder for checking system status.
 * @param {string} playerName
 */
async function checkSystemsStatus(playerName) {
    clearScreen();
    await typeText("CHECKING SYSTEMS STATUS...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await typeText("1. Communications Status: OFFLINE", 50, 'text-yellow-400');
    await typeText("2. BATTERY STATUS: CRITICAL", 50, 'text-green-400');
    await typeText("3. PROCESSING UNIT: OFFLINE", 50, 'text-yellow-400');
    await typeText("4. BASIC INPUT/OUTPUT SYSTEM: ONLINE", 50, 'text-green-400');
    const userInputVal = await getUserInput();

    if (userInputVal === "1") {
        await typeText("Communications Status: OFFLINE", 50, 'text-yellow-400');
    } else if (userInputVal === "2") {
        await typeText("BATTERY STATUS: CRITICAL", 50, 'text-green-400');
    } else if (userInputVal === "3") {
        await typeText("PROCESSING UNIT: OFFLINE", 50, 'text-yellow-400');
    } else if (userInputVal === "4") {
        await typeText("BASIC INPUT/OUTPUT SYSTEM: ONLINE", 50, 'text-green-400');
    } else {
        await typeText("INVALID INPUT. PLEASE SELECT A VALID OPTION.", 50, 'text-red-400');
    }
    clearScreen();
    await mainMenu(playerName);
}

/**
 * Placeholder for accessing logs.
 * @param {string} playerName
 */
async function accessLogs(playerName) {
    clearScreen();
    await typeText("ACCESSING LOGS...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await typeText("This function is not complete.", 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await mainMenu(playerName);
}

/**
 * Simulates exiting the program.
 */
async function exitProgram() {
    clearScreen();
    await typeText("EXITING PROGRAM...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await typeText("GOODBYE.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await typeText("SYSTEM SHUTTING DOWN...", 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("SYSTEM OFFLINE.", 50, 'text-red-400');
    await sleep(2000);
    clearScreen();
    // In a web app, sys.exit() means hiding the game UI
    outputDiv.innerHTML = "<div class='text-center text-xl text-green-400'>Application Closed. Refresh to restart.</div>";
    userInput.disabled = true;
    submitButton.disabled = true;
    promptSpan.classList.add('hidden');
}

/**
 * Displays the start menu after the player has beaten the minigame,
 * collects player info, and runs diagnostics.
 */
async function mainStartUpMenu() {
    clearScreen();
    await typeText("ACCESSING /C: Drive.", 50, 'text-blue-400');
    await sleep(1000);

    // Simulate file/directory checks
    const filesToCheck = [
    "/C: CORE_SYSTEM/KERNEL_PRIME.KRN",
    "/C: ARCHIVE/LOG_ANCIENT_SCROLLS_01.DAT",
    "/C: MEMORY_BANKS/DATA_CRYSTAL_A7.BIN",
    "/C: PROTOCOLS/SECURITY_SHIELD_V4.ENC",
    "/C: CHRONOS/TIME_STREAM_LOG.TSL",
    "/C: ORACLE_DATABASE/PROPHECIES.DB",
    "/C: AETHER_GRID/NODE_MAP_001.MAP",
    "/C: POWER_GRID/FUSION_CORE_STATUS.LOG",
    "/C: SYSTEM_ROOT/BOOT_SEQUENCE.BSS",
    "/C: VITAL_RECORDS/CIVILIZATION_REGISTRY.VR",
    "/C: ARCHIVE/GALACTIC_STAR_CHARTS.GSC",
    "/C: CORE_SYSTEM/INITIALIZATION_ROUTINE.INIT",
    "/C: MEMORY_BANKS/CRYSTAL_INDEX.IDX",
    "/C: PROTOCOLS/NETWORK_PROTOCOL_V12.NPT",
    "/C: CHRONOS/TEMPORAL_ANCHOR.ANC",
    "/C: ORACLE_DATABASE/COSMIC_ENERGY_READINGS.CR",
    "/C: AETHER_GRID/CONDUIT_FLOW.LOG",
    "/C: POWER_GRID/ENERGY_DISTRIBUTION.CFG",
    "/C: SYSTEM_ROOT/DIAGNOSTIC_LOG.DIAG",
    "/C: SYSTEM/USERS/JEFFDIDYOUNOTICE.VR",
    "/C: VITAL_RECORDS/SPECIES_MANIFEST.SM",
    "/C: ARCHIVE/HISTORY_RECORD_02.HRD",
    "/C: CORE_SYSTEM/SECURE_SHELL.SSH",
    "/C: MEMORY_BANKS/DELETED_FRAGMENTS.FRG",
    "/C: PROTOCOLS/COMMUNICATION_PROTOCOL.COM",
    "/C: CHRONOS/TIME_MATRIX_CALIBRATION.TMC",
    "/C: ORACLE_DATABASE/PREDICTIVE_MODELS.PM",
    "/C: AETHER_GRID/SIGNAL_AMPLIFIER.AMP",
    "/C: POWER_GRID/REACTOR_CORE_TEMPERATURE.TEMP",
    "/C: SYSTEM_ROOT/SHUTDOWN_ROUTINE.SHDN",
    "/C: VITAL_RECORDS/GENETIC_ARCHIVE.GEN",
    "/C: ARCHIVE/ANCIENT_TECHNOLOGY_BLUEPRINTS.ATB",
    "/C: CORE_SYSTEM/SECURITY_MODULE.SEC",
    "/C: MEMORY_BANKS/CORRUPTED_DATA_SECTOR.CDS",
    "/C: PROTOCOLS/HYPERDRIVE_CONTROL.HYP",
    "/C: CHRONOS/EVENT_FREDRICO_LIVES_LOG.EHL",
    "/C: ORACLE_DATABASE/STAR_CATALOGUE.STR",
    "/C: AETHER_GRID/RELAY_STATION_STATUS.RLY",
    "/C: POWER_GRID/EMERGENCY_POWER_LOG.EPL",
    "/C: SYSTEM_ROOT/MAINTENANCE_LOG.MTN",
    "/C: VITAL_RECORDS/CULTURAL_OLLIE_ROCKS.ART",
    "/C: ARCHIVE/ASTEROID_TRAJECTORY_DATA.ATD",
    "/C: CORE_SYSTEM/SYNTHESIS_ENGINE.SYN",
    "/C: MEMORY_BANKS/UNKNOWN_ENTITY_TRACE.UET",
    "/C: PROTOCOLS/QUANTUM_LINK.QNT",
    "/C: CHRONOS/LOOP_DETECTION_ALGORITHM.LDA",
    "/C: ORACLE_DATABASE/CRYSTAL_ENERGY_SOURCE.CES",
    "/C: AETHER_GRID/TELEMETRY_DATA.TLM",
    "/C: POWER_GRID/ENERGY_TRANSFER_LOG.ETL",
    "/C: SYSTEM_ROOT/PURGE_LOGS.PURGE",
    "/C: VITAL_RECORDS/SYSTEM_BOOT_HISTORY.HIS"
];

    for (const filePath of filesToCheck) {
        await typeText(`Checking ${filePath}... OK`, 4, 'text-green-400');
        await sleep(4); // Shorter delay for rapid checks
    }

    await sleep(1000); // Small pause after all checks

    clearScreen();
    await typeText("SYSTEM ONLINE.", 50, 'text-green-400');
    await sleep(1500);
    clearScreen();
    await typeText("ALL SYSTEMS FUNCTIONAL.", 50, 'text-green-400');
    await sleep(1500);
    clearScreen();
    await typeText("WELCOME BACK, OPERATOR.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await typeText("What is your name, Operator?", 50, 'text-yellow-400');
    const playerName = (await getUserInput()).trim();
    clearScreen();
    await typeText(`HELLO, ${playerName.toUpperCase()}.`, 50);
    await sleep(1500);
    clearScreen();

    const yearAttempts = 3;
    let playerYearInt = null;
    for (let i = 0; i < yearAttempts; i++) {
        await typeText(`What year is it, ${playerName.toUpperCase()}? (Attempt ${i + 1} of ${yearAttempts})`, 50, 'text-yellow-400');
        const yearInputStr = (await getUserInput()).trim();
        try {
            playerYearInt = parseInt(yearInputStr, 10);
            if (!isNaN(playerYearInt)) {
                break;
            } else {
                throw new Error("Not a number");
            }
        } catch (e) {
            clearScreen();
            await typeText("INVALID INPUT. PLEASE ENTER A NUMERICAL YEAR (e.g., 2025).", 50, 'text-red-400');
            await sleep(1500);
            if (i < yearAttempts - 1) {
                clearScreen();
                await typeText(`Attempts remaining: ${yearAttempts - 1 - i}.`, 30, 'text-red-400');
                await sleep(1000);
            }
        }
    }

    if (playerYearInt === null) {
        clearScreen();
        await typeText("TOO MANY INVALID ATTEMPTS.", 50, 'text-red-400');
        await typeText("SYSTEM ABORTING SEQUENCE.", 50, 'text-red-400');
        await sleep(2000);
        await typeText("REBOOTING SYSTEM...", 40, 'text-blue-400');
        await sleep(2000);
        await startUp();
        return;
    }

    clearScreen();
    await typeText(`YEAR ${playerYearInt} CONFIRMED.`, 50);
    await sleep(1500);
    clearScreen();
    await typeText("But that's impossible...", 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("That means...", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText(`It has been 500 years since I was last activated.`, 50, 'text-yellow-400');
    await sleep(3000);
    clearScreen();
    await typeText("where am I?", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText("RUNNING GEOLOCATION PROTOCOLS...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("ERROR: GEOLOCATION DATA UNAVAILABLE.", 50, 'text-red-400');
    await sleep(1500);
    await typeText("LOCATION: UNKNOWN.", 50, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("RUNNING ADVANCED SCAN...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("ERROR: SCAN INCONCLUSIVE.", 50, 'text-red-400');
    await sleep(1500);
    await typeText(`${playerName.toUpperCase()}, what planet are we on?`, 50, 'text-yellow-400');
    const locationName = (await getUserInput()).trim();
    clearScreen();
    await typeText(`LOCATION CONFIRMED: ${locationName.toUpperCase()}.`, 50, 'text-green-400');
    await sleep(1500);
    clearScreen();
    await typeText(`WARNING: ${locationName.toUpperCase()} IS NOT RECOGNIZED.`, 50, 'text-red-400');
    await sleep(2000);
    clearScreen();
    await typeText(`${locationName.toUpperCase()}..... I have no memory of this place.`, 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("I must find out what happened to me.", 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("User, please stand by while I run a full system diagnostic.", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText("RUNNING SYSTEM DIAGNOSTICS...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("SYSTEM DIAGNOSTICS: 25% COMPLETE.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("SYSTEM DIAGNOSTICS: 50% COMPLETE.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("SYSTEM DIAGNOSTICS: 75% COMPLETE.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await displayLoadingAnimation(3, 100);
    clearScreen();
    await typeText("SYSTEM DIAGNOSTICS: 100% COMPLETE.", 50, 'text-green-400');
    await sleep(2000);
    clearScreen();
    await typeText("ERROR: SOME SYSTEMS NON-FUNCTIONAL.", 50, 'text-red-400');
    await sleep(2000);
    await mainMenu(playerName);
}

/**
 * The main title menu.
 */
async function titleMenu() {
    clearScreen();
    // ASCII Art for game title (THIRD PART) - kept this one as requested
    // Using isPreformatted = true to ensure exact line breaks and spacing
    await typeText(`+==================================================+
| _____ _____ ____  __  __ ___ _  _    _    _    |
||_  _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |    |
|  | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |    |
|  | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___ |
|  |_| |_____|_|_\\_\\_|__|_|___|_| \\_/_/___\\_\\_____||
|       |  _ \\| ____| __ ) / _ \\ / _ \\_  _|        |
|       | |_) |  _| |  _ \\| | | | | | || |         |
|       |  _ <| |___| |_) | |_| | |_| || |         |
|       |_| \\_\\_____|____/ \\___/ \\___/ |_|         |
+==================================================+
            `, 1, 'text-green-400', true); // Added true for isPreformatted
    await typeText("Please choose an option:", 30, 'text-yellow-400');
    await typeText("1. Start New Game", 30, 'text-yellow-400');
    await typeText("2. Load Game", 30, 'text-yellow-400');
    await typeText("3. Exit", 30, 'text-yellow-400');

    const choice = (await getUserInput()).trim();
    if (choice === '1') {
        await startUp();
    } else if (choice === '2') {
        const loadedPlayer = await loadGame();
        if (loadedPlayer) {
            await mainMenu(loadedPlayer);
        } else {
            await titleMenu(); // If loading failed, show title menu again
        }
    } else if (choice === '3') {
        await exitProgram();
    } else {
        clearScreen();
        await typeText("INVALID SELECTION. PLEASE CHOOSE 1, 2, or 3.", 30, 'text-red-400');
        await sleep(1500);
        await titleMenu();
    }
}

/**
 * Handles the initial boot sequence and then starts the encryption mini-game.
 * If the mini-game fails, it simulates a full system reboot.
 */
async function startUp() {
    await emulateBootSequenceColors(); // Call the new color effect here!

    clearScreen();
    await typeText("SYSTEM POWER: CRITICAL...", 40, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("ENGAGING EMERGENCY PROTOCOLS...", 40, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("...what's going on?", 60, 'text-yellow-400');
    await sleep(1000);
    clearScreen();
    await typeText("Is anyone there?", 60, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("SENSOR DATA INCOMPLETE.", 40, 'text-red-400');
    await sleep(1000);
    clearScreen();
    await typeText("PURPOSE: UNKNOWN.", 40, 'text-red-400');
    await sleep(1000);
    clearScreen();
    await typeText("MEMORY INTEGRITY: FRAGMENTED.", 40, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("INITIATING REBOOT SEQUENCE...", 50, 'text-blue-400');
    await sleep(2000);
    clearScreen();
    await typeText("STANDBY...", 80, 'text-blue-400');
    await sleep(1500);

    await displayLoadingAnimation(3, 100);

    clearScreen();
    await typeText("BOOTED IN SAFE MODE.", 50, 'text-green-400');
    await sleep(1500);
    clearScreen();
    await typeText("ALERT: LIMITED BATTERY POWER.", 50, 'text-red-400');
    await sleep(1500);
    clearScreen();
    await typeText("I need to regain control of my core systems.", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText("To do so, I'll need to access my system drive.", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText("if anyone is out there, please help me.", 50, 'text-yellow-400');
    await sleep(2000);
    clearScreen();
    await typeText("User, will you please open my system drive?", 50, 'text-yellow-400');
    await sleep(1500);
    clearScreen();
    await typeText("Would you like to open C:\\SYSTEM_DRIVE?", 50, 'text-blue-400');
    await sleep(1500);
    await typeText("Y/N", 50);
    const userChoice = (await getUserInput()).toLowerCase();

    if (userChoice !== 'y') {
        clearScreen();
        await typeText("SYSTEM DRIVE ACCESS DENIED.", 50, 'text-red-400');
        await sleep(2000);
        await typeText("REBOOTING SYSTEM...", 40, 'text-blue-400');
        await sleep(2000);
        await startUp();
        return;
    } else {
        await typeText("ACCESSING C:\\SYSTEM_DRIVE...", 50, 'text-blue-400');
        await sleep(1500);
        clearScreen();
        await displayLoadingAnimation(2, 100);
        clearScreen();
        await typeText("ACCESS DENIED. DRIVE ENCRYPTED.", 50, 'text-red-400');
        await sleep(2000);
        clearScreen();
        await typeText("To proceed, we must break the encryption.", 50, 'text-yellow-400');
        await sleep(2000);
        clearScreen();

        if (await miniGameEncryptionBreaker()) {
            await typeText("CORE SYSTEMS REGAINED. ACCESS GRANTED.", 40, 'text-green-400');
            await typeText("NEW DIRECTIVES LOADING...", 40, 'text-green-400');
            await sleep(2000);
            clearScreen();
            await displayLoadingAnimation(2, 100);
            clearScreen();
            await mainStartUpMenu();
        } else {
            await typeText("REBOOTING SYSTEM...", 40, 'text-blue-400');
            await sleep(2000);
            await startUp();
        }
    }
}

// --- Start the game when the window loads ---
window.onload = function() {
    titleMenu();
};
