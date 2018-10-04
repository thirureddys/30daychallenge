# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(raw_input())):
    s=raw_input()
    ev=[]
    od=[]
    for i in range(len(s)):
        if i == 0:
            ev.append(s[i])
        elif i%2 == 0:
            ev.append(s[i])
        else:
            od.append(s[i])

    print ''.join(ev) +" "+''.join(od)
