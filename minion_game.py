#Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules

#Both players are given the same string,S.
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.

#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.

#For Example:
#String S= BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#Your task is to determine the winner of the game and their score.

#Input Format
#A single line of input containing the string .
#Note: The string  will contain only uppercase letters: .

#Constraints
#0<len(S)<=10^6

#Output Format
#Print one line: the name of the winner and their score separated by a space.
#If the game is a draw, print Draw.

#CODE
def minion_game(string):
    length=len
    stuw= list()
    kevw= list()
    masterset = list()
    count = length(string)
    for letter in string:
        if letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
            pos = string.find(letter)
            fakestring = string[pos:]
            for i in range(length(fakestring)):
                word = fakestring[:i+1]
                if word in kevw:continue
                kevw.append(word)
        if letter!='A' and letter!='E' and letter!='I' and letter!='O' and letter!='U':
            pos = string.find(letter)
            fakestring = string[pos:]
            for i in range(length(fakestring)):
                word = fakestring[:i+1]
                if word in stuw:continue
                stuw.append(word)
        for i in range(count):
            word = fakestring[:i+1]
            masterset.append(word)
        count = count - 1
    stu = 0
    kev = 0

    for i in range(length(masterset)):
        if masterset[i] in stuw: stu = stu + 1
    for i in range(length(masterset)):
        if masterset[i] in kevw: kev = kev + 1
    
    if kev<stu :print('Stuart',stu)
    elif kev>stu:print('Kevin',kev)
    else :print('Draw')
    
