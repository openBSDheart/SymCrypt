import random
from collections import Counter

#BasicSBox
SBox = {0x0:0x6, 0x1:0x4, 0x2:0xc, 0x3:0x5, 0x4:0x0, 0x5:0x7, 0x6:0x2, 0x7:0xe, 0x8:0x1, 0x9:0xf, 0xa:0x3, 0xb:0xd, 0xc:0x8, 0xd:0xa, 0xe:0x9, 0xf:0xb}
SBoxInverted = dict([[v,k] for k,v in SBox.items()])
DistributionTable = {'u0':[],'u1':[],'v0':[],'v1':[],'diff_v':[]}

Plaintext = [0xf,0x0]
Ciphertext = [0x7,0xb]
#UNKNOWN Keys[0x0,0xb,0x1]
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
    startingdifference = getDifference(Plaintext[0],Plaintext[1])
    print "Calculate Difference: " + startingdifference




def calculateDistributionTable():
    global K1Candidates
    for u0 in range(0,16):
        u1 = u0 ^ 0xf #startingdifference does not work BUT 0xf! //WILL FIX IT LATER
        v0=getSBoxValue[u0]
        v1=getSBoxValue[u1]
        diff_v = v0 ^ v1

        #store values
        DistributionTable['u0'].append(u0)
        DistributionTable['u1'].append(u1)
        DistributionTable['v0'].append(v0)
        DistributionTable['v1'].append(v1)
        DistributionTable['diff_v'].append(diff_v)

        maxCounterofDT = Counter(DistributionTable['diff_v'])
        print  maxCounterofDT
        #v0s = guessed_k1 ^ Ciphertext[0]
        #v1s = guessed_k1 ^ Ciphertext[1]

        #u0s = SBoxInverted[v0s]
        #u1s = SBoxInverted[v1s]

        #print "v0  : "+ hex(v0s)
        #print "Inv0: "+ hex(u0s)

        #print "v1:   "+ hex(v1s)
        #print "Inv1: "+ hex(u1s)

        #diff_us = getDifference (u0s,u1s)
        #print "DIFF:" + diff_us

        #if diff_us == startingdifference:
        #    K1Candidates.append(guessed_k1)

#        print ""

#    for key in K1Candidates:
#        print "Candidate: " + hex(key)
    return
initCipher()
calculateDistributionTable()
