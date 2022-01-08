dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("the original dictionary"+str(dic))
res=[key for key in dic if all(dic[temp]>=dic[key]for temp in dic)]
print("keys with minimum vales are"+str(res))
