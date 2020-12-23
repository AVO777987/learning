try:
    with open('learning.txt', 'r', encoding='UTF-8-sig') as file:
        learning = {}
        for line in file:
            content = line.split()
            count = 1
            sum_value = 0
            for string in content:
                string = string.replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб).', '').replace('(лаб)', '').replace('—', '')
                if count == 1:
                    key = string
                    count += 1
                else:
                    if not string:
                        continue
                    value = int(string)
                    sum_value += value
            learning.update({key: sum_value})
    print(learning)
except IOError:
    print('Файла не существует!!!')