number = [2, 4, 6, 8, 10]


def mean(number):
    sum = 0
    for x in number:
        sum += x
    length = len(number)
    mean = sum/length
    return mean


myMean = mean(number)

print("mean= ", myMean)
