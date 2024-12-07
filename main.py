def find_intersection(sets):
    if not sets:             #если нету множеств -> возвращает пустое множество
        return set()
    inter = set.intersection(*sets)  #кладёт в переменную inter пересечение всех множеств из sets
    return inter


#ввод количества множеств
n = int(input("Введите количество множеств: "))
sets = []
for i in range(n):
    elements = input(f"Введите элементы множества {i + 1} через пробел: ").split(' ')#кладёт в переменную elements массив переменных
    sets.append(set(elements))  #добавляет в массив множество elements

inter = find_intersection(sets)   # обращение к функции, в переменную inter кладётся пересечение


#вывод + проверка на ошибки ввода
if n <=0:
    print('Неправильно введено значение')
elif not inter:
    print("Пересечение множеств: пустое множество")
else:
    print("Пересечение множеств:", inter)