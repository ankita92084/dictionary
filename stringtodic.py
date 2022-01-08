a={}
Sample_string ='w3resource'
for i in Sample_string:
    if i not in a:
        a[i]=1
    else:
        a[i]=a[i]+1
print(a)




