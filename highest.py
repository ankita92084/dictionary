my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
print(max)