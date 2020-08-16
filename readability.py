from cs50 import get_string


def main():
    s = get_string("Text:  ")

    index = 0.0588 * ((float)(100 * count_letters(s)) / count_words(s)) - 0.296 * \
        ((float)(100 * count_sentences(s)) / count_words(s)) - 15.8

    if (index >= 1 and index <= 16):
        r = round(index)
        print(f"Grade {r}")
    elif (index < 1):
        print("Before Grade 1")
    elif (index > 16):
        print("Grade 16+")


def count_letters(text_l):
    letters = 0
    for i in text_l:
        if (i.isalpha()):
            letters += 1
    return letters


def count_words(text_w):
    words = 1
    for i in text_w:
        if i == " ":
            words += 1
    return words


def count_sentences(text_s):
    sentences = 0
    for i in text_s:
        if i == "." or i == "!" or i == "?":
            sentences += 1
    return sentences


main()