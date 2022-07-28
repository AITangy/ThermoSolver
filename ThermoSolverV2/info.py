from initialise import *
import constants

M,R,Cp,Cv,gamma = constants.Air()

for i in range(0,numberofstates):
    mflowrate[i] = 50



T[0] = 15+273



processtype[0] = [""]
processtype[1] = ["Isobaric"]
processtype[2] = [""]
processtype[3] = ["Isobaric"]



componenttype[0] = ["Compressor"]
componenttype[1] = ["Combustor"]
componenttype[2] = ["Turbine"]
componenttype[3] = ["Cooler"]




isenefficiency[0] = 0.8
isenefficiency[2] = 0.85

Pratio[0] = 10
Pratio[2] = 1/10


qtransfer[1]=42*10**6
wtransfer[1]=0
qtransfer[2]=0
wtransfer[3]=0





qtransfer[0] = 0










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

