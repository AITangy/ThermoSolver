from initialise import *
from constants import *

#info.py passes known data into data structures

T[1] = 300
P[0] = 1000000
P[1] = 10000000

processtype[0] = ["Isothermal"]
processtype[1] = ["Isobaric"]
processtype[2] = ["Isentropic"]

componenttype[0] = ["Compressor"]
componenttype[1] = ["Heater"]
componenttype[2] = ["Turbine"]



# defining known (state/property/ratio) information

wtransfer[0] = 3000000
# qtransfer[0] = 0
isenefficiency[2] = 1


datT = 273.16
datP = 1*10**5
datv = R*datT/datP
dats = 3796

for states in range(0, numberofstates):
    if processtype[states] == ["Isentropic"]:  # passing 2d array info
        isenefficiency[states] = 1

    properties[states] = [T[states], P[states], v[states], u[states], h[states], s[states]]
    processes[states] = [qtransfer[states], wtransfer[states], isenefficiency[states], mflowrate[states],processtype[states], componenttype[states], c[states], z[states]]
    ratios[states] = [Tratio[states], Pratio[states], vratio[states]]

