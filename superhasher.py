print("This software is licenced with MPL 2.0, by continuing you agree to the licence")
print('\nSuperHasher\nMade By ERROR#3317')
input('[Press enter to continue]')

import os
import sys
if len(sys.argv) < 2:
    print('Missing Parmeters!')
    print(f"{sys.argv[0]} <To Hash (File or Text)> <If Arg 1 Refers to Text of File (Text: 0, File: 1)>")
    exit(-1)
try:
    if sys.argv[2] == '1':
        stufftohash = open(sys.argv[1], 'rb').read()
    else:
        print('Missing Parmeters!')
        print(f"{sys.argv[0]} <To Hash (File or Text)> <If Arg 1 Refers to Text of File (Text: 0, File: 1)>")
        exit(-1)
except:
    stufftohash=sys.argv[1]
def hasher(tohash, slowness, rounds):
    tohash = str(tohash) + '\0x00\0x00'*3
    if len(tohash) < 1000:
        intified = int(str(''.join([str(ord(tohash[i])*i) for i in range(len(tohash))])))%10000
    else:
        intified = 1
        for i in range(len(tohash)):
            intified = ord(tohash[i])+i+intified
        intified = intified%10000
    answer = 0
    lim = pow(2,1024)
    addval = 1
    for _ in range(rounds):
        for char in tohash:
            addval += pow((round(ord(char)*slowness)+1)+1,intified*ord(char))
            answer += addval % (lim+addval)
            answer = answer % lim
            print(f"Current Number: {bin(answer)[2:]}\nRound Number: {_}/10")
        answer = int(bin(answer)[2:][::-1],2)
    answer = int(str(bin(answer)[2:]) + ('0'*(len(bin(lim)[2:]) - len(bin(answer)[2:]))),2)
    return f"Output: {hex(answer).upper()[2:]}"
    
print(hasher(stufftohash, 1, 10))
