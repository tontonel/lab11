from unittest import TestCase, main
from data_example import examples


class TestDepartmentRepository(TestCase):

    def setUp(self):
        self.__repo = examples()

    def test_get_departments(self):
        self.assertTrue(len(self.__repo.get_departments()) == 4)
        self.assertTrue(self.__repo.get_departments()[0].get_name_id() == "dep1")
        self.assertTrue(self.__repo.get_departments()[2].get_name_id() == "dep3")

