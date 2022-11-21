taco_orders = ['steak picado', 'bistek en salsa roja', 'mole poblano',
               'tinga de pollo', 'calabacitas', 'frijoles con queso',
               'tinga de pollo', 'steak picado', 'bistek en salsa roja']

finished_tacos = []

print("We ran out of steak! Alert the customers!\n")
while ('steak picado' and 'bistek en salsa roja') in taco_orders:
    taco_orders.remove('steak picado')
    taco_orders.remove('bistek en salsa roja')

while taco_orders:
    taco = taco_orders.pop()
    print(f"{taco.title()} taco order complete.")
    finished_tacos.append(taco)

print("\n--- Order Summary ---")
for taco in finished_tacos:
    print(taco.title())