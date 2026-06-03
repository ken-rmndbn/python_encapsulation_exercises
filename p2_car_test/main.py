from car_modification import CarModification
from output_color import OutputColor

def main():
    my_car = CarModification("2017", "Honda Fd")
    print(f"{OutputColor.BOLD}Testing Car: {my_car.get_info()}{OutputColor.RESET}")
    print("-" * 30)

    print(f"\n{OutputColor.GREEN}Accelerating...{OutputColor.RESET}")
    for car in range(5):
        my_car.accelerate()
        print(f"Current speed: {OutputColor.CYAN}{my_car.get_speed()}{OutputColor.RESET}")

    print(f"\n{OutputColor.RED}Breaking...{OutputColor.RESET}")
    for car in range(5):
        my_car.brake()
        print(f"Current speed: {OutputColor.CYAN}{my_car.get_speed()}{OutputColor.RESET}")
        