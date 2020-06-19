# List
fruits = ["Apple", "Banana", "Grapes", "Orange"]
"""
print(fruits)
print(fruits[1])
print(fruits[-1])
print(len(fruits))

for x in fruits:
    print(x)
"""
z = 1
while z <= len(fruits):
    for y in fruits[len(fruits) - z]:
        print(y)
    print("-----")
    z += 1
print("Total Fruits:" + str(len(fruits)))



