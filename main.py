from morse_code_converter import Morse_Code_Converter

converter = Morse_Code_Converter()

decode_encode = input(
    "Do you want to decode or encode? Please write 'decode' or 'encode: "
).lower()

if decode_encode == "decode":
    morse_code = input("Please enter the morse code: ")
    encoded_text = converter.convert_morse_to_text(morse_code)
    print(f"The encoded text is: \n{encoded_text}")
elif decode_encode == "encode":
    text = input("Please enter the text: ")
    morse_code = converter.convert_text_to_morse(text)
    print(f"The morse code is: \n{morse_code}")
