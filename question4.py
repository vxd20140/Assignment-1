it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("LENGTH OF IT_COMPANIES SET:"+str(len(it_companies)))
print("APPENDING ANOTHER ITEM INTO IT_COMPANIES")
print("IT_COMPANIES BEFORE :"+str(it_companies))
it_companies.update({'CISCO'})#APPENDING NEW VALUE INTO LIST
print("IT_COMPANIES AFTER UPDATING :"+str(it_companies))
it_companies.update({'NETFLIX','Alphabet'})
print("ADD MORE COMPANIES INTO IT_COMPANIES:"+str(it_companies))
print("IT_COMPANIES BEFOR DELETING :"+str(it_companies))
it_companies.discard("NETFLIX")#DOES'NT RAISE ERROR IF ITEM IS NOT THERE
it_companies.remove("Apple")#RAISES AN ERROR IF ITEM IS NOT THERE
print("IT_COMPANIES AFTER DELETING :"+str(it_companies))
print("A JOIN B: "+str(A.union(B)))
print("A INTERSECTION B: "+str(A.intersection(B)))
print("A SUBSET OF B: "+str(A.issubset(B)))
print(" A DISJOINT B:"+str(A.isdisjoint(B)))
print("A WITH B JOIN B WITH A: "+str(A.union(B).union(B.union(A))))
print(" SYMMETRIC DIFFERENCE B/W A AND B: "+str(A.symmetric_difference(B)))
print("DELETING ALL SETS:")
del A,B,it_companies #DEL IS USED TO DELETE ITERATORS
#CONVERSION OF LIST TO SET USING SET() METHOD
print("AGE IN LIST FORM:"+str(age)+" WITH LENGTH "+str(len(age)))
age=set(age)
print("AGE IN SET FORM:"+str(age)+" WITH LENGTH "+str(len(age)))
