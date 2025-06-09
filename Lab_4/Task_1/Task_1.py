from Car import Car

my_car = Car("Toyota", "Corolla", 2020)

print("Accelerating:")
for i in range(5):
    my_car.accelerate()
    print(f"Speed after acceleration {i+1}: {my_car.get_speed()} km/h")

print("\nBraking:")
for i in range(5):
    my_car.brake()
    print(f"Speed after braking {i+1}: {my_car.get_speed()} km/h")