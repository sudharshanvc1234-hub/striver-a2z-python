n = int(input())
t = tuple(map(int, input().split()))

x = 0x345678
mult = 1000003
z = len(t)

for item in t:
    x = (x ^ hash(item)) * mult
    z -= 1
    mult += 82520 + z + z

x += 97531
x = x & ((1 << 64) - 1)

if x >= (1 << 63):
    x -= (1 << 64)

if x == -1:
    x = -2

print(x)