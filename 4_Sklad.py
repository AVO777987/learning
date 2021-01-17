import json


class NoIdException(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    try:
        with open('base.txt', 'r', encoding='UTF-8') as file:
            product = json.loads(file.readline())
            storage = json.loads(file.readline())
            subdivision = json.loads(file.readline())
    except IOError:
        product = {}
        storage = {}
        subdivision = {}

    def create_new_product(self, name_product):
        if not name_product in self.storage:
            if name_product == '':
                return print('Название товара не может быть пустым')
            self.product[name_product] = []
            self.storage[name_product] = 0
            for key in self.subdivision:
                self.subdivision[key].setdefault(name_product, 0)
        else:
            return print('Такое наименование товара уже есть на складе')

    def create_new_characteristic(self):
        product_id = sklad.list_product()
        try:
            id = int(input('Для какого товара вы хотите добавить характеристику?\n'))
            if id > len(product_id) or id <= 0:
                raise NoIdException('Такого товара не существует')
        except ValueError:
            return print('Введите число')
        except NoIdException as error:
            return print(error)
        name_characteristic = input('Введите название характеристики\n')
        if name_characteristic == '':
            return print('Название характеристики не может быть пустым')
        if not name_characteristic in self.product[product_id[id]]:
            self.product[product_id[id]].append(name_characteristic)
        else:
            return print('Такая характеристика уже есть у данного товара')

    def add_product_in_storage(self):
        storage_id = sklad.list_storage()
        try:
            id = int(input('Какой тип товара вы хотите добавить на склад?\n'))
            if id > len(storage_id) or id <= 0:
                raise NoIdException('Такого товара не существует!!!')
            value = int(input('Сколько товаров надо добавить?\n'))
        except ValueError:
            return print('Введите число')
        except NoIdException as error:
            return print(error)
        self.storage[storage_id[id]] = self.storage[storage_id[id]] + value

    def create_new_subdivision(self, name_subdivision):
        if not name_subdivision in self.subdivision:
            if name_subdivision == '':
                return print('Название подразделения не может быть пустым')
            self.subdivision[name_subdivision] = {}
            for name_product in self.product:
                for key in self.subdivision:
                    self.subdivision[key].setdefault(name_product, 0)
        else:
            return print('Такое подразделение уже есть')

    def moving_storage_to_subdivision(self):
        storage_id = sklad.list_storage()
        try:
            id_prod = int(input('Какой товар вы хотите переместить в подразделение?\n'))
            if id_prod > len(storage_id) or id_prod <= 0:
                raise NoIdException('Такого подразделения не существует')
        except ValueError:
            return print('Вы ввели не число')
        except NoIdException as error:
            return print(error)
        subdivision_id = sklad.list_subdivision()
        try:
            id_sub = int(input('В какое подразделение вы хотите переместить товар?\n'))
            if id_sub > len(subdivision_id) or id_sub <= 0:
                raise NoIdException('Такого подразделения не существует')
            value = int(input('Какое кол-во товара вы хотите переместить?\n'))
        except ValueError:
            return print('Вы ввели не число')
        except NoIdException as error:
            return print(error)
        if self.storage[storage_id[id_prod]] < value:
            return print('Нехватает кол-во товара, добавте товар на склад либо измените значение')
        else:
            self.storage[storage_id[id_prod]] = self.storage[storage_id[id_prod]] - value
            for key in self.subdivision[subdivision_id[id_sub]]:
                if key == storage_id[id_prod]:
                    self.subdivision[subdivision_id[id_sub]][key] = self.subdivision[subdivision_id[id_sub]][key] + value

    def moving_subdivision_to_storage(self):
        subdivision_id = sklad.list_subdivision()
        try:
            id_sub = int(input('Из какого подразделения вы хотите переместить товар на склад?\n'))
            if id_sub > len(subdivision_id) or id_sub <= 0:
                raise NoIdException('Нет такого подразделения')
        except ValueError:
            return print('Вы ввели не число')
        except NoIdException as error:
            return print(error)
        print(f'В данном подразделении числиться: {self.subdivision[subdivision_id[id_sub]]}')
        storage_id = sklad.list_storage()
        try:
            id_prod = int(input('Какой товар вы хотите переместить на склад?\n'))
            if id_prod > len(storage_id) or id_prod <= 0:
                raise NoIdException('Нет такого товара в подразделении')
            value = int(input('Какое кол-во товара вы хотите переместить?\n'))
        except ValueError:
            return print('Вы ввели не число')
        except NoIdException as error:
            return print(error)
        for key in self.subdivision[subdivision_id[id_sub]]:
            if key == storage_id[id_prod]:
                if self.subdivision[subdivision_id[id_sub]][key] < value:
                    return print('Нехватает кол-во товара, добавте товар в подразделение либо измените значение')
                self.subdivision[subdivision_id[id_sub]][key] = self.subdivision[subdivision_id[id_sub]][key] - value
                self.storage[storage_id[id_prod]] = self.storage[storage_id[id_prod]] + value

    def show_product(self):
        return print(f'Всего наименования товаров с характеристиками {self.product}')

    def show_product_to_storage(self):
        return print(f'Всего товаров на складе {self.storage}')

    def show_product_to_subdivision(self):
        return print(f'Всего товаров в подразделениях {self.subdivision}')

    def list_product(self):
        id = 1
        product_id = {}
        for el in self.product:
            print(f'{id}.{el}')
            product_id[id] = el
            id += 1
        return product_id

    def list_storage(self):
        id = 1
        storage_id = {}
        print(f'Всего оборудования на складе: {self.storage}')
        for el in self.storage:
            print(f'{id}.{el}')
            storage_id[id] = el
            id += 1
        return storage_id

    def list_subdivision(self):
        id = 1
        subdivision_id = {}
        for el in self.subdivision:
            print(f'{id}.{el}')
            subdivision_id[id] = el
            id += 1
        return subdivision_id


sklad = Storage()
while True:
    print('1. Добавить новое наименование товара')
    print('2. Добавить характеристики к товару')
    print('3. Добавить товар на склад')
    print('4. Добавить подразделение')
    print('5. Передать товары со склада в подразделение и обратно')
    print('6. Посмотреть все наименования товаров с характеристиками')
    print('7. Посмотреть остатки на складе')
    print('8. Посмотреть остатки на подразделениях')
    print('9. Выход')
    menu_input = input('Введите то что хотите сделать\n')
    if menu_input == '1':
        name_product = input('Введите название товара\n')
        sklad.create_new_product(name_product)
    if menu_input == '2':
        sklad.create_new_characteristic()
    if menu_input == '3':
        sklad.add_product_in_storage()
    if menu_input == '4':
        name_subdivision = input('Введите название подразделения\n')
        sklad.create_new_subdivision(name_subdivision)
    if menu_input == '5':
        print('1. Переместить товары со склада в подразделение')
        print('2. Переместить товары из подразделения на склад')
        menu_input = input('Введите то что хотите сделать\n')
        if menu_input == '1':
            sklad.moving_storage_to_subdivision()
        if menu_input == '2':
            sklad.moving_subdivision_to_storage()
    if menu_input == '6':
        sklad.show_product()
    if menu_input == '7':
        sklad.show_product_to_storage()
    if menu_input == '8':
        sklad.show_product_to_subdivision()
    if menu_input == '9':
        with open('base.txt', 'w', encoding='UTF-8') as file:
            print(f'{json.dumps(sklad.product, ensure_ascii=False)}', file=file)
            print(f'{json.dumps(sklad.storage, ensure_ascii=False)}', file=file)
            print(f'{json.dumps(sklad.subdivision, ensure_ascii=False)}', file=file)
        break

