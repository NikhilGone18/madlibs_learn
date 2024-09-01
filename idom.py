largest = -1
print("before",largest)
for x in [12,4,5,99,26,10]:
    if largest < x :
        largest =x
    print(largest ,'', x)
print("after ", largest)