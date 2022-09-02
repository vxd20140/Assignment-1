#GETWORDS METHOD RETURNS THE WORDS IN A SENTENSE
def getwords(SENTENSE):
    return SENTENSE.split(" ")
SENTENSE="I am a teacher and I love to inspire and teach people"
WORDS=getwords(SENTENSE)
print("TOTAL WORDS:"+str(WORDS))
#USE A SET TO GET UNIQUE VALUES
UNIQUE_WORDS=set(getwords(SENTENSE))
print("UNIQUE WORDS : "+str(UNIQUE_WORDS))
print("COUNT:"+str(len(UNIQUE_WORDS)))