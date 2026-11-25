# Mission 5: Number Systems and Data
# Beginner-friendly decimal to binary and hexadecimal converter

def main():
    print("=== Decimal Number Converter ===")
    
    # 1. Ask the user for a decimal integer
    user_input = input("Enter a decimal integer: ")
    
    # 2. Convert the input string into an integer
    decimal_number = int(user_input)
    
    # 3. Convert the integer to binary
    binary_representation = bin(decimal_number)
    
    # 4. Convert the integer to hexadecimal
    hex_representation = hex(decimal_number)
    
    # 5. Display the converted results
    print("--- Conversion Results ---")
    print("Decimal value:    ", decimal_number)
    print("Binary value:     ", binary_representation)
    print("Hexadecimal value:", hex_representation)

if __name__ == "__main__":
    main()
