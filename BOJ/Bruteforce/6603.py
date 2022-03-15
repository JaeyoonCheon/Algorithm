"""
6603번 로또
"""

import itertools

def checkUpper(lottoCase):
    for i in range(len(lottoCase)-1):
        if lottoCase[i] > lottoCase[i+1]:
            return False
        
    return True

while True:
    lotto = list(map(int, input().split()))
    length = lotto.pop(0)
    if length == 0:
        break
    for i in itertools.permutations(lotto, 6):
        if checkUpper(i):
            for j in i:
                print(j, end=" ")
            print("")
            
    print("")
        
    
    