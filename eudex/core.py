# Author: Rémi Adon <remi.adon@gmail.com>
# License: BSD 3 clause


def binary_to_int(b):
    if isinstance(b, int):
        return b
    else:
        return int(b, 2)


def char_code(s, idx=0):
    return ord(s[idx])


PHONES = [
    #  +--------- Confident
    #  |+-------- Labial
    #  ||+------- Liquid
    #  |||+------ Dental
    #  ||||+----- Plosive
    #  |||||+---- Fricative
    #  ||||||+--- Nasal
    #  |||||||+-- Discriminant
    #  ||||||||
    "0",  # a
    "01001000",  # b
    "00001100",  # c
    "00011000",  # d
    "0",  # e
    "01000100",  # f
    "00001000",  # g
    "00000100",  # h
    "1",  # i
    "00000101",  # j
    "00001001",  # k
    "10100000",  # l
    "00000010",  # m
    "00010010",  # n
    "0",  # o
    "01001001",  # p
    "10101000",  # q
    "10100001",  # r
    "00010100",  # s
    "00011101",  # t
    "1",  # u
    "01000101",  # v
    "00000000",  # w
    "10000100",  # x
    "1",  # y
    "10010100",  # z
]

PHONES = list(map(binary_to_int, PHONES))

LETTERS = len(PHONES)

PHONES_C1 = [
    PHONES[char_code("s") - char_code("a")] ^ 1,  #  ß
    "0",  #  à
    "0",  #  á
    "0",  #  â
    "0",  #  ã
    "0",  #  ä [æ]
    "1",  #  å [oː]
    "0",  #  æ [æ]
    PHONES[char_code("z") - char_code("a")] ^ 1,  #  ç [t͡ʃ]
    "1",  #  è
    "1",  #  é
    "1",  #  ê
    "1",  #  ë
    "1",  #  ì
    "1",  #  í
    "1",  #  î
    "1",  #  ï
    "00010101",  #  ð [ð̠] (represented as a non-plosive T)
    "00010111",  #  ñ [nj] (represented as a combination of n and j)
    "0",  #  ò
    "0",  #  ó
    "0",  #  ô
    "0",  #  õ
    "1",  #  ö [ø]
    "1",  #  ÷
    "1",  #  ø [ø]
    "1",  #  ù
    "1",  #  ú
    "1",  #  û
    "1",  #  ü
    "1",  #  ý
    "00010101",  #  þ [ð̠] (represented as a non-plosive T)
    "1",  #  ÿ
]

PHONES_C1 = list(map(binary_to_int, PHONES_C1))

INJECTIVE_PHONES = [
    #  +--------- Vowel
    #  |+-------- Closer than ɜ
    #  ||+------- Close
    #  |||+------ Front
    #  ||||+----- Close-mid
    #  |||||+---- Central
    #  ||||||+--- Open-mid
    #  |||||||+-- Discriminant
    #  ||||||||   (*=vowel)
    "10000100",  # a*
    "00100100",  # b
    "00000110",  # c
    "00001100",  # d
    "11011000",  # e*
    "00100010",  # f
    "00000100",  # g
    "00000010",  # h
    "11111000",  # i*
    "00000011",  # j
    "00000101",  # k
    "01010000",  # l
    "00000001",  # m
    "00001001",  # n
    "10010100",  # o*
    "00100101",  # p
    "01010100",  # q
    "01010001",  # r
    "00001010",  # s
    "00001110",  # t
    "11100000",  # u*
    "00100011",  # v
    "00000000",  # w
    "01000010",  # x
    "11100100",  # y*
    "01001010",  # z
]

INJECTIVE_PHONES = list(map(binary_to_int, INJECTIVE_PHONES))


