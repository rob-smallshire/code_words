from code_words import alphabets


def encode(num, separator, alphabet_name):
    alphabet = load_alphabet(alphabet_name)
    digits = encode_in_alphabet(num, alphabet)
    return separator.join(digits)


def encode_in_alphabet(num, alphabet):
    """Encode a positive number in Base X

    Args:
        num: The number to encode
        alphabet: The alphabet to use for encoding
        
    Returns:
        A sequence of "digits", each taken from alphabet.
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num != 0:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return arr



def decode_from_alphabet(digits, alphabet):
    """Decode a Base X encoded string into the number

    Args:
        digits: A sequence of "digits" where each digit is an element from alphabet
        alphabet: The alphabet sequence to use for encoding
    """
    num = 0
    base = len(alphabet)
    lookup = {item: index for index, item in enumerate(alphabet)}    
    for position, symbol in enumerate(reversed(digits)):
        place_value = base ** position
        digit = lookup[symbol]
        num += place_value * digit
    return num


def alphabet_names():
    return [name for name in dir(alphabets) if not name.startswith("_")]


def load_alphabet(name):
    return getattr(alphabets, name)()
