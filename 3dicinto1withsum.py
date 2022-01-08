dic1={"a":100,"b":300,"c":4}
dic2={"a":400,"b":900,"d":4}
dic3={"a":400,"b":40,"c":4}
dic4={}
for i in dic1:
    if i in dic2 and dic3:
        dic4[i]=dic1[i]+dic2[i]+dic3[i]
    elif i in dic2:
        dic4[i]=dic[i]+dic2[i]
    elif i in dic3:
        dic4[i]=dic1[i]+dic3[i]
    else:
        dic4[i]=dic1[i]
for j in dic2:
    if j in dic3 and j not in dic2:
        dic4[i]=dic2[j]+dic3[j]
    if j in dic3:
        dic4[j]=dic2[j]+dic3[i]
    if j not in dic3:
        dic4[j]=dic2[j]
for k in dic3:
    if k not in dic2 and k not in dic1:
        dic4[k]=dic3[k]
print(dic4)
    


