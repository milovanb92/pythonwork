motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

#motocycles[0] = 'ducati'
#print(motocycles)

# add item to beginning of the list using append
motocycles.append('ducati')
print(motocycles)

# add item to list on position with insert
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles.insert(0, 'ducati')
print(motocycles)

# delete item from list using del
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)

# manipulate items with pop
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

popped_motociycle = motocycles.pop()
print(motocycles)
print(popped_motociycle)

# remove item by value with remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motocycles)