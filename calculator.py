
"""
Simple Calculator with Basic Operations
"""

def show_menu():
    """Shows the calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Show history")
    print("6. Clear history")
    print("0. Exit")

def add(a, b):
    """Addition of two numbers"""
    return a + b

def subtract(a, b):
    """Subtraction of two numbers"""
    return a - b

def multiply(a, b):
    """Multiplication of two numbers"""
    return a * b

def divide(a, b):
    """Division of two numbers"""
    if b == 0:
        return "Error: division by zero!"
    return a / b

def get_number(prompt):
    """Gets a number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Please enter a number.")

def main():
    """Main calculator function"""
    history = []
    
    while True:
        show_menu()
        choice = input("\nChoose operation (0-6): ")
        
        if choice == '0':
            print("Goodbye!")
            break
            
        elif choice == '1':  # Addition
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = add(a, b)
            history.append(f"{a} + {b} = {result}")
            print(f"Result: {result}")
            
        elif choice == '2':  # Subtraction
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = subtract(a, b)
            history.append(f"{a} - {b} = {result}")
            print(f"Result: {result}")
            
        elif choice == '3':  # Multiplication
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = multiply(a, b)
            history.append(f"{a} * {b} = {result}")
            print(f"Result: {result}")
            
        elif choice == '4':  # Division
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = divide(a, b)
            history.append(f"{a} / {b} = {result}")
            print(f"Result: {result}")
            
        elif choice == '5':  # History
            if not history:
                print("History is empty")
            else:
                print("\nOperation history:")
                for i, operation in enumerate(history, 1):
                    print(f"{i}. {operation}")
                    
        elif choice == '6':  # Clear history
            history.clear()
            print("History cleared!")
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
