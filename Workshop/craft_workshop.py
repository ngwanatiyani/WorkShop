class CraftWorkshop:
    def __init__(self, title, description, date, instructor,):
        self.title = title
        self.description = description
        self.date = date
        self.instructor = instructor
    def get_details(self):
        return f"{self.title} - {self.description} Date: {self.date}, instrutor: {self.instructor}"    
   
        