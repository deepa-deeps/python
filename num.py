def is_prime(n): 
     
    for i in range(2,(n/2)):
        if n % i == 0:
            return False  
    return True  

number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
