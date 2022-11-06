# Info template.

# Imports
from initialise import *
import constants

# CHOOSE SPECIFIC/EXTENSIVE Q and W
solveforspecific = True
# Can be True/False depending on whether mass flow rate is known.
# If mass flow rate is known, use false and manually enter, otherwise true assumes mass flow rate = 1

# CHOOSE PERFECT GAS
M, R, Cp, Cv, gamma = constants.Air()
# Enter here the type of perfect gas here to load in the constants that should be used.

# KNOWN PROPERTIES
T[0] = 15 + 273
P[0] = 10000
#Enter here any property data known about T, P, v, u, h, s. With state names in square brackets, state 1 set as X[0] etc.

# PROCESS DATA
processtype[0] = [""]
processtype[1] = ["Isobaric"]
processtype[2] = [""]
processtype[3] = ["Isobaric"]
#Enter here any data on the type of process. Options include: "Isothermal", "Isobaric", "Isochoric", "Isoenergetic", "Isenthalpic", "Isentropic"
#If the process does not fit into any of these types simply leave blank.

# COMPONENT DATA
componenttype[0] = ["Compressor"]
componenttype[1] = ["Combustor"]
componenttype[2] = ["Turbine"]
componenttype[3] = ["Cooler"]
#Enter here the component type. Options include: "Compressor", "Combustor", "Heater", "Pump", "Turbnine", "Cooler"
#If component type does not fit into one of these categories try fit to the closest acting;
#The key is to ensure that if enthalpy increasing choose: "Compressor", "Combustor" "Heater" and if enthalpy reducing choose "Pump", "Turbine", "Cooler"

#ISENTROPIC EFFICIENCY DATA
isenefficiency[0] = 0.8
isenefficiency[2] = 0.85
#Enter here known isentropic efficiency data

#RATIOS DATA
Pratio[0] = 10
Pratio[2] = 1 / 10
#Enter here data known on any property ratios, ratios are taken as forwards i.e.Xratio[SelectedComponent] = X[NextComponent]/X[SelectedComponent]

#HEAT AND WORK TRANSFER DATA
qtransfer[1] = 42 * 10 ** 6
wtransfer[1] = 0
qtransfer[2] = 0
wtransfer[3] = 0
#Enter here data known on heat and work transfers, they are taken as fowards i.e. Xtransfer[SelectedComponent] = X[NextComponent] - X[CurrentComponent]

#DATUM VALUES
datT = 273.16
datP = 1 * 10 ** 5
datv = R * datT / datP
dats = 3796
g = 9.81
#Enter here datum values to use for entropy calculations.

#MASS FLOW RATE DATA
#mflowrate[0]=
#mflowrate[1]=
#mflowrate[2]=
#mflowrate[3]=
#Remove # and use this section to enter mass flow rates when not constant throughout

#LOADING VALUES
for states in range(0, numberofstates):

#LOADING IN A CONSTANT MASS FLOW RATE
    mflowrate[states] = 50
#If mass flow rate is not constant throughout remove this line and induvidually enter mass flow rate at each state. Otherwise enter here.

#ISENTROPIC CONDITION
    if processtype[states] == ["Isentropic"]:  # passing 2d array info
        isenefficiency[states] = 1
#A condition is applied here to ensure that if isentropic then isentropic efficiency is set to 1.

#APPLYING SPECIFIC/EXTENSIVE Q and W
    if solveforspecific == True:
        mflowrate[states] = 1
#Sets all massflowrates to 1.

#LOADING INDUVIDAL PROPERTIES INTO LARGER MATRICES.
    properties[states] = [T[states], P[states], v[states], u[states], h[states], s[states]]
    processes[states] = [qtransfer[states], wtransfer[states], isenefficiency[states], mflowrate[states],processtype[states], componenttype[states], c[states], z[states]]
    ratios[states] = [Tratio[states], Pratio[states], vratio[states]]

#MAINTAIN RELATIONSHIPS
def maintainrelationships(properties, processes, ratios):

    return properties, processes, ratios
#Here we can maintain important relationships, for example if the work output of one commponent should be input into another component,
#link them as such.
#E.g. if we wanted the work of the first component to go into the third component
#If processes[0][1] !=0 and processes[2][1] == 0:
#processes[2][1] = -processes[0][1]
#If processes[0][1] ==0 and processes[2][1]!=0:
#processes[0][1] = - procceses[2][1]





