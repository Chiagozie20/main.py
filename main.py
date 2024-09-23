MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '  '  # Double space to separate words
        else:
            morse_code += '? '  # Placeholder for unknown characters
    return morse_code

def morse_to_text(morse_code):
    text = ''
    words = morse_code.split('   ')  # Split by triple space to separate words
    for word in words:
        for code in word.split():
            text += REVERSE_MORSE_CODE_DICT.get(code, '?')  # Use '?' for unknown codes
        text += ' '
    return text.strip()

def main():
    while True:
        print("\nMorse Code Converter.")
        print("1. Convert text to Morse code.")
        print("2. Convert Morse code to text.")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to convert: ")
            morse_code = text_to_morse(text)
            print(f"Morse Code: {morse_code}")
        elif choice == '2':
            morse_code = input("Enter the Morse code to convert (use space to separate letters and triple space to separate words): ")
            text = morse_to_text(morse_code)
            print(f"Text: {text}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
