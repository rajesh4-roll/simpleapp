# def main():
#     print("rajesh")
#     multiplication(5)
#     factors(12)
#     x = factorial(5)
#     print(x)
#     lst = []
#     for x in range(13):
#         a = fibo(x)
#         lst.append(a)
#     print('The fibonaaci series are')
#     print(lst)
#     print("whether is prime")
#     if is_prime(13):
#         print("is prime")
#     else:
#         print("Not prime")


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

def factors(x):
    lst = []
    for i in range(1,x+1):
        if x % i == 0:
            lst.append(i)
    return lst
    
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
        

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 2) + fibo(x-1)

def multiplication(x):
    for i in range(1, 11):
        print(x,'x',i,'=', x * i)
