def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
        #   not a prime number
         is_prime = False
    if is_prime:
         print("It's a prime number .")
    else:
         print("It's not a prime number")

while True:
    guess = int(input("Enter a number: "))
    prime_checker(number=guess)


