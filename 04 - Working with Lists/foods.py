my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# demonstrate two seperate lists after copying a list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods: print(food)

print("\nMy Friend's favorite foods are:")
for food in friend_foods: print(food)
