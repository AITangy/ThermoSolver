
import statename
from info import accuracy,M,R,Cp,Cv,gamma
import numpy as np
from definer import FullyDefinernew,mgetH
from isenaccounters import accountT



def CheckRelation(i, newinfo, properties,processes,ratios,plotinfo):
    # Here we go through and try to find new information by accounting for the process type of each of the components

    nextstate,prevstate = statename.adjstates(i)
    plotinfo = relationshipintermediate(plotinfo, i)
    if processes[i][4] == ["Isobaric"]:  # For strings the values stores inside must be refered to in square brackets for conditional statements however this is not true for integers.
        plotinfo = relationshipintermediate(plotinfo, i)
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
        plotinfo = relationshipintermediate(plotinfo, i)
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
        plotinfo = relationshipintermediate(plotinfo, i)
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

        plotinfo = relationshipintermediate(plotinfo, i)
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

        plotinfo = relationshipintermediate(plotinfo,i)
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

    newinfo,properties = ratiochecker(properties,processes,ratios,i,newinfo)



    # Here we can account for ratio relationships in the processes if they happen to exist!





    return newinfo, properties,plotinfo


def relationshipintermediate(plotinfo,i):

    if plotinfo[i][accuracy-1][5]!=0 and plotinfo[i][0][5]!=0:
        intermediates = np.linspace(plotinfo[i][0][5], plotinfo[i][accuracy-1][5],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
        plotinfo[i][:, 5] = intermediates
        for j in range(0,accuracy):
            plotinfo[i][j] = FullyDefinernew(plotinfo[i][j])

    return plotinfo

def ratiochecker(properties,processes,ratios,i,newinfo):

    nextstate,prevstate = statename.adjstates(i)

    if ratios[i][0] != 0:
        if properties[nextstate][4] != 0 and properties[i][4] == 0:
            newinfo = True
            properties[i][4] = properties[nextstate][4] / ratios[i][0]

        elif properties[i][4] != 0 and properties[nextstate][4] == 0:
            newinfo = True
            properties[nextstate][4] = properties[i][4] * ratios[i][0]

        if processes[i][2] != 0:
            if properties[i][1] != 0 and properties[nextstate][1] == 0:
                properties[nextstate][1] = ((properties[i][1]**(gamma-1/gamma))*ratios[i][0])**(gamma/gamma-1)
                properties[nextstate][1] = accountT(properties[nextstate][1],properties[nextstate][1],i,processes)

            if processes[i][2]==1:

                if properties[nextstate][1] !=0 and properties[i][1] == 0:
                    properties[i][1] = (1/ratios[i][1])**(gamma-1/gamma)*properties[nextstate][0]
                if properties[i][2] != 0 and properties[nextstate][2] == 0:
                    properties[nextstate][2] = ((properties[nextstate][2]**(gamma-1))/ratios[i][0])**(1/(gamma-1))
                if properties[nextstate][2] == 0 and properties[i][2] == 0:
                    properties[nextstate] = (((properties[i][2]**(gamma-1)))/ratios[i][0])**(1/gamma-1)



    if ratios[i][1] != 0:

        if properties[nextstate][1] != 0 and properties[i][1] == 0:
            newinfo = True
            properties[i][1] = properties[nextstate][1] / ratios[i][1]

        elif properties[i][1] != 0 and properties[nextstate][1] == 0:
            newinfo = True
            properties[i][nextstate] = properties[i][1] * ratios[i][1]

        if processes[i][2] != 0:

            if properties[i][0] != 0 and properties[nextstate][0] == 0:
                newinfo = True
                properties[nextstate][0] = properties[i][0] * ratios[i][1] ** ((gamma - 1) / gamma)
                properties[nextstate] = accountT(properties[nextstate],properties[i],i,processes)

            if processes[i][2]==1:
                if properties[nextstate][0] !=0  and properties[i][0] == 0 :
                    newinfo = True
                    properties[i][0] = properties[nextstate][0] / ratios[i][1] ** ((gamma - 1) / gamma)

                if properties[i][2] != 0 and properties[nextstate][2] == 0:
                    newinfo = True
                    properties[nextstate][2] = (properties[i][2]**gamma)/ratios[i][1]

                if properties[nextstate][2] != 0 and properties[i][2] == 0:
                    newinfo = True
                    properties[i][2]=(properties[nextstate][2]**gamma)*ratios[i][1]





    if ratios[i][2] != 0:

        if properties[nextstate][2] != 0 and properties[i][2] == 0:
            newinfo = True
            properties[i][2] = properties[nextstate][2] / ratios[i][2]

        elif properties[i][2] != 0 and properties[nextstate][2] == 0:
            newinfo = True
            properties[nextstate][2] = properties[i][2] * ratios[i][2]

        if processes[i][2] != 0:

            if properties[i][0] != 0 and properties[nextstate][0] == 0:
                properties[nextstate][0] = properties[i][0]/ratios[i][2]**(gamma-1)
                properties[nextstate] = accountT(properties[nextstate],properties[i],i,processes)
            if processes[i][2]==1:

                if properties[nextstate][0] != 0 and properties[i][0] == 0:
                    properties[i][0] = properties[nextstate][0]/ratios[i][2]**(gamma-1)

                if properties[i][1] != 0 and properties[nextstate][1] == 0:
                    properties[nextstate][1] = properties[i][1]/ratios[i][2]**gamma


                if properties[nextstate][1] != 0 and properties[i][1] == 0:
                    properties[i][1] = properties[nextstate][1]*ratios[i][2]**gamma

    return newinfo,properties