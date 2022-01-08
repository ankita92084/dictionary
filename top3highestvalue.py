my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
max=0
second_max=0
third_max=0
for x in my_dict:
    if my_dict[x]>max:
        third_max=second_max
        second_max=max
        max=my_dict[x]
    elif my_dict[x]>second_max:
        third_max=second_max
        second_max=my_dict[x]
print(max,second_max,third_max)

