#CREATING LIST OF WORDS FOR TABLE TO SEPERATE WITH TABS
A=['Name','\tAge','Country','City']
B=['Asabeneh','250','finland','Helsinki']
st=''
st2=''
for i in A:
    st+=i+'\t'
print(st)
for i in B:
    st2+=i+'\t'
print(st2)


