def int_func(string):
    return string.title()

result_text = ''
text = list(input("Введите слова через пробел которые надо преобразовать в верхний регистр ").split())
for n in range(len(text)):
    result_text = f'{result_text} {int_func(text[n])}'
print(result_text)
