from interface import init_gui, init_canvas, init_input


def intersection():

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
        return 'Неправильно введено значение'
    elif not inter:
        return "Пересечение множеств: пустое множество"
    else:
        return f"Пересечение множеств: {inter}"
    

if __name__ == '__main__':
    root = init_gui()
    canvas = init_canvas(root)
    init_input(canvas)
    root.mainloop()