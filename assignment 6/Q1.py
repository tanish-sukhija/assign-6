def perfect():
    num = int(input("Enter a number: "))
    divisors = [i for i in range(1, num) if num % i == 0]
    if sum(divisors) == num:
        print(num," is a perfect number.")
    else:
        print(num," is not a perfect number.")

perfect()
