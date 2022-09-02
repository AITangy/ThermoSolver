from initialise import *
import constants

solveforspecific = True
M,R,Cp,Cv,gamma = constants.Air()
processtype[0] = ["Isentropic"]
processtype[1] = ["Isochoric"]
processtype[2] = ["Isentropic"]
processtype[3] = ["Isochoric"]


componenttype[0] = ["Compressor"]
componenttype[1] = ["Heater"]
componenttype[2] = ["Turbine"]
componenttype[3] = ["Cooler"]

T[2]=3273
T[0]=288
P[0] = 1*10**5

vratio[0] = 9













datT = 273.16
datP = 1*10**5
datv = R*datT/datP
dats = 3796
g = 9.81

for states in range(0, numberofstates):
    if processtype[states] == ["Isentropic"]:  # passing 2d array info
        isenefficiency[states] = 1
    if solveforspecific == True:
        mflowrate[states] = 1

    properties[states] = [T[states], P[states], v[states], u[states], h[states], s[states]]
    processes[states] = [qtransfer[states], wtransfer[states], isenefficiency[states], mflowrate[states],processtype[states], componenttype[states], c[states], z[states]]
    ratios[states] = [Tratio[states], Pratio[states], vratio[states]]

def maintainrelationships(properties,processes,ratios):



    return properties,processes,ratios