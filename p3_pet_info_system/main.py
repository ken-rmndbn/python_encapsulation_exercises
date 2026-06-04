from pet_modification import PetModification
from output_color import OutputColor as Color

def main():
    print(f"{Color.HEADER}{Color.BOLD}    PET INFORMATION SYSTEM    {Color.ENDC}\n")

    my_pet = PetModification()

    print(f"{Color.BLUE}Please enter your pet details:{Color.ENDC}")

    name = input("Enter pet name: ")
    pet_type = input("Enter animal type: ")
    try:
        age = int(input("Enter pet age: "))
    except ValueError:
        print(f"{Color.FAIL}Invalid age entered. Default to 0.{Color.ENDC}")
        age = 0

    my_pet.__set_name__(name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(age)
    