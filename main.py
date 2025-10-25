def PrimeList(N):
    primes = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        is_prime = True
        # 判断num是否为质数（只需检查到num的平方根）
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))  # 转为字符串，方便后续拼接
    # 用空格连接列表元素，自动避免末尾空格
    return ' '.join(primes)

