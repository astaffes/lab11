#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_route():
    """
    Запросить данные о маршруте
    """
    start_destination = input("Введите начальный пункт назначения ")
    end_destination = input("Введите конечный пункт назначения ")
    route_num = input("Введите номер маршрута ")
    return {
        'start_destination': start_destination,
        'end_destination': end_destination,
        'route_num': route_num,
    }


def display_routes(routes):
    """
     Отобразить список машрутов
    """
    if routes:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "No",
                "Начальный пункт",
                "Конечный пункт",
                "Номер машрута"
            )
        )
        print(line)

        for idx, route in enumerate(routes, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    route.get('start_destination', ''),
                    route.get('end_destination', ''),
                    route.get('route_num', 0)
                )
            )
        print(line)

    else:
        print("Список машрутов пуст")


def select_routes(routes, route_num):
    """
    Выбрать машруты с заданным номером
    """
    count = 0
    res = []
    for route in routes:
        if route.get('route_num') == route_num:
            count += 1
            res.append(route)
    if count == 0:
        print("Маршруты не найдены")

    return res


def main():
    """
    Главная функция программы
    """
    routes = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            route = get_route()
            routes.append(route)
            if len(routes) > 1:
                routes.sort(
                    key=lambda item:
                    item.get('route_num', ''))

        elif command == 'list':
            display_routes(routes)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            route_num = (parts[1].capitalize())
            print(f"Для маршрута номер {route_num}:")
            selected = select_routes(routes, route_num)
            display_routes(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список всех маршрутов;")
            print("select <номер маршрута> - запросить маршруты с указанным "
                  "номером;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
