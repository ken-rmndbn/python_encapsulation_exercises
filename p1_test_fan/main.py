from fan_modification import FanModification
from output_color import OutputColor

def main():
    fan_1 = FanModification()
    fan_1.set_speed(FanModification.FAST)
    fan_1.set_radius(10)
    fan_1.set_color("yellow")
    fan_1.set_on(True)

    fan_2 = FanModification()
    fan_2.set_speed(FanModification.MEDIUM)
    fan_2.set_radius(5)
    fan_2.set_color("blue")
    fan_2.set_on(False)

    print(f"\n{OutputColor.BOLD}{OutputColor.PURPLE}   FAN TESTING REPORT  {OutputColor.END}\n")

    print(f"{OutputColor.UNDERLINE}OBJECT 1 (Active Units){OutputColor.END}")
    print(fan_1)

    print(f"{OutputColor.UNDERLINE}OBJECT 2 (Storage Units){OutputColor.END}")
    print(fan_2)

if __name__ == "__main__":
    main()