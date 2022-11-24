import math
'''
You are painting a wall.
Paint instructions direct:
- 1 can of paint can cover 5 square meters of wall

Calculate how many cans of paint to buy

'''
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)