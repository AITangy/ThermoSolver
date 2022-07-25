from definer import FullyDefinernew,mgetH
from isenaccounters import isenaccounterv2
from info import M,R,Cp,Cv,gamma
import numpy as np
numberofstates = 3
startstate = 2
i = 0
processes = np.zeros([numberofstates,8], dtype=object)

processes[startstate][2] = 0.85
processes[startstate][5] = ["Compressor"]


undefstate = [0]*6
defstate = [0]*6

defstate[0] = 300
defstate[1] = 10*10**5
defstate = FullyDefinernew(defstate)

undefstate[1] = 100*10**5                   # If only undefstate[0] is defined then isentropic fefficiencty does not give us new iformation as it operates on the pricniple that the tempreture ois not yet defined
undefstate[0] = 586                         # Normally we woild use a simple alogrythm for this but here we just input it for testing puorpose.
undefstate = mgetH(undefstate,0)



undefstate = isenaccounterv2(undefstate,defstate,startstate,processes)

print(undefstate)
