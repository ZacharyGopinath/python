# DID NOT FINISH QUESTION
# DID NOT FINISH QUESTION
# DID NOT FINISH QUESTION

#AFB+8HC-4
'''
start = 'asdf=5;'
end = '123jasd'
s = 'asdf=5;iwantthis123jasd'
print s[s.find(start)+len(start):s.rfind(end)]
'''
#quite messy
def tuner():
    instr  = input()
    '''
    stringsA = instr.split('+')[0]
    plusMinusA = instr.split('+')[1][0]
    valA = instr.split(plusMinusA)[0][-1]
    stringsB = instr.split(plusMinusA)[1]
    valB1 = stringsB[-2]
    stringsB1 = stringsB.split('-')[0]
    valB = instr.split('-')[1]

    print(stringsA, valA, plusMinusA)
    print(stringsB1, valB1, valB)
    '''
    lettersA = instr.split('+')[0]
    lettersB = instr.split('+')[1]
    numB = instr.split('-')[1]
    



    newLettersB = (lettersB.replace('-'+numB, ' '))
    #strB = (lettersB.replace('-'+numB, ' '))
    newLettersB = " ".join(newLettersB)

    numA = ([int(i) for i in newLettersB.split() if i.isdigit()])
    numA =  str(numA[-1])
    #lettersB = strB.replace(numA, " ")
    #finalLettersB = ''.join(newLettersB)
    newLettersB = newLettersB.replace(' ', '')
    finalLettersB = newLettersB.replace(numA, '')
    print(lettersA, 'tighten', numA)
    print(finalLettersB, 'loosen', numB)
tuner()