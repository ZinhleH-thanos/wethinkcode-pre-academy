import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                
                for row in reader:
                    name_parts = row['name'].split(', ')
                    if len(name_parts) == 2:
                        last_name = name_parts[0]
                        first_name = name_parts[1]
                        writer.writerow({
                            'first': first_name,
                            'last': last_name,
                            'house': row['house']
                        })
    
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
