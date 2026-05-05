import datetime

# Function to perform basic calculations

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"

# Command menu for user interaction

def command_menu():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", calculator(a, b, 'add'))
        elif choice == '2':
            print("Result:", calculator(a, b, 'subtract'))
        elif choice == '3':
            print("Result:", calculator(a, b, 'multiply'))
        elif choice == '4':
            print("Result:", calculator(a, b, 'divide'))
    else:
        print("Invalid choice")

# Current date and time function

def current_time():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Main function to execute the program
if __name__ == '__main__':
    print(f"Current Date and Time (UTC): {current_time()}")
    command_menu()
