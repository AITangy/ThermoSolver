import statename

from constants import *

# If we have information on next h and previous h and are missing information on q or w but have one of them then we can calulate the other
# Calulcating information on Qtransfer or Wtransfer


def calcqandw(properties,processes,i):
    nextstate,prevstate = statename.adjstates(i)

    if properties[i][4] !=0 and properties[nextstate][4]!=0 and (processes[i][0]!="" or processes[i][1]!="") and not (processes[i][0]!="" and  processes[i][1]!= ""):
        if processes[i][0] == 0:
            processes[i][0] = processes[i][1] + processes[nextstate][3]*(properties[nextstate][4] + 0.5 * (processes[nextstate][6])**2 + g * processes[nextstate][6]) - processes[i][3]*(properties[i][4] + 0.5 * (processes[i][6])**2 + g*processes[i][7])

        if processes[i][1] == 0:
            processes[i][1] = processes[i][0] -  (processes[nextstate][3]*(properties[nextstate][4] + 0.5 * (processes[nextstate][6])**2 + g * processes[nextstate][6]) - processes[i][3]*(properties[i][4] + 0.5 * (processes[i][6])**2 + g*processes[i][7]))
    return properties,processes
# Here we need to account for qtransfer and wtransfer if this information has been given                                *********NEW


def useqandw(properties,processes,i):
    nextstate, prevstate = statename.adjstates(i)
    if processes[i][0]!="" and processes[i][1]!="":
        if properties[i][4]!=0 and properties[nextstate][4]==0:                                                 # Solving if we have knowledge on enthalpy of current state
            properties[nextstate][4] = (processes[i][0] - processes[i][1] - processes[i][3] * (properties[i][4]) + 0.5 * (processes[i][6])**2 + g * processes[i][7])/processes[nextstate][3] - 0.5 * (processes[nextstate][6])**2 - g*processes[nextstate][7]


        if properties[nextstate][4]!=0 and properties[i][4] == 0:                                               # Solving if we have knowledge on enthalpy of previous state
            properties[i][4] = (processes[i][0] - processes[i][1] - processes[nextstate][3] * (properties[nextstate][4] + 0.5 * (processes[nextstate][6])**2 + g*processes[nextstate][7]))/processes[i][3] - 0.5 * (processes[i][6])**2 - g*processes[i][7]

    return properties,processes










