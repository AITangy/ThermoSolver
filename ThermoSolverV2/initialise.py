import numpy as np

#initialise.py defines data structures


                                                                                                                        # defining variables
accuracy = 20                                                                                             # Determines the number of points that will be plotted for each process.
numberofstates  = 3                                                                                                 # =numberofcompoenents = numberofprocesses
numberofplots = 4

T= [0]*numberofstates                                                                                                   # intiallising lists of properties
P=[0]*numberofstates
v= [0]*numberofstates
u= [0]*numberofstates
h=[0]*numberofstates
s =[0]*numberofstates


mflowrate = [0]*numberofstates                                                                                          # initiallising lists of processes
isenefficiency = [0]*numberofstates
qtransfer =[""]*numberofstates                                                                                          # Q transfer and W transfer have been initialised to an empty string rather than 0 due to the fact that these variables could potentially be 0, e.g. q transfer would be 0 in the adiabatic case.
wtransfer =[""]*numberofstates
c = [0] * numberofstates
z = [0] * numberofstates                                                                                                # Even though c and z can be 0, we still intitialise them as such as we can assume that c and z are negligible unless we are given information on them.
processtype = ["p"]*numberofstates
componenttype = ["p"]*numberofstates





Tratio = [0]*numberofstates                                                                                             # intiallising lists of ratios
Pratio = [0]*numberofstates
vratio = [0]*numberofstates






properties = np.zeros([numberofstates,6])                                               # intiallising 2d arrays to hold properties/processes/ratios info
processes = np.zeros([numberofstates,8], dtype=object)
ratios = np.zeros([numberofstates,3])
plotinfo = np.zeros([numberofstates,accuracy,6])                                                         # The 3d matrix is alot of data to pass around to just pass around one 2d slice of it at a time into what we are doing.
graphs = np.zeros([numberofplots,numberofstates,accuracy,6])


definedstates = np.zeros([numberofstates], dtype=bool)


