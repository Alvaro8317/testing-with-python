import decimal

# INT

first_number: int = 10

second_number = 20

print("Sum of integers: ", first_number + second_number)

# Float

first_float = 10.1

second_float = 20.3

print(f"Sum of floats: {first_float + second_float}")

# Decimal

my_first_decimal = decimal.Decimal("10.0000000001")
my_second_decimal = decimal.Decimal("20.0000000001")

print(f"Sum of decimals: {my_first_decimal + my_second_decimal}")

# Integer + float

print(f"Sum of int and float: {first_number + first_float}")

# Integer + decimal

print(f"Sum of int and decimal: {first_number + my_second_decimal}")

# Float + decimal

print(f"Sum of float and decimal: {decimal.Decimal(str(second_float)) + my_second_decimal}")
