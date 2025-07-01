# Task2_Calculator: Advanced Calculator with Full Expression Evaluation

def main():
    print("🔢 Advanced Calculator | Type 'exit' to quit\n")

    while True:
        try:
            expr = input("Enter expression (e.g. 8+2*3 or (5+3)/2): ")

            if expr.lower() == "exit":
                print("Goodbye! 👋")
                break

            # Evaluate the full expression safely
            result = eval(expr)
            print(f"✅ Result: {result}\n")

        except ZeroDivisionError:
            print("❌ Cannot divide by zero.\n")
        except Exception:
            print("⚠️ Invalid expression. Please try again.\n")

if __name__ == '__main__':
    main()
