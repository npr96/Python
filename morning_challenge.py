def word_reverser(word_to_reverse):
    word_container = []
    for i in word_to_reverse:
        word_container = i.split() + word_container
    word_container = map(str, word_container)
    reversed_word = ''.join(word_container)
    print(reversed_word)
word = 'people are people, so why should it be, you and I should get along so awfully?'
word_reverser(word)