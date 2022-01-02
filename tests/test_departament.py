from unittest import TestCase, main
from domain.departament import Departament
from domain.patient import Patient


class DepartmentTest(TestCase):

    def setUp(self):
        self.__department = Departament("test_dep", 100, [Patient("Nicusor", "Emil", "1980507387664", "cancer"),
                                                         Patient("Eugenia", "Diana", "2960102510915", "covid"),
                                                         Patient("Sandra", "Dinu", "6020921465064", "covid"),
                                                         Patient("Costel", "Virgil", "1600102022999", "malaria"),
                                                         Patient("Stefanescu", "Anca", "2700113027943", "covid"),
                                                         Patient("Baltazar", "Olimpiu", "1300113025387", "hypertension"),
                                                         Patient("Suceava", "Roxana", "2550113022071", "cancer")])

    def test_get_name_id(self):
        self.assertEqual(self.__department.get_name_id(), "test_dep")
        self.assertEqual(Departament("test_dep1", 100, []).get_name_id(), "test_dep1")
        self.assertEqual(Departament("test", 12, []).get_name_id(), "test")

    def test_get_number_of_beds(self):
        self.assertEqual(self.__department.get_number_beds(), 100)
        self.assertEqual(Departament("test_dep1", 10, []).get_number_beds(), 10)
        self.assertEqual(Departament("test", 12, []).get_number_beds(), 12)

    def test_get_patients(self):
        def comp (list_1, list_2):
            if len(list_2) != len(list_1):
                return False
            for i in range(len(list_1)):
                if list_1[i] != list_2[i]:
                    return False
            return True
        self.assertTrue(comp(self.__department.get_patients(), [Patient("Nicusor", "Emil", "1980507387664", "cancer"),
                                                                Patient("Eugenia", "Diana", "2960102510915", "covid"),
                                                                Patient("Sandra", "Dinu", "6020921465064", "covid"),
                                                                Patient("Costel", "Virgil", "1600102022999", "malaria"),
                                                                Patient("Stefanescu", "Anca", "2700113027943", "covid"),
                                                                Patient("Baltazar", "Olimpiu", "1300113025387", "hypertension"),
                                                                Patient("Suceava", "Roxana", "2550113022071", "cancer")]))
        self.assertTrue(comp(Departament("new_dep", 13, []).get_patients(), []))
        self.assertTrue(comp(Departament("new_dep", 12, [Patient("Eugenia", "Diana", "2960102510915", "covid")]).get_patients()
                                                         , [Patient("Eugenia", "Diana", "2960102510915", "covid")]))

    def test_add_patient(self):
        with self.assertRaises(ValueError):
            self.__department.add_patient(Patient("Costel", "Pop", "2700113027943", "covid"))
            self.__department.add_patient(Patient("Marcel", "Horezu", "2550113022071", "cancer"))
        self.__department.add_patient(Patient("Retezat", "Sergiu", "19980305291978", "flu"))
        self.assertTrue(self.__department.get_patients()[-1] == Patient("Retezat", "Sergiu", "19980305291978", "flu"))

    def test_get_patients_by_personal_code(self):
        with self.assertRaises(ValueError):
            self.__department.get_patient_by_personal_code("2700113047943")
            self.__department.get_patient_by_personal_code("2550113022091")
        self.assertTrue(self.__department.get_patient_by_personal_code("6020921465064") == Patient("Sandra", "Dinu", "6020921465064", "covid"))

    def test_delete_patients_by_personal_code(self):
        with self.assertRaises(ValueError):
            self.__department.delete_patient_by_personal_code("2700113047943")
            self.__department.delete_patient_by_personal_code("2550113022091")
        self.__department.delete_patient_by_personal_code("2700113027943")
        self.assertTrue(len(self.__department.get_patients()) == 6)

    def test_update_patients_by_personal_code(self):
        with self.assertRaises(ValueError):
            self.__department.update_patient_by_personal_code("2700113047943", Patient("Osama", "Binladen", "2555113022071", "depression"))
            self.__department.update_patient_by_personal_code("2550113022091", Patient("Osama", "Mohamed", "2555113045071", "covid"))
            self.__department.update_patient_by_personal_code("1600102022999", Patient("Osama", "Mohamed", "2960102510915", "covid"))

    def test_update_number_of_beds(self):
        with self.assertRaises(ValueError):
            self.__department.update_number_of_beds(-10)
            self.__department.update_number_of_beds(-3)
        self.__department.update_number_of_beds(10)
        self.assertTrue(self.__department.get_number_beds() == 10)

    def test_get_patient_by_index(self):
        with self.assertRaises(IndexError):
            self.__department.get_patient_by_index(10)
            self.__department.get_patient_by_index(-19)
        self.assertEqual(self.__department.get_patient_by_index(3), Patient("Costel", "Virgil", "1600102022999", "malaria"))


if __name__ == "__main__":
    main()
