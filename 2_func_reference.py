def reference(name, family, year, city, email, telephone):
    return f'{name}, {family}, {year}, {city}, {email}, {telephone}'


name = input("Введите имя пользователя")
family = input("Введите фамилию пользователя")
while True:
    try:
        year = int(input("Введите год рождения пользователя в формате XXXX"))
        if len(str(year)) != 4:
            print("Вы ввели год рождения в неправильном формате")
            continue
        else:
            break
    except:
        print("Вы ввели буквы вместо цифр")
        continue
city = input("Введите город проживания пользоватея")
while True:
    email = input("Введите email пользователя в формате example@mail.ru ")
    if '@' in list(email) or '.' in list(email):
        break
    else:
        print("Вы ввели email в неправильном формате")
        continue
while True:
    telephone = input("Введите телефон пользователя в формате 8(999)111-11-11")
    if \
            len(list(telephone)) != 15 \
            or list(telephone)[1] != '(' \
            or list(telephone)[5] != ')' \
            or list(telephone)[9] != '-' \
            or list(telephone)[12] != '-' :
        print("Вы ввели телефон в неправильном формате")
        continue
    else:
        check_tel = list(telephone)
        check_tel.remove('(')
        check_tel.remove(')')
        check_tel.remove('-')
        check_tel.remove('-')
        try:
            check_tel = list(map(int, check_tel))
        except:
            print("Вы ввели буквы вместо цифр")
            continue
        break

print(reference(name=name, family=family, year=year, city=city, email=email, telephone=telephone))

