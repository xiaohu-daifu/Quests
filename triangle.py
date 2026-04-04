import sys

triangle = input("Enter a character: ")
try:
    limit = int(input("Enter an integer greater than 1 and don't exceed 10: "))
except ValueError:
    print("Oops! Looks lke you skipped a lesson in kindergarten. Enter length as an INTEGER to get a triangle.")
    sys.exit()

def equi_triangle(tri: str, limit:int):
    if len(tri) > 1:
        return("Dude I said enter a character, not an essay")
    if limit <2 or limit > 10:
        return("Do you read? I said greater than 1 and don't exceed 10!")
    
    fow = range(0, limit+1)
    back = range(limit+1, 1, -1)
  
    for f, b in zip(fow, back):
        print(" "*(b) + tri*f*2 +tri)
    return "\nGood stuff, bro."

print(equi_triangle(triangle, limit))