n = int(input())
arr = list(map(int, input().split()))

maximum = max(arr)

while maximum in arr:
    arr.remove(maximum)

print(max(arr))
