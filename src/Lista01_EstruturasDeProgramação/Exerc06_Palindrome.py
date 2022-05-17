def palindrome(word):
    # Separating the characters of the word in a list.
    word_list = []
    for c in word:
        if c.isalpha():
            word_list.append(c.lower())

    # Creating a reversed list of the word_list.
    reversed_list = word_list[::-1]

    # Checking if the lists are the same.
    if word_list == reversed_list:
        return True
    return False


def main():
    word = str(input('Enter a word or phrase to check if it is a Palindrome: '))
    if palindrome(word):
        print('Is a Palindrome.')
    else:
        print('Not a Palindrome.')


if __name__ == '__main__':
    main()
