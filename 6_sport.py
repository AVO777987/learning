a = 2
b = 5
days = 1

while(True):
    if a >= b:
        print(f'{days}-й день: {round(a, 2)}')
        break
    else:
        print(f'{days}-й день: {round(a, 2)}')
        a = a + a*0.1
        days += 1
        continue
print(f'на {days}-й день спортсмен достиг результата — не менее {b} км.')
