# dictionaries for morse code conversion

# text to morse code
text_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    6: "-....",
    7: "--...",
    8: "---..",
    9: "----.",
    # Punctuation
    ", ": "--..--",
    ". ": ".-.-.-",
    "? ": "..--..",
    "/ ": "-..-.",
    "- ": "-....-",
    "(": "-.--.",
    ") ": "-.--.-",
}

# morse code to text
morse_to_text = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "/": " ",
}


class Morse_Code_Converter:
    def __init__(self):
        self.text_to_morse = text_to_morse
        self.morse_to_text = morse_to_text

    def convert_text_to_morse(self, text):
        """Convert text to morse code"""
        converted_text = ""
        for char in text:
            if char.upper() in self.text_to_morse:
                converted_text += self.text_to_morse[char.upper()] + " "
            else:
                converted_text += char + " "
            if char == " ":
                converted_text += " / "  # space in morse code
        return converted_text

    def convert_morse_to_text(self, morse_code):
        """Convert morse code to text"""
        words = morse_code.strip().split(" ")
        decoded_text = ""
        for word in words:
            decoded_text += self.morse_to_text[word]
        return decoded_text
