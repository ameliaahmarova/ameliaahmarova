
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

def main():
    """Main calculator function"""
    history = []
    
    while True:
        show_menu()
        choice = input("\nChoose operation (0-6): ").strip()
        print(f"DEBUG: You entered: '{choice}'")  # Отладочная печать
        
        if choice == '0':
            print("Goodbye!")
            break
            
        elif choice == '1':  # Addition
            print("DEBUG: Entering addition...")  # Отладочная печать
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = a + b
                history.append(f"{a} + {b} = {result}")
                print(f"Result: {result}")
            except ValueError:
                print("Error! Please enter valid numbers.")
                
        elif choice == '2':  # Subtraction
            print("DEBUG: Entering subtraction...")  # Отладочная печать
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = a - b
                history.append(f"{a} - {b} = {result}")
                print(f"Result: {result}")
            except ValueError:
                print("Error! Please enter valid numbers.")
                
        elif choice == '3':  # Multiplication
            print("DEBUG: Entering multiplication...")  # Отладочная печать
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = a * b
                history.append(f"{a} * {b} = {result}")
                print(f"Result: {result}")
            except ValueError:
                print("Error! Please enter valid numbers.")
                
        elif choice == '4':  # Division
            print("DEBUG: Entering division...")  # Отладочная печать
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if b == 0:
                    print("Error: division by zero!")
                else:
                    result = a / b
                    history.append(f"{a} / {b} = {result}")
                    print(f"Result: {result}")
            except ValueError:
                print("Error! Please enter valid numbers.")
                
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
