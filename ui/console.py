from infrastructure.departamentRepository import DepartamentRepository
from domain.patient import Patient
from domain.departament import Departament
from data_example import examples
from ui.menu.menu import menu
from controller.controller import Controller


def run():
    """
    runs the app
    :return:
    """
    controller = Controller(examples())
    command = -1
    while command != 0:
        try:
            command = menu()
            if command == 1:
                department_id = input("Enter the name id of department: ")
                controller.sort_patients_by_personal_code(department_id)
            elif command == 2:
                controller.sort_by_number_of_patients()
            elif command == 3:
                age = int(input("Enter an age: "))
                controller.sort_by_age(age)
            elif command == 4:
                controller.sort_by_number_of_patients_and_name()
            elif command == 5:
                age = int(input("Enter an age: "))
                controller.department_under_age(age)
            elif command == 6:
                index = int(input("Enter an index of an department: "))
                string = input("Enter a string: ")
                controller.get_patients_with_string_name(index, string)
            elif command == 7:
                first_name = input("Enter the first name: ")
                controller.departments_with_patients_name(first_name)
            elif command == 8:
                k = int(input("Enter a k: "))
                controller.groups_of_k_with_same_disease(k)
            elif command == 9:
                k = int(input("Enter a k: "))
                p = int(input("Enter a p: "))
                controller.groups_of_k_with_p_patients(k, p)
        except ValueError as Vr:
            print(f"\n{Vr}\n")
        except IndexError as Ir:
            print(f"\n{Ir}\n")
        except IOError as Io:
            print(f"\n{Io}\n")


run()
