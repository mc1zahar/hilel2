while True:
    x = float(input("Введіть первше число : "))
    y = float(input('Введіть друге число : '))
    z = input('Введіть матиматичну опепацію одну з "+, -, /, *" : ')
    if z == '/' and y == 0:
        print('На ноль ділити не можна ')
        continue
    elif z == '+':
        print('Результат =', round(x+y, 3))
    elif z == '-':
        print('Результат =', round(x-y, 3))
    elif z == '*':
        print('Результат =', round(x*y, 3))
    elif z == '/':
        print('Результат =', round(x/y, 3))
    else:
        print('Ви ввели не вірне значеня ')
        continue
    finish = input('Якщо , ви бажаєте продовжити введить "continue", якщо ні , то введіть "quit" : ')
    if finish.lower() == "quit":
        break
    else:
        continue
