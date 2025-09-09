import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    filename = sys.argv[1]
    
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")
    
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        table = tabulate(data, headers="firstrow", tablefmt="grid")
        print(table)
        
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
