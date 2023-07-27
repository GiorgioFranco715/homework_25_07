#if __name__ == "__main__":
    # print('Zdorov')

    # Завдання 1
    # Вивести на екран усі прості числа в діапазоні, зазначеному користувачем.
    # Число називається простим, якщо воно ділиться без залишку тільки на себе та на одиницю.
    # Наприклад, три — це просте число, а чотири — ні.

    # Дані від користувача:
    # number_one = int(input('Введіть нижнє граничне число діапазону:'))
    # number_two = int(input('Введіть верхнє граничне число діапазону:'))

    #Розв'язок задачі:
    # for item in range(number_one,number_two):
    #     if (item %2 != 0) and (item %3 != 0) and (item %5 != 0) and (item %7 != 0) or (item == 1) or (item == 2) or (item == 3) or (item == 5) or (item == 7):
    #         print(item)


    #Завдання 2
    #Вивести на екран таблицю множення для всіх чисел від 1 до 10. Наприклад:
    # 1 * 1 = 1
    # 1 * 2 = 2...
    # 1 * 10 = 10
    # ......................................
    # 10 * 1 = 10
    # 10 * 2 = 20...
    # 10 * 10 = 100

    #Розв'язок задачі
    # for item in range(1,11):
    #     multiplication_by_one = (f"{item}*1={item * 1}")
    #     print(multiplication_by_one)
    # for item in range(1,11):
    #     multiplication_by_two = (f"{item}*2={item * 2}")
    #     print(multiplication_by_two)
    # for item in range(1,11):
    #     multiplication_by_three = (f"{item}*3={item * 3}")
    #     print(multiplication_by_three)
    # for item in range(1,11):
    #     multiplication_by_four = (f"{item}*4={item * 4}")
    #     print(multiplication_by_four)
    # for item in range(1,11):
    #     multiplication_by_five = (f"{item}*5={item * 5}")
    #     print(multiplication_by_five)
    # for item in range(1,11):
    #     multiplication_by_six = (f"{item}*6={item * 6}")
    #     print(multiplication_by_six)
    # for item in range(1,11):
    #     multiplication_by_seven = (f"{item}*7={item * 7}")
    #     print(multiplication_by_seven)
    # for item in range(1,11):
    #     multiplication_by_eight = (f"{item}*8={item * 8}")
    #     print(multiplication_by_eight)
    # for item in range(1,11):
    #     multiplication_by_nine = (f"{item}*9={item * 9}")
    #     print(multiplication_by_nine)
    # for item in range(1,11):
    #     multiplication_by_ten = (f"{item}*10={item * 10}")
    #     print(multiplication_by_ten)


    # Завдання 3
    # Вивести на екран таблицю множення в діапазоні, зазначеному користувачем.
    # Наприклад, якщо користувач вказав 3 і 5, таблиця може виглядати так:
    # 3 * 1 = 3
    # 3 * 2 = 6
    # 3 * 3 = 9...
    # 3 * 10 = 30
    # ........................................
    # 5 * 1 = 5
    # 5 * 2 = 10
    # 5 * 3 = 15...
    # 5 * 10 = 50


    # Дані від користувача:
    # number_one = int(input('Введіть нижнє граничне число діапазону:'))
    # number_two = int(input('Введіть верхнє граничне число діапазону:'))

    # Розв'язок задачі
    # for item in range(number_one, number_two + 1):
    #     for number in range(1,11):
    #         multiplication = (f"{item}*{number}={item * number}")
    #         print(multiplication)