#Input: (1,2),(2,1),(3,4),(4,5),(5,4)
#Output: (2,1) (5,4)

list1 = [[1,2],[2,1],[3,4],[4,5],[5,4]]
for i in list1:
    a = (i[1], i[0])
    a =list(a)
    
    if a in list1:
        print(i)
    