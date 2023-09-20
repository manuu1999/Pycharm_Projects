def local_maxima():
    li = [2,5,4,3,3,7,6,1]
    li2 = []
    for i in li:
        index = 0
        index2 = 2
        if i > li[index] and i > li[index2]:
            li2.append(i)
        else:
            pass
        index +=1
        index2 +=1
    print(li2)

local_maxima()


