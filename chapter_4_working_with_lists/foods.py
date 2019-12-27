my_foods = ['pizza', 'falafel', 'carrot cake']
# define list friends_foods as a copy of my_foods list
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

for food in my_foods:
    print(food)
for food in friends_foods:
    print(food)