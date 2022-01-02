from infrastructure.departamentRepository import DepartamentRepository


class Controller:

    def __init__(self, repo: DepartamentRepository):
        """
        initialize controller with repository
        :param repo:
        """
        self.__repo = repo

    def sort_by_number_of_patients(self):
        """
        handle sort by number of patients
        :return:
        """
        self.__repo.sort_by_number_of_patients()
        print(self.__repo)

    def sort_patients_by_personal_code(self, department_id):
        """
        sort patients in a specific department by personal numerical code
        :param department_id:
        :return:
        """
        find = False
        for department in self.__repo.get_departments():
            if department.get_name_id() == department_id:
                department.sort_patients()
                print(department)
                find = True
        if not find:
            raise ValueError(f"There is no department with this name id: {department_id}")

    def sort_by_age(self, age):
        """
        sort department by a given limit of age
        :param age:
        :return:
        """
        if age <= 0:
            raise IOError("The age should not be a negative number")
        self.__repo.sort_by_age(age)
        print(self.__repo)

    def sort_by_number_of_patients_and_name(self):
        """
        sort department by number o patients and departments by name of the patients
        :return:
        """
        self.__repo.sort_by_number_of_patients_and_name()
        print(self.__repo)

    def department_under_age(self, age):
        """
        get department with patients under a given age
        :param age:
        :return:
        """
        if age <= 0:
            raise IOError("The age should not be a negative number")
        departments = self.__repo.department_under_age(age)
        print(departments)

    def get_patients_with_string_name(self, index, string):
        """
        get patients with specific string in name
        :param index:
        :param string:
        :return:
        """
        department = self.__repo.get_patients_with_string_name(index, string)
        print(department)

    def departments_with_patients_name(self, first_name):
        """
        find departments with patients with given first name
        :param first_name:
        :return:
        """
        new_repo = self.__repo.departments_with_patients_name(first_name)
        print(new_repo)

    def groups_of_k_with_same_disease(self, k):
        """
        print all groups of k patients with same disease
        :param k:
        :return:
        """
        groups = self.__repo.groups_of_k_with_same_disease(k)
        for group in groups:
            if len(group) != 1:
                print(f"Department: {group[0].get_name_id()}:")
                for comb in group[1:]:
                    for patient in comb:
                        print(f"{'':<3}-{patient}")
                    print()

    def groups_of_k_with_p_patients(self, k, p):
        """
        print groups of k departments with groups of p patients with same disease
        :param k:
        :param p:
        :return:
        """
        groups = self.__repo.groups_of_k_with_p_patients(k, p)
        for group in groups:
            if len(group) != 1:
                text = "Departments: "
                for department in group[0]:
                    text += f"{department.get_name_id()}, "
                text = text[:-2] + ":"
                print(text)
                for comb in group[1:]:
                    for patient in comb:
                        print(f"{'':<3}-{patient}")
                    print()

