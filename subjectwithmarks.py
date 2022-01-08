
a=[{"math":5,"science":7},{"math":4,"sience":8},{"math":2,"science":6}]
sub=str(input("enter the subject: "))
add=0
for i in range(len(a)):
    for j in a[i]:
        if j==sub:
            add+=a[i][j]
print(add)









