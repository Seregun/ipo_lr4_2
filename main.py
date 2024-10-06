numbers = input("Введите список чисел через запятую: ").split(',') # Ввод списка чисел
sqrt = [int(num)**2 for num in numbers] # Возведение чисел  в квадрат
print(sqrt) # Вывод чисел в квадрате
