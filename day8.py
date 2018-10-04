n=int(raw_input())
d={}
keys=[]
values=[]
for i in range(n):
    g=raw_input().split()
    keys.append(g[0])
    values.append(g[1])
d=dict(zip(keys,values))
print d
while(1):
    temp=''
    name=raw_input()
    if name in d.keys():
        print name+"="+d[name]
    else:
        print "Not found"
        
    
    
    
