#CREATED A METHOD TO CONVERT THE WEIGHT
def converter(n, POUNDS):
    KILOGRAM = []
    for i in POUNDS:
        KILOGRAM.extend([i * 0.453592])
    print("WEIGHT IN KGS:", end="")
    return KILOGRAM
print("PROVIDE STUDENTS COUNT:", end="")
n = int(input())
#READ INPUTS
print("ENTER WEIGHTS:", end="")
POUNDS = list(map(int, input().split(" ")))
print(converter(n, POUNDS))