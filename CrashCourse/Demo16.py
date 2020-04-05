# P(k,p)=(1-p)**(k-1)*p
def math(k, p):
    return (1 - p) ** (k - 1) * p


def accum(k, p):
    res = 0
    for value in range(1, k+1):
        res = res + math(value, p)
    return res


def birthday_accum(num):
    res = 1
    for value in range(1, num):
        res = res * (365 - value) / 365
    return res


print(f'40次不中的概率:{math(40,1/200)}')
print(f'39次累计概率为:{accum(39,1/200)}')

print(f'70人中生日不同的概率:{birthday_accum(20)}')
