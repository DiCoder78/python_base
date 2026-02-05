def calculate_tax(price):
    return price * 0.2

print(calculate_tax(2))

try:
    number = int(input())
except ValueError:
    print("Это не число")