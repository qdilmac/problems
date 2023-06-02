# Problem 2: Prime Numbers
# Generate a list of prime numbers up to a given limit using list comprehension.

# Example:
# Input: limit = 20
# Output: [2, 3, 5, 7, 11, 13, 17, 19]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): # n sayısının karekökünü alıyoruz ve o sayıyı da dahil etmek için range bitişini +1 olarak alıyoruz.
        if n % i == 0:                  # buradaki mantık şu: 16'nın bölenlerini düşünelim. 16'nın bölenleri şunlardır: 1, 2, 4, 8, 16. 16'nın karekökü yaklaşık olarak 4'tür. 
            return False                # Bunu göz önünde bulundurarak, 16'nın bölenlerini bulmak için 1'den 4'e kadar olan sayıları kontrol etmek yeterlidir.   
    return True

def prime(limit):
    return [prime for prime in range(limit+1) if is_prime(prime)]

if __name__ == "__main__":
    limit = 55
    print(prime(limit))