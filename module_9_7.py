def is_prime(func):
    def wrapper(*num:int):
        result = func(*num)
        for div in range(2, result):
            if result % div == 0:
                print("Составное")
        else:
            print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
