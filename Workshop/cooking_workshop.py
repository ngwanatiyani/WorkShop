class CookingWorkshop:
    def __init__(self, tittle, description, date, instructor, duration):
        self.tittle = tittle
        self.description = description
        self.date = date
        self.instructor = instructor
        self.duration = duration
    def get_details(self):    
        return f"{self.tittle} - {self.description} Date: {self.date}, instrutor: {self.instructor}, Duration: {self.duration} hours"
    