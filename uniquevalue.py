data=[{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
b=[]
for i in range(len(data)):
    for j in data[i]:
        if data[i][j] not in b:
            b.append(data[i][j])
print(b)