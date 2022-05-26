def palindrome(text):
    text_list = []
    for c in text:
        if c.isalpha():
            text_list.append(c.lower())

    reversed_list = text_list[::-1]

    if text_list == reversed_list:
        return True
    return False


def main():
    word_phrase = str(input('Enter a word or phrase to check if it is a Palindrome (Without Accent): '))
    if palindrome(word_phrase):
        print('Is a Palindrome.')
    else:
        print('Not a Palindrome.')


if __name__ == '__main__':
    main()
