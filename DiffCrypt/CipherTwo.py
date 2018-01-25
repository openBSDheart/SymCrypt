import random
from collections import Counter

import os, sys
try:
    s = sys.winver
    os.system("cls")
except:
    os.system("clear")

#BasicSBox
SBox = {0x0:0x6, 0x1:0x4, 0x2:0xc, 0x3:0x5, 0x4:0x0, 0x5:0x7, 0x6:0x2, 0x7:0xe, 0x8:0x1, 0x9:0xf, 0xa:0x3, 0xb:0xd, 0xc:0x8, 0xd:0xa, 0xe:0x9, 0xf:0xb}
SBoxInverted = dict([[v,k] for k,v in SBox.items()])
DistributionTable = {'u0':[],'u1':[],'v0':[],'v1':[],'diff_v':[]}

Plaintext = [0xf,0x0]
Ciphertext = [0x7,0xb]
#hidden Keys[0x0,0xb,0x1] we want to bring up
K1Candidates = []

def getSBoxValue(input):
    return SBox[input]

def getRandomValue():
    return random.randint(0,15)

def getDifference(a,b):
    difference = a ^ b
    return hex(difference)

def initCipher():
    global startingdifference
    print "Init Cipher"
    #inactive due to problems with XOR CALCULATIONS
    startingdifference = getDifference(Plaintext[0],Plaintext[1])
    print "Calculate Difference: " + startingdifference[2:4]

def calculateDistributionTable():
    global DistributionTable
    for u0 in range(0,16):
        u1 = u0 ^ 0xf #startingdifference does not work BUT 0xf! //WILL FIX IT LATER
        v0=getSBoxValue(u0)
        v1=getSBoxValue(u1)
        diff_v = v0 ^ v1

        #store values
        DistributionTable['u0'].append(u0)
        DistributionTable['u1'].append(u1)
        DistributionTable['v0'].append(v0)
        DistributionTable['v1'].append(v1)
        DistributionTable['diff_v'].append(diff_v)

def attack():
    global DistributionTable
    #Sortieralgo
    highestDifferenzofV = Counter(DistributionTable['diff_v'])
    #print highestDifferenzofV

    diff_v=0
    occurence_V=0
    for item in (DistributionTable['diff_v']):
        print hex(item)[2:]
        if highestDifferenzofV[item] > occurence_V:
            diff_v = item
            occurence_V=highestDifferenzofV[item]
    print "Assumption for difference of "+ hex(diff_v) +" is " + str(highestDifferenzofV[diff_v])+"/16"
    return


initCipher()
calculateDistributionTable()
attack()
