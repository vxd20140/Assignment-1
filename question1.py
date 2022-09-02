ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("BEFORE SORTING:"+str(ages))
#SORT A LIST USING SORT()
ages.sort()
print("AFTER SORTING:"+str(ages))
#MIN AND MAX IS PREDEFINED USED TO FIND MAX AND MIN ELEMENTS IN LIST
minimum = min(ages)
maximum = max(ages)
print("MINIMUM AGE: "+str(minimum)+"  MAXIMUM AGE: "+str(maximum))
print("adding mininum and maximum ages to the list")
ages.extend([minimum,maximum])
print("AGES:"+str(ages))
#LEN() IS USED TO FIND THE LENGTH OF ITERATOR
l=len(ages)
MEDIAN=(ages[l//2]+ages[-1-l//2])/2 # MEDIAN IS THE MIDDLE ELEMENT OF THE SET OF ELEMENTSa
print("MEDIAN: "+str(MEDIAN))
average = sum(ages)/len(ages)
print("AVERAGE :"+str(sum(ages)/l))
print("RANGE :"+str(maximum-minimum))#RANGE IS DIFFERENCE BETWEEN MIN AND MAX
