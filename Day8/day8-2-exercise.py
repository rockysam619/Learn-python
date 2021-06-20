#How many cans to paint the wall? when 1 can covers 5 sqm.
import math
def paint(height, width, cover):
    area = height*width
    cans = math.ceil(area/cover)
    return cans

height = int(input("What is height of the wall in metres?: "))
width = int(input("What is width of the wall in metres?: "))
cans = paint(height, width, 5)

print(f"No of cans needed by you are {cans}")