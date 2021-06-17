# Average height using for loops
heights_list = (input("Enter heights separated by space:\n")).split(" ")
height_sum = 0
count = 0

for height in heights_list:
    height_sum = height_sum + int(height)
    count+=1

average_height = round(height_sum/count)
print(f"Average height of the group is {average_height}")