INJECTIVE_PHONES_C1 = [
    #  +--------- Vowel
    #  |+-------- Closer than ɜ
    #  ||+------- Close
    #  |||+------ Front
    #  ||||+----- Close-mid
    #  |||||+---- Central
    #  ||||||+--- Open-mid
    #  |||||||+-- Discriminant
    #  ||||||||
    INJECTIVE_PHONES[char_code("s") - char_code("a")] ^ 1,  # ß
    INJECTIVE_PHONES[char_code("a") - char_code("a")] ^ 1,  # à
    INJECTIVE_PHONES[char_code("a") - char_code("a")] ^ 1,  # á
    "10000000",  # â
    "10000110",  # ã
    "10100110",  # ä [æ]
    "11000010",  # å [oː]
    "10100111",  # æ [æ]
    "01010100",  # ç [t͡ʃ]
    INJECTIVE_PHONES[char_code("e") - char_code("a")] ^ 1,  # è
    INJECTIVE_PHONES[char_code("e") - char_code("a")] ^ 1,  # é
    INJECTIVE_PHONES[char_code("e") - char_code("a")] ^ 1,  # ê
    "11000110",  # ë [ə] or [œ]
    INJECTIVE_PHONES[char_code("i") - char_code("a")] ^ 1,  # ì
    INJECTIVE_PHONES[char_code("i") - char_code("a")] ^ 1,  # í
    INJECTIVE_PHONES[char_code("i") - char_code("a")] ^ 1,  # î
    INJECTIVE_PHONES[char_code("i") - char_code("a")] ^ 1,  # ï
    "00001011",  # ð [ð̠] (represented as a non-plosive T)
    "00001011",  # ñ [nj] (represented as a combination of n and j)
    INJECTIVE_PHONES[char_code("o") - char_code("a")] ^ 1,  # ò
    INJECTIVE_PHONES[char_code("o") - char_code("a")] ^ 1,  # ó
    INJECTIVE_PHONES[char_code("o") - char_code("a")] ^ 1,  # ô
    INJECTIVE_PHONES[char_code("o") - char_code("a")] ^ 1,  # õ
    "11011100",  # ö [œ] or [ø]
    "1",  # ÷
    "11011101",  # ø [œ] or [ø]
    INJECTIVE_PHONES[char_code("u") - char_code("a")] ^ 1,  # ù
    INJECTIVE_PHONES[char_code("u") - char_code("a")] ^ 1,  # ú
    INJECTIVE_PHONES[char_code("u") - char_code("a")] ^ 1,  # û
    INJECTIVE_PHONES[char_code("y") - char_code("a")] ^ 1,  # ü
    INJECTIVE_PHONES[char_code("y") - char_code("a")] ^ 1,  # ý
    "00001011",  # þ [ð̠] (represented as a non-plosive T)
    INJECTIVE_PHONES[char_code("y") - char_code("a")] ^ 1,  # ÿ
]

INJECTIVE_PHONES_C1 = list(map(binary_to_int, INJECTIVE_PHONES_C1))

A = char_code("a")
Z = char_code("z")


def eudex(sequence):
    """
    Apply eudex on the input string and return the result as a left-padded binary representation
    The result is a hash

    Warning: numerical distance cannot be applied on that hash, `eudex(a) - eudex(b)` has no sense
    Rather, one should apply hamming distance on the binary representation

    Parameters
    ----------
    sequence: string
       input string

    Examples
    --------
    >>>> eudex('Jeff Buckley')
    235392249864232960
    >>>> eudex('Tim Buckley')
    1009448435818536960
    >>> bin(eudex('Jeff Buckley'))[-20:] == bin(eudex('Tim Buckley'))[-20:] # check last 20 bits
    True

    Returns
    -------
    res : str
    """
    entry = ((char_code(sequence) | 32) - A) & 0xFF if sequence else 0
    first_byte = 0
    if entry < LETTERS:
        first_byte = INJECTIVE_PHONES[entry]
    else:
        if 0xDF <= entry < 0xFF:
            first_byte = INJECTIVE_PHONES_C1[entry - 0xDF]

    res, n, b = 0, 0, 1

    while n < 8 and b < len(sequence):
        entry = ((char_code(sequence, idx=b) | 32) - A) & 0xFF

        if entry <= Z:
            x = 0
            if entry < LETTERS:
                x = PHONES[entry]
            elif 0xDF <= entry < 0xFF:
                x = PHONES_C1[entry - 0xDF]
            else:
                b += 1
                continue

            if (res & 0xFE) != (x & 0xFE):
                res = res << 8
                res |= x
                n += 1

        b += 1

    return res | (first_byte << 56)

