import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def ask_question(x, y):
    correct = x + y
    for tries in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == correct:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{x} + {y} = {correct}")
    return False

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_question(x, y):
            score += 1

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
