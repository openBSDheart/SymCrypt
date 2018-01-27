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

import os, sys
try:
    s = sys.winver
    os.system("cls")
except:
    os.system("clear")




# S-Box of Cipher (- DEMO - NON PRESENT --> CHANGE LATER )
SBox = [0xF,0xE,0xB,0xC,0x6,0xD,0x7,0x8,0x0,0x3,0x9,0xA,0x4,0x2,0x1,0x5]
DifferenceDistTable = [[0 for x in range(16)] for y in range(16)]


# Berechne Difference Distribution Table
for x0 in range(0,16):
    for x1 in range(0,16):
        inputDiff = x0 ^ x1

        outputDiff = SBox[x0] ^ SBox[x1]
        DifferenceDistTable[outputDiff][inputDiff] += 1


# Gebe Difference Distribution Table aus
sys.stdout.write("   ")
for z in range(0,16):
    sys.stdout.write(str(z)+" ")
sys.stdout.write("\n")

for i in range(0,16):
    sys.stdout.write(str(i)+": ")
    for j in range(0,16):
        sys.stdout.write(str(DifferenceDistTable[j][i])+" ")
    sys.stdout.write("\n")

# Werte kommen von oben und werden aus HEX umgewandelt in binaer und dann zugeteilt in Array
#    0 1 2 3
# ay = [0,0,0,1] #    Ausgabe-SBox PRESENT CHIFFRE
# by = [0,1,0,0] #    Ausgabe-SBox PRESENT CHIFFRE


#############################################################
# LOOP:
CTR=0 # init loop

#ZEILE 1
x = [0,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1

x = [0,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [0,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1

x = [1,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,0,1,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,0,1,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1

x = [1,1,0,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,1,0,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [1,0,0,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,1,1,0] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,0,0,0] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1
x = [1,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
y = [0,1,1,1] #    Eingabe-SBox PRESENT CHIFFRE
if (x[0]==y[0]):
    CTR+=1

COUNT= float((float(CTR)/16)-0.5)*16 #floatCASTING = - 0.125*16 = -2.0 (STIMMT)
print "SUMME:" + str(COUNT)

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
