from definer import FullyDefinernew
from info import processes

def isenaccounter(i,nextstate,isenproperties,definedstates, properties):




    if processes[i][2] == 1:
        properties[nextstate] = isenproperties[nextstate]
        definedstates[nextstate] = True                                                                                 # Ensuring the code understands that the algorythm has defined the next state so no need to waste code redefining it.
    else:
        if processes[i][5] == "Compressor" or processes[i][5] =="Pump" or processes[i][5] == "Heater" and processes[i][2]!=0:

            properties[nextstate][4] = (isenproperties[nextstate][4] - properties[i][4]) / processes[i][2] + properties[i][4]
            properties[nextstate] = FullyDefinernew(properties[nextstate])
            definedstates[nextstate] = True

        elif processes[i][5] == "Turbine" or processes[i][5]=="Cooler" and processes[i][2]!=0:
            properties[nextstate][4] = processes[i][2] * (isenproperties[nextstate][4] - properties[i][4]) + properties[i][4]
            properties[nextstate] = FullyDefinernew(properties[nextstate])
            definedstates[nextstate] = True
    return definedstates,properties

def isenaccounterback(i,prevstate,isenproperties,definedstates,properties):





    if processes[prevstate][2] == 1:
        properties[prevstate] = isenproperties[prevstate]
        definedstates[prevstate] = True                                                                                 # Ensuring the code understands that the algorythm has defined the next state so no need to waste code redefining it.
    else:
        if processes[prevstate][5] == "Compressor" or processes[prevstate][5] =="Pump" or processes[prevstate][5] == "Heater" and processes[prevstate][2]!=0:

            properties[prevstate][4] = (isenproperties[prevstate][4] - properties[i][4]) / processes[i][2] + properties[i][4]
            properties[prevstate] = FullyDefinernew(properties[prevstate])
            definedstates[prevstate] = True

        elif processes[prevstate][5] == "Turbine" or processes[prevstate][5]=="Cooler" and processes[prevstate][2]!=0:

            properties[prevstate][4] = processes[i][2] * (isenproperties[prevstate][4] - properties[i][4]) + properties[i][4]
            properties[prevstate] = FullyDefinernew(properties[prevstate])
            definedstates[prevstate] = True
    return definedstates,properties


def isenaccounterbackv2(undefstate,defstate,prevstate,i):


    if processes[prevstate][5] == ["Compressor"] or processes[prevstate][5] == ["Pump"] or processes[prevstate][5] == ["Heater"]:

        undefstate[4] = processes[i][2] * (undefstate[4] - defstate[4]) + defstate[4]

        undefstate = FullyDefinernew(undefstate)

        # The current way Fully Definer alogrythm works is under the assumptiion that we import the full list of properites
        # We need to modify the fully definer algorythm to account for the fact that we might not have the full list of porperites in our system and to jjust solve what it can...


    if processes[prevstate][5] == ["Turbine"] or processes[prevstate][5]==["Cooler"]:

        undefstate[4] = (undefstate[4] - defstate[4]) / processes[prevstate][2] + defstate[4]

        undefstate = FullyDefinernew(undefstate)



    return undefstate

