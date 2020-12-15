p = float(input("What is your initial investment?"))
r = float(input("What is the annual nominal interest rate in decimals?"))
n = int(input("What is the number of times the interest is compounded per year?"))
t = int(input("After how many years would you like to know the value of your investment?"))

final_amount = p * (1 + r / n) ** (n * t)
print(final_amount)

