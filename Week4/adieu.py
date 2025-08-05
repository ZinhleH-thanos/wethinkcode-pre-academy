import inflect

def main():
    p = inflect.engine()
    names = []
    
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")

if __name__ == "__main__":
    main()
