i=0
a=[]
b={}
k=1
while i<=50:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        a.append(i)
        b[k]=i
        k+=1
        # print(i,"prime number ")
    i+=1
print( 'prime number list= ',a,"\n")
print('prime number dictonary = ',b)



