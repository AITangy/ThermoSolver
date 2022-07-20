from info import processes,ratios
import statename
from info import accuracy
import numpy as np

def CheckRelation(i, newinfo, properties,plotinfo):
    # Here we go through and try to find new information by accounting for the process type of each of the components

    nextstate,prevstate = statename.adjstates(i)

    if processes[i][4] == ["Isobaric"]:  # For strings the values stores inside must be refered to in square brackets for conditional statements however this is not true for integers.
        if properties[nextstate][1] != 0 and properties[i][1] == 0:
            newinfo = True
            properties[i][1] = properties[nextstate][1]

            for j in range(0,accuracy):
                plotinfo[i][j][1] = properties[nextstate][1]







        elif properties[i][1] != 0 and properties[nextstate][1] == 0:
            newinfo = True
            properties[nextstate][1] = properties[i][1]

            for j in range(0,accuracy):
                plotinfo[i][j][1] = properties[nextstate][1]

            #   maybe the intermediate relationship function can wait until the end? But no that would be completly inneficient, we should have it throughout!








    if processes[i][4] == ["Isochoric"]:

        if properties[nextstate][2] != 0 and properties[i][2] == 0:
            newinfo = True
            properties[i][2] = properties[nextstate][2]

            for j in range(0,accuracy):
                plotinfo[i][j][2] = properties[nextstate][2]

        elif properties[i][2] != 0 and properties[nextstate][2] == 0:
            newinfo = True
            properties[nextstate][2] = properties[i][2]

            for j in range(0,accuracy):
                plotinfo[i][j][2] = properties[nextstate][2]







    if processes[i][4] == ["Isoenergetic"]:

        if properties[nextstate][3] != 0 and properties[i][3] == 0:
            newinfo = True
            properties[i][3] = properties[nextstate][3]

            for j in range(0,accuracy):
                plotinfo[i][j][3] = properties[nextstate][3]

        elif properties[i][3] != 0 and properties[nextstate][3] == 0:
            newinfo = True
            properties[nextstate][3] = properties[i][3]

            for j in range(0,accuracy):
                plotinfo[i][j][3] = properties[nextstate][3]











    if processes[i][4] == ["Isenthalpic"]:

        if properties[nextstate][4] != 0 and properties[i][4] == 0:
            newinfo = True
            properties[i][4] = properties[nextstate][4]

            for j in range(0,accuracy):
                plotinfo[i][j][4] = properties[nextstate][4]

        elif properties[i][4] != 0 and properties[nextstate][4] == 0:
            newinfo = True
            properties[nextstate][4] = properties[i][4]

            for j in range(0,accuracy):
                plotinfo[i][j][4] = properties[nextstate][4]











    if processes[i][4] == ["Isothermal"]:

        if properties[nextstate][0] != 0 and properties[i][0] == 0:
            newinfo = True
            properties[i][0] = properties[nextstate][0]

            for j in range(0,accuracy):
                plotinfo[i][j][0] = properties[nextstate][0]

        elif properties[i][0] != 0 and properties[nextstate][0] == 0:
            newinfo = True
            properties[nextstate][0] = properties[i][0]

            for j in range(0,accuracy):
                plotinfo[i][j][0] = properties[nextstate][0]

    # Here we can account for ratio relationships in the processes if they happen to exist!

    if ratios[i][0] != 0:
        if properties[nextstate][4] != 0 and properties[i][4] == 0:
            newinfo = True
            properties[i][4] = properties[nextstate][4] / ratios[i][0]

        elif properties[i][4] != 0 and properties[nextstate][4] == 0:
            newinfo = True
            properties[nextstate][4] = properties[i][4] * ratios[i][0]

    if ratios[i][1] != 0:
        if properties[nextstate][1] != 0 and properties[i][1] == 0:
            newinfo = True
            properties[i][1] = properties[nextstate][1] / ratios[i][1]

        elif properties[i][1] != 0 and properties[nextstate][1] == 0:
            newinfo = True
            properties[i][nextstate] = properties[i][1] * ratios[i][1]

    if ratios[i][2] != 0:
        if properties[nextstate][2] != 0 and properties[i][2] == 0:
            newinfo = True
            properties[i][2] = properties[nextstate][2] / ratios[i][2]

        elif properties[i][2] != 0 and properties[nextstate][2] == 0:
            newinfo = True
            properties[nextstate][2] = properties[i][2] * ratios[i][2]

    return newinfo, properties,plotinfo