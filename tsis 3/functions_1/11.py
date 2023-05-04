def is_palindrom(word):
    word = str(word.lower())
    l = 0
    word = list(word)
    r = len(word)-1
    while(l<r):
        if(word[l]!=word[r]):
            return False
        else:
            l=l+1
            r=r-1
    return True

word = input()
print(is_palindrom(word))
