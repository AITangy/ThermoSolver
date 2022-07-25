from statename import adjstates
from isenaccounters import isenaccounterv2
from definer import mgetH,FullyDefinernew
from constants import *
import numpy as np
import math
from info import accuracy



def checkaround(properties, processes,plotinfo, definedstates,newinfo, i):
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






                # Now that we have caluclated some new properties we outhgt to try and plot what is going on... It could ctreate a real problem if the system is overdefcined, even if it is correct if two states are fully defined and adjacent from the outset we are not going to be able to plot the stuff inbetween

            elif properties[nextstate][1] !=0 and processes[i][2]!=0:

                newinfo = True

                properties[nextstate][0] = properties[i][0] * (properties[nextstate][1]/properties[i][1])**((gamma-1)/gamma)

                properties[nextstate] = mgetH(properties[nextstate],0)

                properties[nextstate] = isenaccounterv2(properties[nextstate],properties[i],i,processes)


                # plotinfo[i][0] = properties[i]
                # plotinfo[i][accuracy - 1] = properties[nextstate]
                # plotinfo[nextstate][0] = properties[nextstate]

            elif properties[nextstate][2]!=0 and processes[i][2]!=0:
                newinfo = True

                properties[nextstate][0] = properties[i][0]*(properties[i][2]/properties[nextstate][2])**(gamma-1)

                properties[nextstate] = mgetH(properties[nextstate], 0)

                properties[nextstate] = isenaccounterv2(properties[nextstate], properties[i], i, processes)

            # plotinfo[i][0] = properties[i]
                # plotinfo[i][accuracy - 1] = properties[nextstate]
                # plotinfo[nextstate][0] = properties[nextstate]



        if definedstates[prevstate] == False:

            if properties[prevstate][0] != 0 and processes[prevstate][2] == 1 and definedstates[prevstate] == False:
                newinfo = True

                properties[prevstate][1] = (1/(gamma-1)) * math.log((properties[i][0]* (properties[i][2]**(gamma-1)) )/properties[prevstate][0])


                properties[prevstate] = FullyDefinernew(isenproperties[prevstate])




                # plotinfo[i][0] = properties[i]
                # plotinfo[prevstate][accuracy-1] = properties[i]
                # plotinfo[prevstate][0] = properties[prevstate]


            elif properties[prevstate][1] != 0 and processes[prevstate][2]==1 and definedstates[prevstate] == False:
                newinfo = True


                properties[prevstate][0] = properties[i][0] * (properties[prevstate][1] / properties[i][1]) ** ((gamma - 1) / gamma)
                properties[prevstate] = FullyDefinernew(properties[prevstate])








                                    # Im going to modularise this algorythm and place it as a functiom within a different module.
                plotinfo[i][0] = properties[i]
                plotinfo[prevstate][0] = properties[prevstate]
                plotinfo[prevstate][accuracy - 1] = properties[i]
                intermediates = np.linspace(plotinfo[prevstate][0][1],plotinfo[i][0][1],num=accuracy)                 # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
                plotinfo[prevstate][:,1] = intermediates

                for j in range(0,accuracy):
                    if processes[prevstate][2] != 0:                             # We need to account for the fact that if the info is about T then it only works if isentropic!
                        newinfo = True
                        plotinfo[prevstate][j][0] = properties[i][0] * (plotinfo[prevstate][j][1]/properties[i][1])**((gamma - 1) / gamma)  # here we are storing the isentropic Tempreturues, however now we need to account for isentropic efficiency and store the real tempreratures
                        isenindex = 0                                                                                   # Setting a vairable to track which property has the isentropic assumption in order to remove it once the algorythm has calculated h
                        plotinfo[prevstate][j] = mgetH(plotinfo[prevstate][j],isenindex)                                        # We don't actually want to define the whole thing herre, what we need is an algorythm that will just get us h!
                        plotinfo[prevstate][j] = isenaccounterv2(plotinfo[prevstate][j],properties[i],prevstate,processes)
                current,prevprevstate = adjstates(prevstate)
                plotinfo[prevprevstate][accuracy-1] = plotinfo[prevstate][0]                                            # This alogrytm is really nice hiowever it really does not make any sense to use it in thw backwards fashion





            elif properties[prevstate][2] != 0 and processes[prevstate][2]==1 and definedstates[prevstate] == False:
                newinfo = True
                properties[prevstate][1] = properties[i][1] * (properties[i][2] / properties[prevstate][2]) ** (gamma)

                properties[prevstate] = FullyDefinernew(isenproperties[prevstate])



                # plotinfo[i][0] = properties[i]
                # plotinfo[prevstate][accuracy - 1] = properties[i]
                # plotinfo[prevstate][0] = properties[prevstate]
                #
                # intermediates = np.linspace(plotinfo[prevstate][0][2], plotinfo[i][0][2], num=10)
                #
                # plotinfo[prevstate][:, 2] = intermediates
                #
                # for j in range(0,accuracy):
                #
                #     plotinfo[prevstate][j][0] = properties[i][0] * (plotinfo[prevstate][j][1]/properties[i][1])**((gamma - 1) / gamma)
                #     plotinfo[prevstate] = FullyDefiner(plotinfo[prevstate],j)

    return properties,plotinfo,newinfo



