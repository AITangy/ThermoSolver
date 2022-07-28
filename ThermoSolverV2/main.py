
from definer import  CheckDefine, defmessage
from relationships import CheckRelation
from qandw import calcqandw, useqandw
from plotter import plotaround, plotPv,plotTs,ploths
from propertiesaround import checkaround
from info import properties, processes,ratios,  definedstates, plotinfo,  numberofstates


def mainsolver(properties,processes,ratios,plotinfo,definedstates,plotnumber):


    newinfo = True                                                                                                      # Defining a variable to check with each pass whether we have got some new information
    passes = 0
    while newinfo == True:

        passes = passes + 1                                                                                             # This is for debugging / optimisation purposes to see how many times it is needed to loop through the states to solve all the variables.
        newinfo = False
        for i in range(0, numberofstates):                                                                              # Looping through each state.
                                                                                                                        # Initiallising a sum of the number of information in each state
                                                                                                                        # Looping through each property within a state.
            if definedstates[i]==False:
                properties,plotinfo,definedstates,newinfo = CheckDefine(i,properties,plotinfo,definedstates,newinfo)
            newinfo,properties,plotinfo = CheckRelation(i,newinfo, properties,processes,ratios,plotinfo)
                                                                                                                        # If we have information on next h and previous h and are missing information on q or w but have one of them then we can calulate the other
# Calulcating information on Qtransfer or Wtransfer
            properties,processes = calcqandw(properties,processes,i)
# Utilising information on Qtransfer and Wtransfer
            properties,processes = useqandw(properties,processes,i)

# We need to solve for information on properties around every defined state, and account for the intermediate information which should be plotted
            properties,plotinfo,newinfo,definedstates = checkaround(properties,processes,ratios,plotinfo, definedstates,newinfo, i)

    defmessage(definedstates,properties)

    plotaround(plotinfo,plotnumber,processes)





mainsolver(properties,processes,ratios,plotinfo,definedstates,0)













