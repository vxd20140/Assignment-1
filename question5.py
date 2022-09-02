#METHODS TO RETURN AREA AND CIRCUMFERENCE
def area(radius):
    return 3.14*radius*radius
def circumference(radius):
    return 2*3.14*radius
RADIUS=int(input("ENTER RADIUS:"))
area_of_circle=area(RADIUS)
print("AREA: "+str(area_of_circle))
circum_of_circle= circumference(RADIUS)
print("CIRCUMFERENCE: "+str(circum_of_circle))
