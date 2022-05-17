def palindrome(word):
    # Separating the characters of the word in a list.
    word_list = []
    for c in word:
        word_list.append(c.lower())

    # Creating a reversed list of the word_list.
    reversed_list = word_list[::-1]

    # Checking if the lists are the same.
    if word_list == reversed_list:
        return True
    return False

