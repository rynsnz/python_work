favorite_numbers = {
    'ryan': [9, 49, 59],
    'erwin': [2, 12, 100],
    'poe': [3],
    'alex': [4, 50],
    'leslie': [6, 26, 36]
}

# print each person's name and thier favorite number
for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{person.title()}'s favorite number is: {numbers[0]}.")    
    else: 
        print(f"{person.title()}'s favorite numbers are: {[number for number in numbers]}.")