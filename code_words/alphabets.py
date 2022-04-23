import importlib.resources

import code_words.data


def base32():
    return "abcdefghijklmnopqrstuvwxyz234567"


def zbase32():
    return "ybndrfg8ejkmcpqxot1uwisza345h769"


def base32hex():
    return "0123456789abcdefghijklmnopqrstuv"


def base58():
    return "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base62():
    return "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def words1024():
    return [word.strip() for word in importlib.resources.open_text(code_words.data, "words_1024.txt")]


def words2048():
    return [word.strip() for word in importlib.resources.open_text(code_words.data, "words_2048.txt")]


def words4096():
    return [word.strip() for word in importlib.resources.open_text(code_words.data, "words_4096.txt")]


def words65536():
    return [word.strip() for word in importlib.resources.open_text(code_words.data, "words_65536.txt")]