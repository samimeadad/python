x = [10, 15, 22, 25, 30, 33, 43, 46]
odd = 0
even = 0
divByFive = 0

for i in range(0, len(x)):
    if (x[i] % 5 == 0):
        divByFive += 1
    if (x[i] % 2 == 1):
        odd += 1
    else:
        even += 1

print("Total Odd Number Count= ", odd)
print("Total Even Number Count= ", even)
print("Number divisible by 5: ", divByFive)
