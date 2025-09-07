# Functions
# Simple function for addition of two numbers
def add(a, b) -> str:
    print(f"{a} + {b} = {a + b}\n")

# Screen outputs
def prints() -> None:
    print("Student Name:\tOmair Abid Jaswal")
    print("Roll Number:\tPIAIC115285\n")
    
    add(2, 2)


# Minimal main program
def main() -> None:
    print("\nHello from packaged-app-module!\n")
    prints()

if __name__ == "__main__":
    main()
