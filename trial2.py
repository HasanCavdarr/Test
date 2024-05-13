def sum_of_list(numbers):
    if not numbers:  
        return 0     
    return sum(numbers)
numbers = [15, 25, 35, 45, 55]


result = sum_of_list(numbers)
print("sum of the list:", result)

def main(a):
    if a % 2 == 0:
        print("your number is even")
    else: 
        print("your number is odd")
number3 = int(input("enter a number"))
answer = main(number3)
