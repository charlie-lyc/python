# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"
    return message


def is_help_command(user_input):
    result = None
    if user_input.upper() == 'HELP':
        result = True
    elif user_input.upper() == 'H':
        result = True
    else:
        result = False
    return result


def is_validated_english_sentence(user_input):
    result = None
    word_list = []
    for word in user_input.split():
        for c in word:
            if c != '.' and c != ',' and c != '!' and c != '?':
                word_list.append(c)
    new_user_input = ''.join(word_list)
    if len(user_input) != 0:
        if new_user_input.isalpha() == True:
            result = True
        else:
            result = False
    else:
        result = False
    return result


def is_validated_morse_code(user_input):
    result = None
    if len(user_input) != 0:
        for code in user_input.split():
            if 0 >= len(code) or len(code) > 4:
                result = False
                break
            nc_list = []
            for c in code:
                if c != '-' and c != '.' and c != ' ':
                    nc_list.append(c)
            if len(nc_list) != 0:
                result = False
                break
            result = True
    else:
        result = False
    return result


def get_cleaned_english_sentence(raw_english_sentence):
    word_list = []
    for word in raw_english_sentence.split():
        word_string = ''
        for c in word:
            if c != '.' and c != ',' and c != '!' and c != '?':
                word_string += c
        word_list.append(word_string)
    result = ' '.join(word_list)
    return result


def decoding_character(morse_character):
    result = None
    morse_code_dict = get_morse_code_dict()
    for k, v in morse_code_dict.items():
        if morse_character == v:
            result = k
            break
    return result


def encoding_character(english_character):
    result = None
    morse_code_dict = get_morse_code_dict()
    for k, v in morse_code_dict.items():
        if english_character == k:
            result = v
            break
    return result


def decoding_sentence(morse_sentence):
    result = ''
    morse_sentence = morse_sentence.strip()
    for code in morse_sentence.split(' '):
        if code == '':
            result += ' '
        else:
            result += decoding_character(code)
    return result


def encoding_sentence(english_sentence):
    result = ''
    english_sentence = english_sentence.strip()
    cleaned_sentence = get_cleaned_english_sentence(english_sentence)
    for c in cleaned_sentence.upper():
        if c == ' ':
            result += ' '
        else:
            result += encoding_character(c) + ' '
    return result


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        user_input = input('Input your message (H - Help, 0 - Exit) : ')
        if user_input == '0':
            break
        elif is_help_command(user_input) == True:
            print(get_help_message())
            break
        elif is_validated_english_sentence(user_input) == True:
            english_sentence = get_cleaned_english_sentence(user_input)
            print(encoding_sentence(english_sentence))
            continue
        elif is_validated_morse_code(user_input) == True:
            print(decoding_sentence(user_input))
            continue
        else:
            print('Wrong Input')
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()
