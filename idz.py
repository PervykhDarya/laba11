#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys

def get_product():
    name = input("Название продукта: ")
    shop = input("Название магазина: ")
    price = float(input("Стоимость: "))

    return {
        'name': name,
        'shop': shop,
        'price': price,
    }

def display_products(goods):
    if goods:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Продукт",
                "Магазин",
                "Цена"
            )
        )
        print(line)

        for idx, product in enumerate(goods, 1):
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('shop', ''),
                    product.get('price', 0)
            )
        )
        print(line)

def select_products(goods):
    tovar = input("Введите товар: ")
    result = []
    for tovar in goods:
        if tovar.get('name', ''):
            result.append(tovar)
    return result

def main():
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = get_product()

            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            display_products(products)

        elif command.startswith('select'):
            selected = select_products(products)
            display_products(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить запись;")
            print("list - вывести список;")
            print("select <продукт> - запросить информацию о продукте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("")

if __name__ == '__main__':
    main()