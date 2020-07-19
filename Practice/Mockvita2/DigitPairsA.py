# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:23:58 2020

@author: egayu
"""
def find_number_of_pairs(l):
    bit_scores = []
    
    for number in l:
        num = [int(i) for i in str(number)]
        bitscore = (min(num)*7 + 11*max(num))%100
        if bitscore <= 9:
            bitscore = '0'+str(bitscore)
        bit_scores.append(str(bitscore))
    
    pair = 0
    pairs = []
    msb = []
    
    for i in range(len(bit_scores)):
        for j in range(i+1,len(bit_scores)):
            if bit_scores[i][0] == bit_scores[j][0]:
                
                if msb.count(bit_scores[i][0]) < 2:
                
                    if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):         
                        pair += 1
                        pairs.append([bit_scores[i],bit_scores[j]])
                        msb.append(bit_scores[i][0])
    '''
    mydict = {}
    for i in range(len(bit_scores)):
        mydict[i] = bit_score[i][0]
    '''
    
    #print(pairs)                
    #print(msb)
    return pair
    
if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    pairs = find_number_of_pairs(l)
    print(pairs)
