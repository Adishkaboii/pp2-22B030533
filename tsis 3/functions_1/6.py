def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    reversed_sentence = ' '.join(words)
    return reversed_sentence

print(reverse_sentence(input()))
