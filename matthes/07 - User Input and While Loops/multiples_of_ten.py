prompt = "Enter a number. "
prompt += "I'll tell you if it is a multiple of 10 or not: "
number = int(input(prompt))

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")