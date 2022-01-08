dic={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
sort={}
for i in dic:
    a=dic[i]
    for j in dic:
        b=dic[j]
        if b>a:
            sort[j]=a
print(sort)


