from fan_modification import FanModification
from output_color import OutputColor

def main():
    fan_1 = FanModification()
    fan_1.set_speed(FanModification.FAST)
    fan_1.set_radius(10)
    fan_1.set_color("yellow")
    fan_1.set_on(True)
    