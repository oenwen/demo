def create_cookbook():
    cookbook = dict()
    dish_list = list()
    ingredient_list = list()
    with open('recipes.TXT', encoding='utf8') as recipes:
        while True:
            dish = recipes.readline().strip()
            if not dish:
                break
            dish_list.append(dish)
            quantity = int(recipes.readline().strip())
            for i in range(quantity):
                ingredient_list.append(recipes.readline().strip())
            recipes.readline().strip()  # чтение пустой строки

            # превращение списка строк ingredient_list в список словарей
            book_values = list()
            for ingredient in ingredient_list:
                ingredient_name = ingredient.split(' | ')[0]
                ingredient_quantity = int(ingredient.split(' | ')[1])
                ingredient_unit = ingredient.split(' | ')[2]
                ingredient_dict = {'ingredient_name': ingredient_name,
                                   'quantity': ingredient_quantity,
                                   'measure': ingredient_unit}
                book_values.append(ingredient_dict)
            cookbook[dish] = book_values
            ingredient_list = list()
        # from pprint import pprint
        # pprint(cookbook)
    return cookbook

def get_shop_list(dishes):
    new_cookbook = create_cookbook()
    print(f'\nМеню: {list(new_cookbook.keys())}')
    order = input('Ваш заказ: введите названия блюд через запятую ')
    order_list = (order.split(sep=','))
    for dish in order_list:
        if dish.strip().capitalize() in list(new_cookbook.keys()):
            print(f'Блюдо "{dish.strip().capitalize()}" добавлено в заказ')
            dishes.append(dish.strip().capitalize()) # создан список блюд dishes
        else:
            print(f'Сожалеем, блюда "{dish.strip().capitalize()}" нет в нашем меню или Вы допустили опечатку')

    while True:
        try:
            person_count = int(input('Введите количество персон '))
            break
        except ValueError:
            print('Введите число')

    ingr_dict = dict()
    help_dict = dict()

    counter = 0
    for i, dish in enumerate(dishes):
        if dishes.count(dish) > 1:
            dishes[i] = dishes[i] + str(counter)
            counter += 1

    for key, value in new_cookbook.items():
        for dish in dishes:
            if key in dish:
                for i in range(len(value)):
                    ingredient = value[i]['ingredient_name']
                    if not ingredient in ingr_dict.keys():
                        quantity_dict = {'measure':value[i]['measure'],
                                         'quantity':(value[i]['quantity'] * person_count)}
                        ingr_dict[ingredient] = quantity_dict
                        help_dict[ingredient] = value[i]['quantity'] * person_count
                    else:
                        quantity_dict = {'measure': value[i]['measure'],
                                         'quantity': ((value[i]['quantity'] * person_count) + help_dict[ingredient])}
                        ingr_dict[ingredient] = quantity_dict
                        help_dict[ingredient] = quantity_dict['quantity']

    from pprint import pprint
    pprint(ingr_dict)

def main():
    create_cookbook()
    get_shop_list(dishes=[])
main()