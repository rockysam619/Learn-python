# def add_numbers(x, y):
#     return x + y


# print("Enter first integer")
# x = int(input())
# print("Enter second integer")
# y = int(input())


# print(add_numbers(x, y))

# def factorial(N):
#     fact = 1
#     while N>1:
#             fact = fact*(N)
#             N-=1
#     return fact

# print(factorial(5))

# my_list = [1, 2, 3]
# print("Given list: %s" %my_list)

# data = ("Robin", 10, "chocolates")
# format_string = "Hello %s. You are currently left with %d %s."
# print(format_string %data)


# print(any(r.isalnum() for r in S))
# print(any(r.isalpha() for r in S))
# print(any(r.isdigit() for r in S))
# print(any(r.islower() for r in S))
# print(any(r.isupper() for r in S))

# tuple1 = ["one"]
# print(type(tuple1))

# def main():
#     tuple1 = tuple(("one", "two", "three"))
#     tuple2 = tuple(("1", "2", "3"))
    
#     # change value at index 0 of both tuple to string "number"
#     # Your code goes here
#     tuple1 = list(tuple1)
#     tuple2 = list(tuple2)
    
#     tuple1[0] = "number"
#     tuple2[0] = "number"
    
#     tuple1 = tuple(tuple1)
#     tuple2 = tuple(tuple2)

#     print(tuple1)
#     print(tuple2)
    
#     return 0

# main()

# import itertools
# cnt = 0
# for i in itertools.count(1000, 500):
#     if cnt == 1000:
#         break
#     else:
#         print(i, )
#         cnt+=1

# cnt = 0
# for i in itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     if cnt == 26:
#         break
#     else:
#         print (i, )
#         cnt+=1

# print(list(itertools.repeat(4, 1000)))

from itertools import permutations
putin = list(input().split())
putin[0] = list(putin[0])
putout = list()
for i in list(permutations(putin[0], 2)):
    putout.append("".join(i))

putout.sort()
for i in putout:
    print(i)

