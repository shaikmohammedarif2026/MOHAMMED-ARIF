t = [[1,2],[3,4],[5,6]]
v=[]
for i in t:
    for j in i:
        b =list(map(lambda j: j+5, i ))
        v.append(b)
        print(v)
