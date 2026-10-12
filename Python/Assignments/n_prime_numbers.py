n = int(input("Enter N: "))

count = 0
num = 2
total_sum = 0

while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        total_sum = total_sum + num
        count = count + 1
        
    num = num + 1

print("Sum of prime numbers:", total_sum)