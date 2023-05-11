x = input('Ввеліть 3-х значне число :')

sum = int(x[0])+int(x[1])+int(x[2])
print(sum)
a = int(x)
b = (a % 1000) // 100
c = (a % 100) // 10
d = a % 10
sum_2 = b+c+d
print(sum_2)