from initialise import *
import constants

M,R,Cp,Cv,gamma = constants.Air()

for i in range(0,numberofstates):
    mflowrate[i] = 1

P[0] = 1*10**5
T[0] = 20 + 273
P[1] = 10*10**5
T[1] = 344+273
P[4] = 1*10**5
T[2] = 1100


processtype[0] = [""]
processtype[1] = ["Isobaric"]
processtype[2] = [""]
processtype[3] = ["Isentropic"]
processtype[4]= ["Isobaric"]


componenttype[0] = ["Compressor"]
componenttype[1] = ["Combustor"]
componenttype[2] = ["Turbine"]
componenttype[3] = ["Compressor"]
componenttype[4] = ["Cooler"]




isenefficiency[2] =0.9
# isenefficiency[2] =
#
#
Pratio[0] =10
# Pratio[2] =


qtransfer[0]=0
wtransfer[1]=0
qtransfer[2]=0
wtransfer[3]=0
qtransfer[3]=0
wtransfer[4]=0



c[4]=""




datT = 273.16
datP = 1*10**5
datv = R*datT/datP
dats = 3796
g = 9.81

for states in range(0, numberofstates):
    if processtype[states] == ["Isentropic"]:  # passing 2d array info
        isenefficiency[states] = 1

    properties[states] = [T[states], P[states], v[states], u[states], h[states], s[states]]
    processes[states] = [qtransfer[states], wtransfer[states], isenefficiency[states], mflowrate[states],processtype[states], componenttype[states], c[states], z[states]]
    ratios[states] = [Tratio[states], Pratio[states], vratio[states]]

def maintainrelationships(properties,processes,ratios):
    if processes[0][1]!="":
        processes[2][1] = -1*processes[0][1]


    return properties,processes,ratios
