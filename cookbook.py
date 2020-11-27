def read_cooking_book(recipes):
    with open(recipes, encoding='utf8') as f:
        while True:
            dish = f.readline().strip()
            cook_book[dish] = []

            for str in range(int(f.readline().strip())):
                item = f.readline().strip()
                item = item.split(sep=' | ')

                cook_book[dish].append({'ingredient_name': item[0], 'quantity': item[1], 'measure': item[2]})

            if f.readline() != '\n':
                return


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for item in cook_book[dish]:
            if shop_list.get(item['ingredient_name']) is None:
                shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                      'quantity': int(item['quantity']) * person_count}
            else:
                shop_list[item['ingredient_name']]['quantity'] += int(item['quantity']) * person_count

    return shop_list


cook_book = {}


def main():
    read_cooking_book('recipes.txt')
    print(get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 2))


if __name__ == '__main__':
    main()