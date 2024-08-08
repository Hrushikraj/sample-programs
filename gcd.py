def gcd(m, n):
    m_multiples = []
    n_multiples = []
    for i in range(1, m+1):
        if m%i == 0:
            m_multiples.append(i)
    for i in range(1, n+1):
        if n%i == 0:
            n_multiples.append(i)
    
    for i in range (0, len(m_multiples)):
        for j in range(0, len(n_multiples)):
            if m_multiples[i] == n_multiples[j]:
                gcd = m_multiples[i]
    return gcd

print(gcd(8,12))
print(gcd(18,25))