while(True):
    try:
        n = list(map(int, input('Введите целое положительное число n в котором найдем самое большое число')))
    except:
        print('Вы ввели не число. Попробуйте еще раз')
        continue
    break
counter = 1
result = 0
while (len(n) >= counter):
    if n[counter - 1] > result:
        result = n[counter - 1]
    counter += 1
print(f' Самое большое число {result}')

