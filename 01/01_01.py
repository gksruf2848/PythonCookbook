p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, mon, day) = data
print(name, year, mon, day)


#문자열 언패킹
s = 'Hello'
a, b, c, d, e = s
print(a, d, e)


#특정 값을 무시하는 방법
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares, price)