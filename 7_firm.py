import json
try:
    with open('firm.txt', 'r', encoding='UTF-8-sig') as file:
        firm_list = []
        firm_dict = {}
        average_profit = 0
        firms_profit = 0
        for line in file:
            profit = 0
            firm = line.split()
            if int(firm[2]) >= int(firm[3]):
                profit = int(firm[2]) - int(firm[3])
                firms_profit += 1
                firm_dict.update({firm[0]: profit})
            else:
                lesion = int(firm[2]) - int(firm[3])
                firm_dict.update({firm[0]: lesion})
            average_profit += profit
        average_profit = average_profit/firms_profit
    firm_list = [firm_dict, {'average_profit': round(average_profit, 2)}]
    with open("firm.json", "w", encoding='UTF-8-sig') as file:
        json.dump(firm_list, file, ensure_ascii=False)
except IOError:
    print('Файла не существует!!!')
