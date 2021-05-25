from mathematics import * #multiplication, factorial, factors, fibo, is_prime

def green():
    print("1. Fibonaaci Series")
    print("2. Check Prime Number")
    print("3. Factors of a Number")
    print("4. Multiplication Table")
    print("5. Factorials of a Number")
    _input = int(input('Enter your choice: '))
    print()
    if _input == 1:
        lst = []
        num = int(input("Enter number: "))
        for x in range(13):
            a = fibo(x)
            lst.append(a)
        print('Fibonacci Series are: ')
        print(lst)
    elif _input == 2:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(num,'is prime number.')
        else:
            print(num,'is not prime number.')
    elif _input == 3:
        num = int(input("Enter number: "))
        lst = factors(num)
        print(lst)
    elif _input == 4:
        num = int(input("Enter number: "))
        multiplication(num)
    elif _input == 5:
        num = int(input("Enter number: "))
        print(factorial(num))
    else:
        print('Invalid Choice !!!')




# if __name__ == '__main__':
#     main()