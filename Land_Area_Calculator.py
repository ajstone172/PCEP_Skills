#calculating the area of a rectangular plot of land

unit = input("Measured in units of ha or ac? ")
l = int(input("Length of the plot: "))
w = int(input("Width of the plot: "))
area = l * w
print()
print(f"The area of the plot is {area} {unit}.")
