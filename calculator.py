
"""
Простой калькулятор с базовыми операциями
"""

def show_menu():
    """Показывает меню калькулятора"""
    print("\n=== Простой калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Показать историю")
    print("6. Очистить историю")
    print("0. Выход")

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def get_number(prompt):
    """Получает число от пользователя"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

def main():
    """Основная функция калькулятора"""
    history = []
    
    while True:
        show_menu()
        choice = input("\nВыберите операцию (0-6): ")
        
        if choice == '0':
            print("До свидания!")
            break
            
        elif choice == '1':  # Сложение
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = add(a, b)
            history.append(f"{a} + {b} = {result}")
            print(f"Результат: {result}")
            
        elif choice == '2':  # Вычитание
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = subtract(a, b)
            history.append(f"{a} - {b} = {result}")
            print(f"Результат: {result}")
            
        elif choice == '3':  # Умножение
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = multiply(a, b)
            history.append(f"{a} * {b} = {result}")
            print(f"Результат: {result}")
            
        elif choice == '4':  # Деление
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = divide(a, b)
            history.append(f"{a} / {b} = {result}")
            print(f"Результат: {result}")
            
        elif choice == '5':  # История
            if not history:
                print("История пуста")
            else:
                print("\nИстория операций:")
                for i, operation in enumerate(history, 1):
                    print(f"{i}. {operation}")
                    
        elif choice == '6':  # Очистка истории
            history.clear()
            print("История очищена!")
            
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
