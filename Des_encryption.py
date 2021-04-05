# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:59:02 2021

@author: Raza_Jutt
mail: muhammadrazaali.raza@gmail.com
"""
plain_text  =[1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1, 1,1,1,1,0,0,1,0]
key = [0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1]
pcindex = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
pc2index =[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
ip = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,56,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
per = [ 16,  7, 20, 21,29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2,  8, 24, 14,32, 27,  3,  9, 19, 13, 30,  6,22, 11,  4, 25 ]
sbox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],    
         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]], 
         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
               39, 7, 47, 15, 55, 23, 63, 31, 
               38, 6, 46, 14, 54, 22, 62, 30, 
               37, 5, 45, 13, 53, 21, 61, 29, 
               36, 4, 44, 12, 52, 20, 60, 28, 
               35, 3, 43, 11, 51, 19, 59, 27, 
               34, 2, 42, 10, 50, 18, 58, 26, 
               33, 1, 41,  9, 49, 17, 57, 25 ]

def placement(place,index):
    ary_placed = []
    for i in place:
        ary_placed.append(index[i-1])
    return ary_placed

def converting(num,ary):
    c = ary[:num]
    d = ary[num:]
    return c,d

def printing(ary):
    counter = 0
    for i in ary:
        if counter == 7 and (len(ary)==56 or len(ary)==28):
            print(" ",end="")
            counter= 0
        if counter == 8 and (len(ary)==64 or len(ary)==32 or len(ary)==48):
            print(" ",end="")
            counter= 0
        counter = counter + 1
        print(i,end="")
    print("")
    return

def shift(num,ary):
    if num > 1:
        ary = shift(1,ary)
    a = ary[0]
    shifted = []
    for i in range(1,len(ary)):
        shifted.append(ary[i])
    shifted.append(a)
    return shifted

def shifting(ary):
    temp_ary = ary
    list_ary = [ary]
    for i in range(1,17):
        if i<3 or i==16:
            temp_ary = shift(1,temp_ary)
            list_ary.append(temp_ary)
        else:
            temp_ary = shift(2,temp_ary)
            list_ary.append(temp_ary)
    return list_ary

def convert28_28to56(ary1,ary2):
    for i in ary2:
        ary1.append(i)
    return ary1

def xor(ary1,ary2):
    ary = []
    for i in range(0,len(ary1)):
        if ary1[i]==ary2[i]:
            ary.append(0)
        else:
            ary.append(1)
    return ary

def bin2dec(binary):   
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def dec2bin(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def bin32(ary):
    bin32 =[]
    for i in ary:
        a = dec2bin(i)
        l = len(a)
        b = 4-l
        for i in range(0,b):
            bin32.append(0)
        for i in a:
            bin32.append(i)
    return bin32

def R_list(num,R):
    b = xor(k[num],placement(E,R))
    B = []
    n = 0
    for i in range(0,49,6):
        if i is not 0:
            ary=b[n:i]
            n=i
            B.append(ary)
    fst_lst=[]
    middel=[]
    n=b= ""
    for i in range(0,8):
        n = str(B[i][0]) + str(B[i][5])
        b = str(B[i][1]) + str(B[i][2]) +str(B[i][3]) + str(B[i][4])
        fst_lst.append(n)
        middel.append(b)
        n=b=""
    col=[]
    row=[]
    for i in range(0,8):
        row.append(bin2dec(int(fst_lst[i])))
        col.append(bin2dec(int(middel[i])))
    s=[]
    for i in range(0,8):
        s.append(sbox[i][row[i]][col[i]])
    return xor(l,placement(per,bin32(s)))




c,d = converting(28,placement(pcindex,key))
c = shifting(c)
d = shifting(d)
for i in range(1,len(c)):
    print("C{0} = ".format(i),end="")
    printing(c[i])
    print("D{0} = ".format(i),end="")
    printing(d[i])

c_d =[]
for i in range(1,len(c)):
    c_d.append(convert28_28to56(c[i], d[i]))

for i in range(0,len(c_d)):
    print("C{0}&D{1} = ".format(i,i),end="")
    printing(c_d[i])

k=[]
for i in range(0,len(c_d)):
    k.append(placement(pc2index,c_d[i]))

for i in range(0,len(k)):
    print("K{0} = ".format(i),end="")
    printing(k[i])
print("")
l,r = converting(32,placement(ip, plain_text))
L=[l,r]
R=[r]
for i in range(1,16):
    r = R_list(1,r)
    l = L[i]
    R.append(r)
    L.append(r)
L = L[:16]

for i in range(0,16):
    print("L{0} = ".format(i),end="")
    printing(L[i])
    print("R{0} = ".format(i),end="")
    printing(R[i])

R_L = R[15]
for i in L[15]:
    R_L.append(i)
print("R15&L15 = ".format(i),end="")
printing(R_L)
print("DES = ",end="")
printing(placement(final_perm, R_L))