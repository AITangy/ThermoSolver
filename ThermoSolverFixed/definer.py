
import math
from info import definedstates, numberofstates,accuracy,datT,datP,datv,dats,M,R,Cp,Cv,gamma
import numpy as np
from statename import adjstates
from plotter import plotaround, plotaroundundefined


def CheckDefine(i,properties,plotinfo,definedstates,newinfo):
    sum = 0

    nextstate,prevstate = adjstates(i)
    for j in range(0,6):

        if properties[i][j] != 0:
            sum = sum + 1

        if sum == 4:  # Fully defining the state in each case where we have enough information
            newinfo = True
            definedstates[i] = True
            properties[i] = FullyDefinernew(properties[i])
            plotinfo[i][0] = properties[i]
            plotinfo[prevstate][accuracy-1] = properties[i]
        elif sum == 3 and (properties[i][1] + properties[i][2] + properties[i][5]) != 0:
            newinfo = True
            definedstates[i] = True
            properties[i] = FullyDefinernew(properties[i])
            plotinfo[i][0] = properties[i]
            plotinfo[prevstate][accuracy - 1] = properties[i]

        elif sum == 2 and (properties[i][1] + properties[i][2]  +properties[i][4] + properties[i][5]) != 0 and (properties[i][1] + properties[i][2] + properties[i][3] + properties[i][5]) != 0 and ( properties[i][1] + properties[i][2] + properties[i][5]) != 0:
            newinfo = True
            definedstates[i] = True
            properties[i] = FullyDefinernew(properties[i])
            plotinfo[i][0] = properties[i]
            plotinfo[prevstate][accuracy - 1] = properties[i]

    if properties[i][4]!=0 and properties[i][3]==0 and properties[i][0]==0:
        newinfo = True
        properties[i] = Tstuff(properties[i])
    if properties[i][3]!=0 and properties[i][4]==0 and properties[i][0]==0:
        newinfo = True
        properties[i] = Tstuff(properties[i])
    if properties[i][4]!=0 and properties[i][3]!=0 and properties[i][0]==0:
        newinfo = True
        properties[i] = Tstuff(properties[i])
    if properties[i][0]!=0 and properties[i][3]==0 and properties[i][4]==0:
        newinfo = True
        properties[i] = Tstuff(properties[i])
    if properties[i][0]!=0 and properties[i][4]!=0 and properties[i][0]==0:
        newinfo = True
        properties[i] = Tstuff(properties[i])
    if properties[i][0]!=0 and properties[i][3]!=0 and properties[i][4]==0:
        newinfo= True
        properties[i] = Tstuff(properties[i])



    return properties,plotinfo,definedstates,newinfo







def FullyDefinernew(modifproperties):   # We now need to tweak every instance of using the fully definer alogrythm to include the fact that we have the counter built in...                                                                                                                  # for entropy we will use datum values at the triple point of water and 1 bar

    if modifproperties[0] != 0 and modifproperties[1]!= 0:                                            # Solving given T and P
        modifproperties[2] = (R * modifproperties[0] )/ modifproperties[1]
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[0] != 0 and modifproperties[2] != 0:                                         # Solving given T and v
        modifproperties[1] = (R * modifproperties[0]) / modifproperties[2]  # P = RT/v
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[0] != 0 and modifproperties[5] != 0:                                         # Solving given T and s
        modifproperties[1] = math.exp((Cp*math.log(modifproperties[0]/datT)+dats-modifproperties[5])/R)*datP
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]


    elif modifproperties[1] != 0 and modifproperties[2] != 0:                                         # Solving given P and T
        modifproperties[0] = modifproperties[1] * modifproperties[2] / R
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[1] != 0 and modifproperties[3] != 0:                                         # Solving given P and u
        modifproperties[0] = modifproperties[3] / Cv
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[4] = Cp * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[1] != 0 and modifproperties[4] != 0:                                         # Solving given P and h
        modifproperties[0] = modifproperties[4] / Cp
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[1] != 0 and modifproperties[5] != 0:                                         # Solving given P and s
        modifproperties[0] = math.exp((modifproperties[5]-dats + R*math.log(modifproperties[1]/datP))/Cp)*datT
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]

    elif modifproperties[2] != 0 and modifproperties[3] != 0:                                         # Solving given v and u
        modifproperties[0] = modifproperties[3] / Cv
        modifproperties[1] = (R * modifproperties[0]) / modifproperties[2]
        modifproperties[4] = Cp * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[2] != 0 and modifproperties[4] != 0:                                         # Solving if given v and h
        modifproperties[0] = modifproperties[4] / Cp
        modifproperties[1] = (R * modifproperties[0]) / modifproperties[2]  # P = RT/v
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[5] = Cp * math.log(modifproperties[0] / datT) - R * math.log(modifproperties[1] / datP) + dats

    elif modifproperties[2] != 0 and modifproperties[5] != 0:                                         # Solving if given v and s
        modifproperties[1] = math.exp((modifproperties[5]-dats - Cp*math.log(modifproperties[2]/datv))/Cv)*datP
        modifproperties[0] = modifproperties[1] * modifproperties[2] / R
        modifproperties[3] = Cv * modifproperties[0]
        modifproperties[4] = Cp * modifproperties[0]


    elif modifproperties[3] != 0 and modifproperties[5] != 0:                                         # Solving if given u and s
        modifproperties[0] = modifproperties[3] / Cv
        modifproperties[1] = math.exp((Cp*math.log(modifproperties[0]/datT)+dats-modifproperties[5])/R)*datP
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[4] = Cp * modifproperties[0]

    elif modifproperties[4] != 0 and modifproperties[5] != 0:                                         # Solving if given h and s
        modifproperties[0] = modifproperties[4] / Cp
        modifproperties[1] = math.exp((Cp*math.log(modifproperties[0]/datT)+dats-modifproperties[5])/R)*datP
        modifproperties[2] = R * modifproperties[0] / modifproperties[1]
        modifproperties[3] = Cv * modifproperties[0]

    return modifproperties



