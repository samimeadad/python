data = [12, 64, 55, 23, 2, 8, 48, 36, 28, 7, 19, 16, 13, 15, 41]

print("Unsorted List: ", data)
data.sort()
print("Sorted List: ", data)

n = len(data)

print("Total items in the list: ", n)

i = int(n/2)
j = int(n/2)+1

print(i, j)

if (n % 2 == 1):
    median = data[i]
else:
    median = (data[i-1]+data[j-1])/2

print(median)
