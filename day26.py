da, ma, ya = map(int,raw_input().split(' '))
de, me, ye = map(int,raw_input().split(' '))
fine = 0
if(ye==ya):
    if(me < ma):
        fine = (ma - me) * 500
    elif((me == ma) and (de < da)):
        fine = (da - de) * 15
elif(ye < ya):
    fine = 10000

print fine
  
