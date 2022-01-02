def menu():
    """
    prints menu and read command
    :return:
    """
    print("1. Sort the patients in a department by personal numerical code")
    print("2. Sort departments by the number of patients")
    print("3. Sort departments by the number of patients having the age above a given limit")
    print("4. Sort departments by the number of patients and the patients in a department alphabetically")
    print("5. Identify departments where there are patients under a given age")
    print("6. Identify patients from a given department for which the first name or last name contain a given string")
    print("7. Identify department/departments where there are patients with a given first name")
    print("8. Form groups of k patients from the same department and the same disease")
    print("9. Form groups of k departments having at most p patients suffering from the same disease")
    print("0. Exit")
    command = int(input("\nEnter a command: "))
    if not 0 <= command <= 9:
        raise ValueError("Your command is invalid")
    return command
