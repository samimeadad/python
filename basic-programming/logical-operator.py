# and
# or
# not

highIncome = False
goodCredit = True
student = False

message = "Eligible" if (highIncome or goodCredit) and (
    not student) else "Not Eligible"

print(message)
