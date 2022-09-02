#CREATING DOG AND STUDENTS DICTIONARY
dog={'Name':'Jimmy','Color':'black','Breed':'Poodle','Legs':4,'Age':3}
print("Dog= "+str(dog))
student={'first_name':'Henry','last_name':'john','gender':'Male','age':21,'marital_status':'married','skills':['Machine learning','devops','python'],'country':'USA','city':'New york','address':'5th avenue, tensor city'}
print("Student= "+str(student))
LENGTH=len(student)
type_skill=type(student['skills'])#TYPE CAN FIND THE DATATYPE
print("STUDENT DICT LENGTH= "+str(LENGTH))
print("key values of skills="+str(student['skills'])+"and type is "+str(type_skill))
student['skills'].extend(['Data Structures'])#EXTEND APPENDS THE ELEMENT AT THE END
print("Adding another skill to skills key"+str(student['skills']))
print("---keys and values of dog----")
print("KEYS= "+str(list(dog.keys())))#.KEYS() RETURNS THE LIST OF KEYS IN A DICTIONARY
print("VALUES= "+str(list(dog.values())))#.VALUES() RETURNS THE LIST OF VALUES IN A DICTIONARY
print("---keys and values of student----")
print("KEYS= "+str(list(student.keys())))
print("VALUES= "+str(list(student.values())))
