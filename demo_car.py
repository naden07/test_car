import time
from car import Car


def main():
    my_car = Car(2024, "Toyota Supra")

    print("=" * 45)
    print(f"Starting engine for the {my_car.get_car_info()}")
    print("=" * 45)
    time.sleep(1)

    print("\nVROOM! Hitting the gas...\n")
    time.sleep(0.5)

    for i in range(1, 6):
        my_car.accelerate()
        print(f"[Acceleration {i}/5] Current Speed: {my_car.get_speed():>3} km/h")
        time.sleep(0.7)

    print("\nWatch out! Stepping on the brakes...\n")
    time.sleep(0.5)

    for i in range(1, 6):
        my_car.brake()
        print(f"[Braking {i}/5]      Current Speed: {my_car.get_speed():>3} km/h")
        time.sleep(0.7)

    print("\n" + "=" * 45)
    print(f"The {my_car.get_car_info()} has come to a safe stop.")
    print("=" * 45)


if __name__ == "__main__":
    main()