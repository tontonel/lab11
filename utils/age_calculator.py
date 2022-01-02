from datetime import date


def calculate_age(patient):
    """
    calculates age of a patient
    :param patient:
    :return:
    """
    cnp = patient.get_personal_code()
    patient_age = {}
    if int(cnp[0]) < 5:
        patient_age["year"] = int(f"19{cnp[1:3]}")
    else:
        patient_age["year"] = int(f"20{cnp[1:3]}")
    patient_age["month"] = int(cnp[3:4])
    patient_age["day"] = int(cnp[4:6])
    today = date.today()
    return today.year - patient_age["year"] - ((today.month, today.day) < (patient_age["month"], patient_age["day"]))
