from utils.sort_algo import sort_algo
from domain.departament import Departament
from utils.backtracking import backtracking
from utils.age_calculator import calculate_age


class DepartamentRepository:

	def __init__(self, departments: [Departament] = None):
		"""
		initialize the repository
		:return:
		"""
		if departments is None:
			departments = []
		for i in range(len(departments) - 1):
			for j in range(i + 1, len(departments)):
				if departments[i].get_name_id() == departments[j].get_name_id():
					raise ValueError("There two repositories with same name")
		self.__departments = departments

	def get_departments(self):
		"""
		get the list of departments
		:return:
		"""
		return self.__departments[:]

	def sort_by_number_of_patients(self):
		"""
		sort the departments by number of patients
		:return:
		"""
		self.__departments = sort_algo(self.__departments[:],
		lambda x1, x2: bool(x1.get_number_of_patients() <= x2.get_number_of_patients()))

	def sort_by_age(self, age):
		"""
		sort the department with by number of patients above a given age
		:param age:
		:return:
		"""
		def get_patients_above(department):
			counter = 0
			for patient in department.get_patients():
				if calculate_age(patient) >= age:
					counter += 1
			return counter
		self.__departments = sort_algo(self.__departments[:],
		lambda x1, x2: bool(get_patients_above(x1) <= get_patients_above(x2)))

	def sort_by_number_of_patients_and_name(self):
		"""
		sort by number of patients and patients alphabetically
		:return:
		"""
		self.sort_by_number_of_patients()
		for departament in self.__departments:
			departament.sort_by_name()

	def department_under_age(self, age):
		"""
		get departments with patients under a given age
		:param age:
		:return:
		"""
		def patients_under_age(patients):
			for patient in patients:
				if calculate_age(patient) < age:
					return True
			return False
		department_list = []
		for department in self.__departments:
			if patients_under_age(department.get_patients()):
				department_list.append(department)
		if not department_list:
			raise ValueError(f"There are no departments with patients under {age}")
		return DepartamentRepository(department_list)

	def get_patients_with_string_name(self, index, string):
		"""
		get patients with specific string in name
		:param index:
		:param string:
		:return:
		"""
		if not 0 <= index <= len(self.__departments):
			raise IndexError("Your index is out of range")
		patients = []
		for patient in self.__departments[index].get_patients():
			if patient.get_first_name().find(string) != -1:
				patients.append(patient)
			elif patient.get_last_name().find(string) != -1:
				patients.append(patient)
		if not patients:
			raise ValueError("The string is not contained in any of the patients names")
		return Departament("newDep", 0, patients)

	def departments_with_patients_name(self, first_name):
		"""
		find departments with patients that have a given first name
		:param first_name:
		:return:
		"""
		departments_list = []
		for department in self.__departments:
			for patient in department.get_patients():
				if patient.get_first_name() == first_name:
					departments_list.append(department)
					break
		if not departments_list:
			raise ValueError(f"There are no patients with first name {first_name}")
		return DepartamentRepository(departments_list)

	def groups_of_k_with_same_disease(self, k):
		"""
		generate all the groups of patients in department with same disease
		:param k:
		:return:
		"""
		groups = []
		for department in self.__departments:
			diseases = []
			for patient in department.get_patients():
				if not patient.get_disease() in diseases:
					diseases.append(patient.get_disease())

			groups.append([department])
			for disease in diseases:
				for combination in backtracking([],
							exist = lambda solution: solution[-1] < len(department.get_patients()),
						   	is_solution = lambda solution: len(solution) == k,
							consistent = lambda solution: department.get_patient_by_index(
												solution[-1]).get_disease() == disease
												and all(i < j for i, j in zip(solution, solution[1:]))):
					if combination is None:
						raise ValueError(f"It can not be formed groups of {k} patients")
					groups[-1].append(list(map(lambda index: department.get_patients()[index], combination)))

		return groups.copy()

	def groups_of_k_with_p_patients(self, k, p):
		"""
		form groups of p patients from at most k departments
		:param k:
		:param p:
		:return:
		"""
		groups = []
		for department_combination in backtracking([],
										exist = lambda solution: solution[-1] < len(self.__departments),
										is_solution = lambda solution: len(solution) == k,
										consistent = lambda solution: all(i < j for i, j in zip(solution, solution[1:]))):
			if department_combination is None:
				raise ValueError(f"It can not be formed groups of {k} departments")
			groups.append([[self.__departments[index] for index in department_combination]])
			patients = [patient
						for depart_index in department_combination
						for patient in self.__departments[depart_index].get_patients()
			]
			diseases = []
			for patient in patients:
				if not patient.get_disease() in diseases:
					diseases.append(patient.get_disease())
			for disease in diseases:
				for combination in backtracking([],
							exist = lambda solution: solution[-1] < len(patients),
						   	is_solution = lambda solution: len(solution) == p,
							consistent = lambda solution: patients[solution[-1]].get_disease() == disease
												and all(i < j for i, j in zip(solution, solution[1:]))):
					if combination is None:
						raise ValueError(f"It can not be formed groups of {p} patients")
					groups[-1].append(list(map(lambda index: patients[index], combination)))
		return groups[:]

	def __str__(self):
		text = ""
		for department in self.__departments:
			text += department.__str__() + "\n"
		return text
