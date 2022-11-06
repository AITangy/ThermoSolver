import statename

from info import M,R,Cp,Cv,gamma,g

# If we have information on next h and previous h and are missing information on q or w but have one of them then we can calulate the other
# Calulcating information on Qtransfer or Wtransfer


def calcqandw(properties,processes,i):
    nextstate,prevstate = statename.adjstates(i)
    sufficientinfo = False
    if processes[i][3]!="" and processes[i][6]!="" and processes[i][7]!="" and processes[nextstate][3]!="" and processes[nextstate][6]!="" and processes[nextstate][7]!="":
        sufficientinfo = True

    if properties[i][4] !=0 and properties[nextstate][4]!=0 and (processes[i][0]!="" or processes[i][1]!="") and not (processes[i][0]!="" and  processes[i][1]!= "") and sufficientinfo==True:
        if processes[i][0] == "":
            processes[i][0] = processes[i][1] + processes[nextstate][3]*(properties[nextstate][4] + 0.5 * (processes[nextstate][6])**2 + g * processes[nextstate][6]) - processes[i][3]*(properties[i][4] + 0.5 * (processes[i][6])**2 + g*processes[i][7])

        if processes[i][1] == "":
            processes[i][1] = processes[i][0] - processes[nextstate][3]*(properties[nextstate][4] + 0.5 * (processes[nextstate][6])**2 + g * processes[nextstate][6]) + processes[i][3]*(properties[i][4] + 0.5 * (processes[i][6])**2 + g*processes[i][7])
    return properties,processes
# Here we need to account for qtransfer and wtransfer if this information has been given                                *********NEW


def useqandw(properties,processes,i):

    nextstate, prevstate = statename.adjstates(i)
    sufficientinfo = False
    if processes[i][3]!="" and processes[i][6]!="" and processes[i][7]!="" and processes[nextstate][3]!="" and processes[nextstate][6]!="" and processes[nextstate][7]!="":
        sufficientinfo = True


    if processes[i][0]!="" and processes[i][1]!="" and sufficientinfo==True:
        if properties[i][4]!=0 and properties[nextstate][4]==0:                                                 # Solving if we have knowledge on enthalpy of current state
            properties[nextstate][4] = (processes[i][0] - processes[i][1] + processes[i][3] * (properties[i][4]) + 0.5 * (processes[i][6])**2 + g * processes[i][7])/processes[nextstate][3] - 0.5 * (processes[nextstate][6])**2 - g*processes[nextstate][7]


        if properties[nextstate][4]!=0 and properties[i][4] == 0 and sufficientinfo==True:                                               # Solving if we have knowledge on enthalpy of previous state
            properties[i][4] = (processes[i][0] - processes[i][1] + processes[i][3]*(processes[i][4] + 0.5 * processes[i][6]**2 + g*processes[i][7]))/processes[nextstate][3] - 0.5*processes[nextstate][6]**2 - g*processes[nextstate][7]

    return properties,processes










