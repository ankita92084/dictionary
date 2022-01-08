count={}
word=input("enter a word")
for i in word:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print(count)


count={}
a=["a","n","k","i","t","a"]
for i in a:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print(count)



a="MISSISSIPPI"
count={}
for i  in a:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print(count)





