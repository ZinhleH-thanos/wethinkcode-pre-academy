text = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u']
result = ""

for char in text:
    if char.lower() not in vowels:
        result += char

print("Output:", result)
