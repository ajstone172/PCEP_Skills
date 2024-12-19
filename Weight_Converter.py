#Weight Converter

weight = float(input("Enter a weight: "))
unit = input("Kilograms or Pounds? (K or L) ")

if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight / 2.205
else:
    print(f"{unit} is not valid.")

print(f"Your weight is {weight} {unit}.")


