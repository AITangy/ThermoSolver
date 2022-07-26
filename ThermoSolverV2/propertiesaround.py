from statename import adjstates
from isenaccounters import isenaccounterv2
from definer import mgetH,FullyDefinernew

import numpy as np
import math
from info import accuracy,M,R,Cp,Cv,gamma



def checkaround(properties, processes,ratios,plotinfo, definedstates,newinfo, i):
    nextstate,prevstate = adjstates(i)
    isenproperties = np.copy(properties)

    if definedstates[i] == True:
        if definedstates[nextstate] == False:                                                                   # Checking if future state is defined or not and if not trying to use the information it has along with the adjacent fully defined state to define it.

            if properties[nextstate][0] != 0 and processes[i][2] == 1:
                # We can only use T to fully define the system when it is isentropic, otherwise the other property we can calculate must be enthalpy, and enthalpy and temprerature alone is not enough to define the perfect gas state.

                newinfo = True
                properties[nextstate][1] = (1/(gamma-1)) * math.log((properties[i][0]* (properties[i][2]**(gamma-1)))/properties[nextstate][0])
                                                                                                                # We want to fully define the isentropic matrix to allow us to use its values if it turns out to be good, this could also aid in drawing graphs where we could use the isentropic case to show how isentropic efficencies are affecting the graph, sicne the isentropic stuff updates each tijme perhaps we need a "saved" one which keeps the isentropic function rather than updating with the main so we can seperate what was calculated isentropically and graph it distinctly
                properties[nextstate] = FullyDefinernew(isenproperties[nextstate])
                definedstates[nextstate]=True
                plotinfo[i][0] = properties[i]
                plotinfo[nextstate][0] = properties[nextstate]
                plotinfo[i][accuracy - 1] = properties[nextstate]
                intermediates = np.linspace(plotinfo[i][0][0], plotinfo[nextstate][0][0],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[i][:, 0] = intermediates


                for j in range(0, accuracy):
                    if processes[i][2] ==1:
                        plotinfo[i][j][1] = (plotinfo[i][j][0]/properties[i][0] * (properties[i][1])**((gamma-1)/gamma))**(gamma/(gamma-1))
                        plotinfo[i][j]=FullyDefinernew(plotinfo[i][j])





            elif properties[nextstate][1] !=0 and processes[i][2]!=0:

                newinfo = True

                properties[nextstate][0] = properties[i][0] * (properties[nextstate][1]/properties[i][1])**((gamma-1)/gamma)

                properties[nextstate] = mgetH(properties[nextstate],0)

                properties[nextstate] = isenaccounterv2(properties[nextstate],properties[i],i,processes)
                definedstates[nextstate] = True


                plotinfo[i][0] = properties[i]
                plotinfo[nextstate][0] = properties[nextstate]
                plotinfo[i][accuracy - 1] = properties[nextstate]
                intermediates = np.linspace(plotinfo[i][0][1], plotinfo[nextstate][0][1],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[i][:, 1] = intermediates




                for j in range(0, accuracy):
                    if processes[i][2] !=0:

                        plotinfo[i][j][0] = properties[i][0] * (plotinfo[i][j][1]/properties[i][1])**((gamma-1)/gamma)
                        plotinfo[i][j] = mgetH(plotinfo[i][j],0)
                        plotinfo[i][j] = isenaccounterv2(plotinfo[i][j],properties[i],i,processes)




            elif properties[nextstate][2]!=0 and processes[i][2]!=0:
                newinfo = True

                properties[nextstate][0] = properties[i][0]*(properties[i][2]/properties[nextstate][2])**(gamma-1)

                properties[nextstate] = mgetH(properties[nextstate], 0)

                properties[nextstate] = isenaccounterv2(properties[nextstate], properties[i], i, processes)
                definedstates[nextstate] = True
                plotinfo[i][0] = properties[i]
                plotinfo[nextstate][0] = properties[nextstate]
                plotinfo[i][accuracy - 1] = properties[nextstate]
                intermediates = np.linspace(plotinfo[i][0][2], plotinfo[nextstate][0][2],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[i][:, 2] = intermediates



                for j in range(0, accuracy):
                    if processes[i][2] != 0:

                        plotinfo[i][j][0] = properties[i][0]*(properties[i][2]/plotinfo[i][j][2])**(gamma-1)
                        plotinfo[i][j] = mgetH(plotinfo[i][j], 0)
                        plotinfo[i][j] = isenaccounterv2(plotinfo[i][j], properties[i], i, processes)



            if ratios[i][0]!=0 and processes[i][2]!=0:
                if properties[i][1]!=0 and properties[nextstate][1]==0:
                    print()
                if properties[nextstate][1]==0 and properties[i][1]==0:
                    print()
                if properties[i][2]!=0 and properties[nextstate][2]==0:
                    print()
                if properties[nextstate][2]==0 and properties[i][2]==0:
                    print()


            if ratios[i][1]!=0 and processes[i][2]!=0:
                if properties[i][0] != 0 and properties[nextstate][0] == 0:
                    print()
                if properties[nextstate][0] == 0 and properties[i][0] == 0:
                    print()
                if properties[i][2] != 0 and properties[nextstate][2] == 0:
                    print()
                if properties[nextstate][2] == 0 and properties[i][2] == 0:
                    print()

            if ratios[i][2]!=0 and processes[i][2]!=0:
                if properties[i][0] != 0 and properties[nextstate][0] == 0:
                    print()
                if properties[nextstate][0] == 0 and properties[i][0] == 0:
                    print()
                if properties[i][1] != 0 and properties[nextstate][1] == 0:
                    print()
                if properties[nextstate][1] == 0 and properties[i][1] == 0:
                    print()





        if definedstates[prevstate] == False:

            if properties[prevstate][0] != 0 and processes[prevstate][2] == 1 and definedstates[prevstate] == False:
                newinfo = True

                properties[prevstate][1] = (1/(gamma-1)) * math.log((properties[i][0]* (properties[i][2]**(gamma-1)) )/properties[prevstate][0])
                properties[prevstate] = FullyDefinernew(isenproperties[prevstate])
                definedstates[prevstate] = True
                plotinfo[i][0] = properties[i]
                plotinfo[prevstate][0] = properties[prevstate]
                plotinfo[prevstate][accuracy - 1] = properties[i]
                intermediates = np.linspace(plotinfo[prevstate][0][1], plotinfo[i][0][1],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[prevstate][:, 1] = intermediates

                for j in range(0,accuracy):
                    newinfo = True
                    plotinfo[prevstate][j][1] = (1 / (gamma - 1)) * math.log((properties[i][0] * (properties[i][2] ** (gamma - 1))) / plotinfo[prevstate][j][0])
                    plotinfo[prevstate][j] = FullyDefinernew(plotinfo[prevstate[j]])




            elif properties[prevstate][1] != 0 and processes[prevstate][2]==1 and definedstates[prevstate] == False:
                newinfo = True


                properties[prevstate][0] = properties[i][0] * (properties[prevstate][1] / properties[i][1]) ** ((gamma - 1) / gamma)
                properties[prevstate] = FullyDefinernew(properties[prevstate])
                definedstates[prevstate] = True
                plotinfo[i][0] = properties[i]
                plotinfo[prevstate][0] = properties[prevstate]
                plotinfo[prevstate][accuracy - 1] = properties[i]
                intermediates = np.linspace(plotinfo[prevstate][0][1],plotinfo[i][0][1],num=accuracy)                 # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[prevstate][:,1] = intermediates

                for j in range(0, accuracy):
                    newinfo = True
                    plotinfo[prevstate][j][0] = properties[i][0] * (plotinfo[prevstate][j][1]/properties[i][1])**((gamma - 1) / gamma)
                    plotinfo[prevstate][j] = FullyDefinernew(plotinfo[prevstate][j])

            elif properties[prevstate][2] != 0 and processes[prevstate][2]==1 and definedstates[prevstate] == False:
                newinfo = True
                properties[prevstate][1] = properties[i][1] * (properties[i][2] / properties[prevstate][2]) ** (gamma)

                properties[prevstate] = FullyDefinernew(isenproperties[prevstate])
                definedstates[prevstate] = True
                plotinfo[i][0] = properties[i]
                plotinfo[prevstate][0] = properties[prevstate]
                plotinfo[prevstate][accuracy - 1] = properties[i]
                intermediates = np.linspace(plotinfo[prevstate][0][1], plotinfo[i][0][1],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[prevstate][:, 1] = intermediates

                for j in range(0, accuracy):
                    newinfo = True
                    plotinfo[prevstate][j][1] = properties[i][1] * (properties[i][2] / plotinfo[prevstate][j][2]) ** (gamma)
                    plotinfo[prevstate][j] = FullyDefinernew(plotinfo[prevstate[j]])




















    return properties,plotinfo,newinfo,definedstates




