successful = True
finalAttempt = 5

for number in range(1, finalAttempt+1):
    print("Attempt: ", number, number * ".")
    if (successful):
        print("Attempt Successfull")
        break
else:
    print(
        f"Attempted {finalAttempt} times and failed to send the email. Sorry!!!"
    )
