# String format

string_format = "{0:2} {2:3} {3:4} {1:6.2f}"

for i in range(11):
    print(string_format.format(i, i ** .5, i ** 2, i ** 3))
