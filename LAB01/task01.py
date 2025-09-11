def main():
    numbers = []
    count = 0
    
    print("Введите 10 целых чисел:")
    
    while count < 10:
        try:
            # Получаем ввод от пользователя
            user_input = input(f"Число {count + 1}: ")
            
            # Пытаемся преобразовать в целое число
            number = int(user_input)
            
            # Добавляем число в список
            numbers.append(number)
            count += 1
            
        except ValueError:
            # Если введено не число, выводим сообщение об ошибке
            print("Ошибка! Введите целое число.")
    
    # Вычисляем результаты
    if numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        sum_numbers = sum(numbers)
        
        # Выводим результаты
        print("\nРезультаты:")
        print(f"Список чисел: {numbers}")
        print(f"Минимальное число: {min_number}")
        print(f"Максимальное число: {max_number}")
        print(f"Сумма всех чисел: {sum_numbers}")
    else:
        print("Список пуст.")

# Запускаем программу
if __name__ == "__main__":
    main()
