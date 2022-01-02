class Patient:
	def __init__(self, first_name, last_name, personal_code, disease):
		"""
		initialize the patient
		:return:
		"""
		if not (first_name.isalpha() and last_name.isalpha()):
			raise ValueError("The name should contain only letters")
		self.__first_name = first_name
		self.__last_name = last_name
		self.__personal_code = personal_code
		self.__disease = disease

	def get_first_name(self):
		"""
		get the first name of the patient
		:return:
		"""
		return self.__first_name

	def get_last_name(self):
		"""
		get the last name of the patient
		:return:
		"""
		return self.__last_name

	def get_personal_code(self):
		"""
		get personal code
		:return:
		"""
		return self.__personal_code

	def get_disease(self):
		"""
		get the disease of the patient
		:return:
		"""
		return self.__disease

	def set_first_name(self, new_first_name):
		"""
		set the first name
		:param new_first_name:
		:return:
		"""
		if not new_first_name.isalpha():
			raise ValueError("The name should contain only letters")

		self.__first_name = new_first_name

	def set_last_name(self, new_last_name):
		"""
		set the last name
		:param new_last_name:
		:return:
		"""
		if not new_last_name.isalpha():
			raise ValueError("The name should contain only letters")
		self.__last_name = new_last_name

	def set_personal_code(self, new_personal_code):
		"""
		set the personal_code
		:param new_personal_code:
		:return:
		"""
		self.__personal_code = new_personal_code

	def set_disease(self, new_disease):
		"""
		set new disease
		:param new_disease:
		:return:
		"""
		self.__disease = new_disease

	def __eq__(self, other):
		"""
		compare two patients objects
		:param other:
		:return:
		"""
		if (self.__disease != other.get_disease() or
				self.__first_name != other.get_first_name() or
					self.__last_name != other.get_last_name() or
						self.__personal_code != other.get_personal_code()):
			return False
		return True

	def __str__(self):
		return f"Name: {self.__first_name} {self.__last_name}, ID: {self.__personal_code}, Disease: {self.__disease}"

