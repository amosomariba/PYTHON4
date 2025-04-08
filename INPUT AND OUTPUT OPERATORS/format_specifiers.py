price = 200.456789
quantity = 50

# Format specifier {value:.2f}
print(f"You bought {quantity}kgs of sugar @{price :.2f} Ksh.")

# Example 2

price1 = 234.6785
price2 = 7347.00345
price3 = -4562.000047
price4 = 21.43

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")
print(f"Price 4 is ${price4:.3f}")

# Example 3
price5 = 2340000.6785
price6 = 734700.00345
price7 = -456200.000047
price8 = 210000.43

print(f"Price 5 is ${price5:03}")  # You can add + ,
print(f"Price 6 is ${price6:03}")
print(f"Price 7 is ${price7:,}")
print(f"Price 8 is ${price8:+,}")
