from car_modification import CarModification
from output_color import OutputColor

def main():
    my_car = CarModification("2017", "Honda Fd")
    print(f"{OutputColor.BOLD}Testing Car: {my_car.get_info()}{OutputColor.RESET}")
    print("-" * 30)