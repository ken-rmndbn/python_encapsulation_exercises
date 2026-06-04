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

    print(f"\n{Color.GREEN}{Color.BOLD}Successfully Registered!{Color.ENDC}")
    print("-" * 30)
    print(f"{Color.YELLOW}Pet Name: {Color.ENDC} {my_pet.get_name()}")
    print(f"{Color.YELLOW}Animal Type: {Color.ENDC} {my_pet.get_animal_type()}")
    print(f"{Color.YELLOW}Pet Age: {Color.ENDC} {my_pet.get_age()}")
    print("-" * 30)

if __name__ == "__main__":
    main()