wordA = input('First word: ')
wordB = input('Second word: ')

if len(wordA) == len(wordB):
    anagrams = False
    for i in range (1, len(wordA), 1):
        if wordA[i] in wordB:
            wordA.replace(wordA[i], '')
            anagrams = True
        else:
            anagrams = False
            print('They are different (different letters)')
            break
    if anagrams == True:
        print('They are anagrams!')
else:
    print('They are different (different length)')