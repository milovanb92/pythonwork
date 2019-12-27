one_to_milion = []
for value in range(1, 1000001):
    one_to_milion.append(value)
print(f"{min(one_to_milion)}")
print(f"{max(one_to_milion)}")
print(f"{sum(one_to_milion)}")

for value in range(1, 21, 2):
    print(value)

for value in range(3, 30):
    print(value * 3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)