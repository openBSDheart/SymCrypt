#Project1
#Linear Attack on PRESENT

#You should understand the attack and be able to present the code in the oral
#exam.
#Exercise P1.1 Experiments with PRESENT
#This is an exercise where you need to implement some things.
#1. Compute the linear approximation table for the PRESENT S-box.
#2. Find all biased linear approximation with a one bit input and output mask.
#3. Find a linear characteristic for some rounds with only one active Sbox per round.
#4. Compute its bias.
#5. Why do all these characteristic have the same absolute bias?
#6. For any given one-bit input and output mask: Find the total number of linear charac-
#teristics in the linear hull over r rounds with only one active S-box per round.
#7. Execute some experiments to see how the bias is distributed over the keys.
#Note: This might take some time, but is very helpful for a better understanding!

# EXECUTION RESULT: SBOX approximation
# 8  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
# 0  0 -2 -2  0  0 -2  6  2  2  0  0  2  2  0  0
# 0  0 -2 -2  0  0 -2 -2  0  0  2  2  0  0 -6  2
# 0  0  0  0  0  0  0  0  2 -6 -2 -2  2  2 -2 -2
# 0  2  0 -2 -2 -4 -2  0  0 -2  0  2  2 -4  2  0
# 0 -2 -2  0 -2  0  4  2 -2  0 -4  2  0 -2 -2  0
# 0  2 -2  4  2  0  0  2  0 -2  2  4 -2  0  0 -2
 #0 -2  0  2  2 -4  2  0 -2  0  2  0  4  2  0  2
 #0  0  0  0  0  0  0  0 -2  2  2 -2  2 -2 -2 -6
 #0  0 -2 -2  0  0 -2 -2 -4  0 -2  2  0  4  2 -2
 #0  4 -2  2 -4  0  2 -2  2  2  0  0  2  2  0  0
 #0  4  0 -4  4  0  4  0  0  0  0  0  0  0  0  0
 #0 -2  4 -2 -2  0  2  0  2  0  2  4  0  2  0 -2
 #0  2  2  0 -2  4  0  2 -4 -2  2  0  2  0  0  2
 #0  2  2  0 -2 -4  0  2 -2  0  0 -2 -4  2 -2  0
 #0 -2 -4 -2 -2  0  2  0  0 -2  4 -2 -2  0  2  0
 #

import os, sys
try:
    s = sys.winver
    os.system("cls")
except:
    os.system("clear")




#        0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
SBox= [0xc,0x5,0x6,0xb,0x9,0x0,0xa,0xd,0x3,0xe,0xf,0x8,0x4,0x7,0x1,0x2]

def getCoefficient(i,j):
    a=b=c=d=e=f=g=h=0
    #CountNumbers --> dann zuerst hinten auffuellen der variablen
    i=str(bin(i))[2:] #Binaerumwandlung der Zahl 7 --> 111
    stellen=(len(str(i))) #Stellen abzaehlen -- hier war str davor --> 3


    #Korrekturvorbereitung fuer Masking 0er Stellen z.B. 4 = 11 statt notwendiger 0011
    #print "STELLEN: "+ str(stellen)
    if stellen == 1:
        a=b=c=0
        d=i[0]
    if stellen == 2:
        a=b=0
        c=i[0]
        d=i[1]
    if stellen == 3:
        a=0
        b=i[0]
        c=i[1]
        d=i[2]
    if stellen == 4:
        a=i[0]
        b=i[1]
        c=i[2]
        d=i[3]




    j=str(bin(j))[2:] #Binaerumwandlung der Zahl 7 --> 111
    stellen=(len(str(j))) #Stellen abzaehlen -- hier war str davor --> 3


    #Korrekturvorbereitung fuer Masking 0er Stellen z.B. 4 = 11 statt notwendiger 0011
    #print "STELLEN: "+ str(stellen)
    if stellen == 1:
        e=f=g=0
        h=j[0]
    if stellen == 2:
        e=f=0
        g=j[0]
        h=j[1]
    if stellen == 3:
        e=0
        f=j[0]
        g=j[1]
        h=j[2]
    if stellen == 4:
        e=j[0]
        f=j[1]
        g=j[2]
        h=j[3]


    #CountDigits:
    a = int (a)
    b = int (b)
    c = int (c)
    d = int (d)
    e = int (e)
    f = int (f)
    g = int (g)
    h = int (h)
    return a,b,c,d,e,f,g,h