def intermediatestatesP(properties,plotinfo,newinfo,i,proptype,processes):
    nextstate,prevstate = adjstates(i)

    # Im going to modularise this algorythm and place it as a functiom within a different module.
    plotinfo[i][0] = properties[i]
    plotinfo[prevstate][0] = properties[prevstate]
    plotinfo[prevstate][accuracy - 1] = properties[i]
    intermediates = np.linspace(plotinfo[prevstate][0][proptype], plotinfo[i][0][proptype],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
    plotinfo[prevstate][:, proptype] = intermediates



    for j in range(0, accuracy):

        if processes[prevstate][2] != 0:  # We need to account for the fact that if the info is about T then it only works if isentropic!
            newinfo = True
            plotinfo[prevstate][j][0] = properties[i][0] * (plotinfo[prevstate][j][1] / properties[i][1]) ** ((gamma - 1) / gamma)  # here we are storing the isentropic Tempreturues, however now we need to account for isentropic efficiency and store the real tempreratures

            isenindex = 0  # Setting a vairable to track which property has the isentropic assumption in order to remove it once the algorythm has calculated h
            plotinfo[prevstate][j] = mgetH(plotinfo[prevstate][j],isenindex)  # We don't actually want to define the whole thing herre, what we need is an algorythm that will just get us h!
            plotinfo[prevstate][j] = isenaccounterv2(plotinfo[prevstate][j], properties[i], prevstate, processes)
    current, prevprevstate = adjstates(prevstate)
    plotinfo[prevprevstate][accuracy - 1] = plotinfo[prevstate][0]  # This alogrytm is really nice hiowever it really does not make any sense to use it in thw backwards fashion

    return properties,plotinfo,newinfo


def intermediatestatesv(properties, plotinfo, newinfo, i, proptype, processes):
    nextstate, prevstate = adjstates(i)

    # Im going to modularise this algorythm and place it as a functiom within a different module.
    plotinfo[i][0] = properties[i]
    plotinfo[prevstate][0] = properties[prevstate]
    plotinfo[prevstate][accuracy - 1] = properties[i]
    intermediates = np.linspace(plotinfo[prevstate][0][proptype], plotinfo[i][0][proptype],num=accuracy)  # here we solve for P becuause this is the data that was already there, the rest of the data will be solved off this.
    plotinfo[prevstate][:, proptype] = intermediates

    for j in range(0, accuracy):

        if processes[prevstate][
            2] != 0:  # We need to account for the fact that if the info is about T then it only works if isentropic!
            newinfo = True
            plotinfo[prevstate][j][0] = properties[i][0] * (plotinfo[prevstate][j][1] / properties[i][1]) ** (( gamma - 1) / gamma)  # here we are storing the isentropic Tempreturues, however now we need to account for isentropic efficiency and store the real tempreratures


            isenindex = 0  # Setting a vairable to track which property has the isentropic assumption in order to remove it once the algorythm has calculated h
            plotinfo[prevstate][j] = mgetH(plotinfo[prevstate][j],isenindex)  # We don't actually want to define the whole thing herre, what we need is an algorythm that will just get us h!
            plotinfo[prevstate][j] = isenaccounterv2(plotinfo[prevstate][j], properties[i], prevstate, processes)
    current, prevprevstate = adjstates(prevstate)
    plotinfo[prevprevstate][accuracy - 1] = plotinfo[prevstate][0]  # This alogrytm is really nice hiowever it really does not make any sense to use it in thw backwards fashion

    return properties, plotinfo, newinfo
