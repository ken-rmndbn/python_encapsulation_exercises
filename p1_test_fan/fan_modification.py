from output_color import OutputColor

class FanModification:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5.0, color = "blue", on = False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)

    def get_speed(self): return self.__speed
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def is_on(self): return self.__on

    def set_speed(self, speed):
        if speed in [FanModification.SLOW, FanModification.MEDIUM, FanModification.FAST]:
            self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

    def __str__(self):
        status_color = OutputColor.GREEN if self.__on else OutputColor.RED
        status_text = "ON" if self.__on else "OFF"

        speed_name = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}. get(self.__speed, "UNKNOWN")

        return(
            f"{OutputColor.BOLD}Speed:{OutputColor.END} {OutputColor.CYAN}{speed_name} ({self.__speed}){OutputColor.END}\n"
            f"{OutputColor.BOLD}Color:{OutputColor.END} {OutputColor.YELLOW}{self.__color.capitalize()}{OutputColor.END}\n"
            f"{OutputColor.BOLD}Radius:{OutputColor.END} {self.__radius}\n"
            f"{OutputColor.BOLD}Status:{OutputColor.END} {status_color}{status_text}{OutputColor.END}\n"
            f" {'-' * 25}"
        )