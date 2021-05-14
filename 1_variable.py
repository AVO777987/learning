name = 'Андрей'
age = 33
height = (193, 50)
location = {'country': 'Россия', 'city': 'Москва'}
fruit = ['яблоки', 'мандарины', 'груши']

print(
    f'Добрый день, я хочу с Вами познакомиться. Сначала расскажу не много о себе. Меня зовут {name}, мне {age} года, мой рост {height[0]} метра и {height[1]} сантиметров. '
    f'Сам я из {location["country"]} из города {location["city"]}. Из фруктов я люблю {fruit[0]}, {fruit[1]} и {fruit[2]}')
print('')
name = input('Теперь не могли бы Вы ответить на несколько вопросов о Вас. Как вас зовут?')
while(True):
    try:
        age = int(input('Сколько Вам лет?'))
    except:
        print('Вы ввели не число. Введите еще раз')
        continue
    break
while(True):
    try:
        meter = int(input('Введите свой рост в метрах '))
    except:
        print('Вы ввели не число. Введите еще раз')
        continue
    break
while(True):
    try:
        centimeter = int(input('А сколько еще сантиметров?'))
    except:
        print('Вы ввели не число. Введите еще раз')
        continue
    break
country = input('Введите в какой стране вы живете? ')
city = input('А в каком городе? ')
location = {'country': country, 'city': city}
fruit = input('Введите через пробел 3 фрукта которые вы любите').split()
print(
    f'Получаеться что Вы {name}, Вам {age} года, ваш рост {height[0]} метра и {height[1]} сантиметров. '
    f'Сами Вы из {location["country"]} из города {location["city"]}. Из фруктов Вы любите {fruit[0]}, {fruit[1]} и {fruit[2]}')