def mgetH(modifproperties):

    dummyproperties = np.copy(modifproperties)
    dummyproperties = FullyDefinernew(dummyproperties)
    modifproperties[4] = dummyproperties[4]
    modifproperties[0] = 0
    return modifproperties




def Tstuff(modifproperties):

    if modifproperties[0]!=0:
        modifproperties[3] = Cv*modifproperties[0]
        modifproperties[4] = Cp*modifproperties[0]

    elif modifproperties[3]!=0:
        modifproperties[0] = modifproperties[3]/Cv
        modifproperties[4] = Cp*modifproperties[0]

    elif modifproperties[4]!=0:
        modifproperties[0] = modifproperties[4]/Cp
        modifproperties[3] = Cv*modifproperties[0]

    return modifproperties

# def hGet(dummyproperties, counter):
#     datT = 273.16
#     datP = 10000
#     datv = 1 / 1.276
#     dats = 3796
#     modifproperties = np.copy(dummyproperties)
#
#
#     if dummyproperties[counter][0] != 0 and dummyproperties[counter][1]!= 0:                                            # Solving given T and P
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][0] != 0 and dummyproperties[counter][2] != 0:                                         # Solving given T and v
#         dummyproperties[counter][1] = (R * dummyproperties[counter][0]) / dummyproperties[counter][2]  # P = RT/v
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][0] != 0 and dummyproperties[counter][5] != 0:                                         # Solving given T and s
#         dummyproperties[counter][1] = math.exp((1 / R * (Cp * math.log(dummyproperties[counter][0] / datT) + dummyproperties[counter][5] - dats))) * datP
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#
#
#     elif dummyproperties[counter][1] != 0 and dummyproperties[counter][2] != 0:                                         # Solving given P and T
#         dummyproperties[counter][0] = dummyproperties[counter][1] * dummyproperties[counter][2] / R
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][1] != 0 and dummyproperties[counter][3] != 0:                                         # Solving given P and u
#         dummyproperties[counter][0] = dummyproperties[counter][3] / Cv
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][1] != 0 and dummyproperties[counter][4] != 0:                                         # Solving given P and h
#         dummyproperties[counter][0] = dummyproperties[counter][4] / Cp
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][1] != 0 and dummyproperties[counter][5] != 0:                                         # Solving given P and s
#         dummyproperties[counter][0] = math.exp((dummyproperties[counter][5] - dats + R * math.log(dummyproperties[counter][1] / datP)) * 1 / Cp) * dummyproperties[counter][0]
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#
#     elif dummyproperties[counter][2] != 0 and dummyproperties[counter][3] != 0:                                         # Solving given v and u
#         dummyproperties[counter][0] = dummyproperties[counter][3] / Cv
#         dummyproperties[counter][1] = (R * dummyproperties[counter][0]) / dummyproperties[counter][2]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][2] != 0 and dummyproperties[counter][4] != 0:                                         # Solving if given v and h
#         dummyproperties[counter][0] = dummyproperties[counter][4] / Cp
#         dummyproperties[counter][1] = (R * dummyproperties[counter][0]) / dummyproperties[counter][2]  # P = RT/v
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][5] = Cp * math.log(dummyproperties[counter][0] / datT) - R * math.log(dummyproperties[counter][1] / datP)
#
#     elif dummyproperties[counter][2] != 0 and dummyproperties[counter][5] != 0:                                         # Solving if given v and s
#         dummyproperties[counter][0] = math.exp((dummyproperties[counter][5] - dats - R * math.log(dummyproperties[counter][2] / datv)) / Cv) * datT
#         dummyproperties[counter][1] = (R * dummyproperties[counter][0]) / dummyproperties[counter][2]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#
#     elif dummyproperties[counter][3] != 0 and dummyproperties[counter][5] != 0:                                         # Solving if given u and s
#         dummyproperties[counter][0] = dummyproperties[counter][3] / Cv
#         dummyproperties[counter][1] = math.exp((1 / R * (Cp * math.log(dummyproperties[counter][0] / datT) + dummyproperties[counter][5] - dats))) * datP
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][4] = Cp * dummyproperties[counter][0]
#
#     elif dummyproperties[counter][4] != 0 and dummyproperties[counter][5] != 0:                                         # Solving if given h and s
#         dummyproperties[counter][0] = dummyproperties[counter][4] / Cp
#         dummyproperties[counter][1] = math.exp((1 / R * (Cp * math.log(dummyproperties[counter][0] / datT) + dummyproperties[counter][5] - dats))) * datP
#         dummyproperties[counter][2] = R * dummyproperties[counter][0] / dummyproperties[counter][1]
#         dummyproperties[counter][3] = Cv * dummyproperties[counter][0]
#
#
#     modifproperties[counter][4] = dummyproperties[counter][4]
#     return modifproperties
#
#
# def FullyDefiner(modifproperties, counter):                                                                                                                     # for entropy we will use datum values at the triple point of water and 1 bar
#     datT = 273.16
#     datP = 10000
#     datv = 1 / 1.276
#     dats = 3796
#
#     if modifproperties[counter][0] != 0 and modifproperties[counter][1]!= 0:                                            # Solving given T and P
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][0] != 0 and modifproperties[counter][2] != 0:                                         # Solving given T and v
#         modifproperties[counter][1] = (R * modifproperties[counter][0]) / modifproperties[counter][2]  # P = RT/v
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][0] != 0 and modifproperties[counter][5] != 0:                                         # Solving given T and s
#         modifproperties[counter][1] = math.exp((1 / R * (Cp * math.log(modifproperties[counter][0] / datT) + modifproperties[counter][5] - dats))) * datP
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#
#
#     elif modifproperties[counter][1] != 0 and modifproperties[counter][2] != 0:                                         # Solving given P and T
#         modifproperties[counter][0] = modifproperties[counter][1] * modifproperties[counter][2] / R
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][1] != 0 and modifproperties[counter][3] != 0:                                         # Solving given P and u
#         modifproperties[counter][0] = modifproperties[counter][3] / Cv
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][1] != 0 and modifproperties[counter][4] != 0:                                         # Solving given P and h
#         modifproperties[counter][0] = modifproperties[counter][4] / Cp
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][1] != 0 and modifproperties[counter][5] != 0:                                         # Solving given P and s
#         modifproperties[counter][0] = math.exp((modifproperties[counter][5] - dats + R * math.log(modifproperties[counter][1] / datP)) * 1 / Cp) * modifproperties[counter][0]
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#
#     elif modifproperties[counter][2] != 0 and modifproperties[counter][3] != 0:                                         # Solving given v and u
#         modifproperties[counter][0] = modifproperties[counter][3] / Cv
#         modifproperties[counter][1] = (R * modifproperties[counter][0]) / modifproperties[counter][2]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][2] != 0 and modifproperties[counter][4] != 0:                                         # Solving if given v and h
#         modifproperties[counter][0] = modifproperties[counter][4] / Cp
#         modifproperties[counter][1] = (R * modifproperties[counter][0]) / modifproperties[counter][2]  # P = RT/v
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][5] = Cp * math.log(modifproperties[counter][0] / datT) - R * math.log(modifproperties[counter][1] / datP)
#
#     elif modifproperties[counter][2] != 0 and modifproperties[counter][5] != 0:                                         # Solving if given v and s
#         modifproperties[counter][0] = math.exp((modifproperties[counter][5] - dats - R * math.log(modifproperties[counter][2] / datv)) / Cv) * datT
#         modifproperties[counter][1] = (R * modifproperties[counter][0]) / modifproperties[counter][2]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#
#     elif modifproperties[counter][3] != 0 and modifproperties[counter][5] != 0:                                         # Solving if given u and s
#         modifproperties[counter][0] = modifproperties[counter][3] / Cv
#         modifproperties[counter][1] = math.exp((1 / R * (Cp * math.log(modifproperties[counter][0] / datT) + modifproperties[counter][5] - dats))) * datP
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][4] = Cp * modifproperties[counter][0]
#
#     elif modifproperties[counter][4] != 0 and modifproperties[counter][5] != 0:                                         # Solving if given h and s
#         modifproperties[counter][0] = modifproperties[counter][4] / Cp
#         modifproperties[counter][1] = math.exp((1 / R * (Cp * math.log(modifproperties[counter][0] / datT) + modifproperties[counter][5] - dats))) * datP
#         modifproperties[counter][2] = R * modifproperties[counter][0] / modifproperties[counter][1]
#         modifproperties[counter][3] = Cv * modifproperties[counter][0]
#
#     return modifproperties












