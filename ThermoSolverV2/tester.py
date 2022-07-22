from definer import FullyDefinernew,mgetH
from isenaccounters import isenaccounterbackv2
from info import gamma
cat = [0]*6
dog = [0]*6
cat[0]=300
cat[1]=10*10**5
dog[1] = 100*10**5
dog[0] = 586.005
dog = mgetH(dog,0)

print(cat)
print(dog)
cat = FullyDefinernew(cat)
print(cat)
dog = isenaccounterbackv2(dog,cat,2,0)
print(dog)