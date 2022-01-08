# Q4. Find keys with duplicate values in the dictionary?

dic={"ball":"red","bat":4,"wickets":4,"boll":"red","match":3}
dic2={}
for i in dic:
    for j in dic:
        if dic[j] not in dic2:
            dic2.update(dic)
print(dic2)