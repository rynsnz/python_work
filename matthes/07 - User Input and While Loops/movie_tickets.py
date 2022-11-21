# calculate ticket prices
prompt = "\nWelcome to the movies! Enter the age of each guest for total cost:"
prompt += "\n(Enter 'done' when you are finished) "

total = 0

while True:
    age = input(prompt)
    if age == 'done':
        print(f"Your total is ${total}.")
        break
    if int(age) < 3:
        continue    
    if 3 <= int(age) <= 12:
        total += 10
    else:
        total += 15