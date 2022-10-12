from dis import dis
from pprint import pprint


def create_cook_book(path):
    global cook_book
    cook_book = {}

    with open(path, 'rt', encoding='utf-8') as file:
        for l in file:
            dish = l.strip()
            ingr = []
            for i in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingr.append({'ingredient_name': ingredient_name,
                            'quantity': quantity,
                             'measure': measure})
            file.readline()
            cook_book[dish] = ingr
    return cook_book


def get_shop_list_by_dishes(person_count=1, *dishes):
    ingredients = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in ingredients:
                ingredients[ingr['ingredient_name']
                            ]['quantity'] += (int(ingr['quantity']) * person_count)
                continue
            ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'],
                                                    'quantity': int(ingr['quantity']) * person_count}
    return ingredients


if __name__ == '__main__':
    pprint(create_cook_book('recipes.txt'))
    pprint(get_shop_list_by_dishes(2, 'Фахитос', 'Омлет'))
