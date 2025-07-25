def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    
    numbers = [c for c in s if c.isdigit()]
    if numbers:
        if numbers[0] == '0':
            return False
        if not s[-len(numbers):].isdigit():
            return False
    return True

main()
