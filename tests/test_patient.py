from unittest import TestCase, main
from domain.patient import Patient


class TestPatient(TestCase):

	def setUp(self):
		self.__patient = Patient("Parker", "Peter", "05010810261978", "covid")

	def test_get_first_name(self):
		self.assertTrue(self.__patient.get_first_name() == "Parker")
		self.__patient = Patient("Pop", "Peter", "05010810261978", "covid")
		self.assertTrue(self.__patient.get_first_name() == "Pop")
		self.__patient = Patient("Serban", "Peter", "05010810261978", "covid")
		self.assertEqual(self.__patient.get_first_name(), "Serban")

	def test_get_last_name(self):
		self.assertTrue(self.__patient.get_last_name() == "Peter")
		self.__patient = Patient("Pop", "Poly", "05010810261978", "covid")
		self.assertTrue(self.__patient.get_last_name() == "Poly")
		self.__patient = Patient("Serban", "Marin", "05010810261978", "covid")
		self.assertEqual(self.__patient.get_last_name(), "Marin")

	def test_get_personal_code(self):
		self.assertTrue(self.__patient.get_personal_code() == "05010810261978")
		self.__patient = Patient("Pop", "Poly", "05010810231978", "covid")
		self.assertTrue(self.__patient.get_personal_code() == "05010810231978")
		self.__patient = Patient("Serban", "Marin", "05011010261978", "covid")
		self.assertTrue(self.__patient.get_personal_code() == "05011010261978")

	def test_get_disease(self):
		self.assertTrue(self.__patient.get_disease() == "covid")
		self.__patient = Patient("Pop", "Poly", "05010810231978", "cancer")
		self.assertTrue(self.__patient.get_disease() == "cancer")
		self.__patient = Patient("Serban", "Marin", "05011010261978", "flu")
		self.assertTrue(self.__patient.get_disease() == "flu")

	def test_set_first_name(self):
		self.__patient.set_first_name("Octavus")
		self.assertTrue(self.__patient.get_first_name() == "Octavus")
		self.__patient.set_first_name("Pop")
		self.assertTrue(self.__patient.get_first_name() == "Pop")
		self.__patient.set_first_name("Sabau")
		self.assertTrue(self.__patient.get_first_name() == "Sabau")

	def test_set_last_name(self):
		self.__patient.set_last_name("Mihai")
		self.assertTrue(self.__patient.get_last_name() == "Mihai")
		self.__patient.set_last_name("Marinica")
		self.assertTrue(self.__patient.get_last_name() == "Marinica")
		self.__patient.set_last_name("Cezar")
		self.assertTrue(self.__patient.get_last_name() == "Cezar")

	def test_personal_code(self):
		self.__patient.set_personal_code("05023810261978")
		self.assertTrue(self.__patient.get_personal_code() == "05023810261978")
		self.__patient.set_personal_code("05023810261933")
		self.assertTrue(self.__patient.get_personal_code() == "05023810261933")
		self.__patient.set_personal_code("05023810261944")
		self.assertTrue(self.__patient.get_personal_code() == "05023810261944")

	def test_set_disease(self):
		self.__patient.set_disease("cancer")
		self.assertTrue(self.__patient.get_disease() == "cancer")
		self.__patient.set_disease("depression")
		self.assertTrue(self.__patient.get_disease() == "depression")
		self.__patient.set_disease("flu")
		self.assertTrue(self.__patient.get_disease() == "flu")


if __name__ == "__main__":
	main()
