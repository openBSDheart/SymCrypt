#recovers the key k0||k1
#
#given textvectors a->9,5->6 should ends up in k1=7,8
#and   testvectors 9->7,8->0 should ends up in k1=0,7
#result: deduct that k1=7 is the right key.
#a-->9 gives k0=a^InvertSbox[9^k1] with k1=7 and ends up in k0=d
#So we recover with this attack k1=7 and k0=7.

import random
#BasicSBox
SBox = {0x0:0x6, 0x1:0x4, 0x2:0xc, 0x3:0x5, 0x4:0x0, 0x5:0x7, 0x6:0x2, 0x7:0xe, 0x8:0x1, 0x9:0xf, 0xa:0x3, 0xb:0xd, 0xc:0x8, 0xd:0xa, 0xe:0x9, 0xf:0xb}
SBoxInverted = dict([[v,k] for k,v in SBox.items()])

Plaintext = [0x9,0x8]
Ciphertext = [0x7,0x0]
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
    startingdifference=getDifference(Plaintext[0],Plaintext[1])
    print "Calculate Difference: " + startingdifference

def findCandidates():
    global K1Candidates
    for guessed_k1 in range(0,16):
        v0s = guessed_k1 ^ Ciphertext[0]
        v1s = guessed_k1 ^ Ciphertext[1]

        u0s = SBoxInverted[v0s]
        u1s = SBoxInverted[v1s]

        #print "v0  : "+ hex(v0s)
        #print "Inv0: "+ hex(u0s)

        #print "v1:   "+ hex(v1s)
        #print "Inv1: "+ hex(u1s)

        diff_us = getDifference (u0s,u1s)
        print "DIFF:" + diff_us

        if diff_us == startingdifference:
            K1Candidates.append(guessed_k1)

        print ""

    for key in K1Candidates:
        print "Candidate: " + hex(key)

initCipher()
findCandidates()
