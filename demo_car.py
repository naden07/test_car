import time
from car import Car


def main():
    my_car = Car(2024, "Toyota Supra")

    print("=" * 45)
    print(f"Starting engine for the {my_car.get_car_info()}")
    print("=" * 45)
    time.sleep(1)