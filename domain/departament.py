from utils.sort_algo import sort_algo


class Departament:

	def __init__(self, name_id, number_beds, patients):
		"""
		initialize the departament
		:return:
		"""
		self.__number_beds = number_beds
		self.__patients = patients
		self.__name_id = name_id

	def get_name_id(self):
		"""
		get the name id of departament
		:return:
		"""
		return self.__name_id

	def get_number_beds(self):
		"""
		get the number of beds
		:return:
		"""
		return self.__number_beds

	def get_patients(self):
		"""
		get the list of patients
		:return:
		"""
		return self.__patients.copy()

	def add_patient(self, patient):
		"""
		add a patient
		:param patient:
		:return:
		"""
		if self.get_number_beds() < len(self.__patients):
			raise ValueError("All beds are occupied")
		for p in self.__patients:
			if p.get_personal_code() == patient.get_personal_code():
				raise ValueError("There is another patient with same id")
		self.__patients.append(patient)

	def get_patient_by_index(self, index):
		"""
		returns a patient by index
		:param index:
		:return:
		"""
		if not 0 <= index < len(self.__patients):
			raise IndexError("Index out of range")
		return self.__patients[index]

	def get_patient_by_personal_code(self, cnp):
		"""
		get patient by personal code
		:param cnp:
		:return:
		"""
		match = None
		for patient in self.__patients:
			if patient.get_personal_code() == cnp:
				match = patient
		if match is None:
			raise ValueError(f"There is no patient with this personal code {cnp}")
		return match

	def delete_patient_by_personal_code(self, cnp):
		"""
		delete a patient by his personal code
		:param cnp:
		:return:
		"""
		match = None
		for patient in self.__patients:
			if patient.get_personal_code() == cnp:
				match = patient
		if match is None:
			raise ValueError(f"There is no patient with this personal code {cnp}")
		new_patients = []
		for patient in self.__patients:
			if patient.get_personal_code() != cnp:
				new_patients.append(patient)
		self.__patients = new_patients

	def delete_patient_by_name(self, first_name, last_name):
		new_patients = []
		for patient in self.__patients:
			if patient.get_first_name() == first_name and patient.get_last_name() == last_name:
				pass
			else:
				new_patients.append(patient)

	def update_patient_by_personal_code(self, personal_code, new_patient):
		"""
		update a patient by personal code
		:param new_patient:
		:param personal_code:
		:return:
		"""
		for patient in self.__patients:
			if new_patient.get_personal_code() == patient.get_personal_code():
				raise ValueError("The new patient have the same cnp as another patient")
		found = -1
		for i in range(len(self.__patients)):
			if self.__patients[i].get_personal_code() == personal_code:
				self.__patients[i] = new_patient
				found = 1
		if found == -1:
			raise ValueError(f"There is no patient with personal code: {personal_code}")

	def update_patient_by_name(self, first_name, last_name, new_patient):
		"""
		update a patient with a given name
		:param first_name:
		:param last_name:
		:param new_patient:
		:return:
		"""
		found = -1
		for i in range(len(self.__patients)):
			if self.__patients[i].get_first_name() == first_name and self.__patients[i].get_last_name() == last_name:
				self.__patients[i] = new_patient
				found = 1
		if found == -1:
			raise ValueError(f"There is no patient with name: {first_name} {last_name}")

	def update_number_of_beds(self, number_beds):
		"""
		update number of beds
		:param number_beds:
		:return:
		"""
		if number_beds < 0:
			raise ValueError("There can not be a negative number of beds")
		self.__number_beds = number_beds

	def sort_patients(self):
		"""
		sort patients by numerical code
		:return:
		"""
		self.__patients = sort_algo(self.__patients.copy(), lambda x1, x2: bool(x1.get_personal_code() <= x2.get_personal_code()))

	def get_number_of_patients(self):
		"""
		returns the number of patients
		:return:
		"""
		return len(self.__patients)

	def sort_by_name(self):
		"""
		sort patients by name;
		:return:
		"""
		self.__patients = sorted(self.__patients,
		key = lambda patient: patient.get_first_name() + patient.get_last_name())

	def __str__(self):
		text = f"\nDepartament: {self.__name_id}, Number of beds: {self.__number_beds}, Patients:\n"
		for patient in self.__patients:
			text += f"{'':<3}-{patient.__str__()}\n"
		return text
