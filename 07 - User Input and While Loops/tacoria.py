taco_orders = ['steak picado', 'bistek en salsa roja', 'mole poblano',
               'tinga de pollo', 'calabacitas', 'frijoles con queso']
finished_tacos = []

while taco_orders:
    taco = taco_orders.pop()
    print(f"{taco.title()} taco order complete.")
    finished_tacos.append(taco)

print("\n--- Order Summary ---")
for taco in finished_tacos:
    print(taco.title())