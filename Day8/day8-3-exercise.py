#Prime number function

def prime_number(num):
    
    if num == 2 or num == 3:
        print("It is a prime.")
        return
    
    for n in range(2, num-1):
        if num%n == 0:
            print("Not a prime.")
            break
        else:
            print("It is a prime")
            break

num = int(input("Please enter a number to check if it is prime: "))
prime_number(num)
