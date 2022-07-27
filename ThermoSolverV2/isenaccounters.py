from definer import FullyDefinernew





def isenaccounterv2(undefstate,defstate,startstate,processes):


    if processes[startstate][5] == ["Compressor"] or processes[startstate][5] == ["Pump"] or processes[startstate][5] == ["Heater"] or processes[startstate][5] == ["Combustor"]:
        undefstate[4] = (undefstate[4] - defstate[4]) / processes[startstate][2] + defstate[4]



        undefstate = FullyDefinernew(undefstate)

        # The current way Fully Definer alogrythm works is under the assumptiion that we import the full list of properites
        # We need to modify the fully definer algorythm to account for the fact that we might not have the full list of porperites in our system and to jjust solve what it can...


    if processes[startstate][5] == ["Turbine"] or processes[startstate][5]==["Cooler"]:

        undefstate[4] = processes[startstate][2] * (undefstate[4] - defstate[4]) + defstate[4]

        undefstate = FullyDefinernew(undefstate)



    return undefstate

def accountT(undefstate,defstate,startstate,processes):

    if processes[startstate][5] == ["Compressor"] or processes[startstate][5] == ["Pump"] or processes[startstate][5] == ["Heater"] or processes[startstate][5] == ["Combustor"]:
        undefstate[0] = (undefstate[0] - defstate[0]) / processes[startstate][2] + defstate[0]

        # The current way Fully Definer alogrythm works is under the assumptiion that we import the full list of properites
        # We need to modify the fully definer algorythm to account for the fact that we might not have the full list of porperites in our system and to jjust solve what it can...


    if processes[startstate][5] == ["Turbine"] or processes[startstate][5]==["Cooler"]:

        undefstate[0] = processes[startstate][2] * (undefstate[0] - defstate[0]) + defstate[0]


    return undefstate