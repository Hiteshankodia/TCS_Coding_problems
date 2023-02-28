num = int(input("ENTER length of AP:"))
ele = 0
AP = []
for i in range(1, num+1):
    ele = int(input("ENTER THE " + str(i) +"th AP NUMBER:"))
    AP.append(ele)

AP = [2,3,4,5]
num = len(AP)

if len(AP)>=2:    
  a = AP[0]
  d = AP[1] - AP [0]
 
  sum_of_AP = int((num / 2) * ((2*a) + (num-1)*d))
  print(sum_of_AP)