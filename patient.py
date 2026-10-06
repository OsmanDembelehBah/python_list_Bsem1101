# Patient Class 
class Patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        #a function that print out patients informations 
    def display_info(self):
        print("\n===================== PATIENT INFORMATION ======================")
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")
        
        
        