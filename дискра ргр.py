def main():
    n = int(input("Введите количество множеств: "))
    sets = [set(input(f"Введите элементы множества {i + 1} через пробел: ").split()) for i in range(n)]
    
    intersection = set.intersection(*sets)
    
    print("Пересечение множеств:", intersection)

if __name__ == "__main__":
    main()