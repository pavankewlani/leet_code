class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        is_prime = bytearray([1]) * n
        is_prime[0] = is_prime[1] = 0
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                count = (n - 1 - i * i) // i + 1
                if count > 0:
                    is_prime[i * i : n : i] = b'\x00' * count
                    
        return sum(is_prime)