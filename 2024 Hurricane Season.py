print("________________________")
print("2024 HURRICANE SEASON")
#to practice building and manipulating a dictionary

hurricanes = {"ALBERTO": "tropical",
              "BERYL": "5",
              "CHRIS": "tropical",
              "DEBBY": "1",
              "ERNESTO": "2",
              "FRANCINE": "2",
              "GORDON": "tropical",
              "HELENE": "4",
              "ISAAC": "2",
              "JOYCE": "tropical",
              "KIRK": "4",
              "LESLIE": "2",
              "MILTON": "5",
              "NADINE": "tropical",
              "OSCAR": "1",
              "PATTY": "tropical",
              "RAFAEL": "3",
              "SARA": "tropical"}

print("________________________")
keys = hurricanes.keys()
for key in hurricanes.keys():
    print(key)
print("________________________")


key = input("Enter the name of a 2024 hurricane to learn its strength: ").upper()
if hurricanes.get(key):
    value = hurricanes[key]
    print(f"{key} was a category {value} storm.")
else:
        print("That is not the name of a hurricane in the 2024 season.")




#values = hurricanes.values()
#for value in hurricanes.values():
    #print(value)

#for key, value in hurricanes.items():
    #print(f"{key} was a category {value} storm.")
