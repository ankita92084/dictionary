Original_dictionary={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a={}
for x,y in Original_dictionary.items():
    space={x.replace(" ", ""):y}
    a.update(space)
print(a)