#############################################################
# LOOP:
#RetCPos = getCoefficient (15,14) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7

#if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
#    print "+++++++++++++++++ +++++++ WOR KI NG !!!! YEAH  U ARE GREAT ++++++++++++++++"



CTR=0 # init loop

# MASKing --> Selektoren fuer Angriff

#TESTVECTOR
#x = [1,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE 1000
#y = [1,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE 1000 = FEHLER
#if (a*x[0] ^ b*x[1] ^ c*x[2] ^ d*x[3] == e*y[0] ^ f*y[1] ^ g*y[2] ^ h*y[3]):#
#if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
#    print "+++++++++++++++++ +++++++ WOR KI NG !!!! YEAH  U ARE GREAT ++++++++++++++++"

## TODO:
# Selektoren a-h muessen aus Funktion dynamisch geliefert werden von 0000 - 1111 als Rueckgabewert
# e-h bestimmt die Ausgabespalte X (oben), danach wird ueber die Ausgabespalte e-h in einer Loop gelaufen.
# Zuerst 0,1,2,3,4,5,6, ... in X Achse, dann einen runter, wieder 0,1,2,3,4,5,6,7, auf X, einen runter ...
# nach je 16 Zeilendurchlaufen bis ganz nach unten inkrementieren wir zuerst die Eingabewerte, danach die Ausgabewerte

inp = 0
outp = 0

y=0

for inp in range(0,16):
    sys.stdout.write("\n")
    for outp in range(0,16):
        CTR=0 # init or reset call







        #ZEILE 1
        x = [0,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1


        x = [0,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [0,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1


        x = [1,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1


        x = [1,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [1,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1

        x = [1,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        y = [0,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
        RetCPos = getCoefficient (inp,outp) #RetCoefficientPosition 0 1 2 3 - 4 5 6 7
        if (RetCPos[0]*x[0] ^ RetCPos[1]*x[1] ^ RetCPos[2]*x[2] ^ RetCPos[3]*x[3] == RetCPos[4]*y[0] ^ RetCPos[5]*y[1] ^ RetCPos[6]*y[2] ^ RetCPos[7]*y[3]):
            CTR+=1


        COUNT= float((float(CTR)/16)-0.5)*16 #floatCASTING = - 0.125*16 = -2.0 (STIMMT)
        sys.stdout.write ("%2d " % (COUNT))


# LOOP ENDE
#############################################################

# PRUEFE AUTOMATISIERT ALLE LINEAR EQUATION INPUTS & OUTPUTS
# IN=OUT
# 0 auf 0
#for i in range(0,16):
#if (x[0]==y[0]):
#    ctr+=1


#if (x[0] ^ x[2]==y[0] ^ y[2] ^ y[3])


# 0 auf 0

#if  (x[0] ^ x[1] ^ x[2] ^ x[3] == y[0] ^ y[1] ^ y[2] ^ y[3]): # IDEE XOR mit 0 zum auslassen von Variablen
#    print ""
#    print ">>>> INC_CTR++ "



#print "Success of the attack BIAS = (SUMME_CTR/16)-1/2"



# Finde Maximum
# delta y, delta x, number of times
#maximum = [0,0,0]
#for i in range(0,16):
#    for j in range(0,16):
#        if DifferenceDistTable[j][i] >= maximum[2] and i != 0 and j !=0:
#            maximum[0] = i
#            maximum[1] = j
#            maximum[2] = DifferenceDistTable[j][i]

# Gebe Maximum aus
#print ""
#print "Maximum"
#print "Delta X: " + str(hex(maximum[0]))
#print "Delta Y: " + str(hex(maximum[1]))
#print "Auftreten: " + str(maximum[2])
#print "Warscheinlichkeit: " + str(maximum[2]) +"/16"
