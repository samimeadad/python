# Beecrowd Problem-1005

a = float(input("Grade of student A: "))
b = float(input("Grade of student B: "))

weightOfA = 3.5
weightOfB = 7.5

totalWeight = weightOfA+weightOfB

media = (a*weightOfA + b*weightOfB)/(totalWeight)

print("Media = {:.5f}".format(media))
