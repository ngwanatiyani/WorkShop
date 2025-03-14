# painting_workshop.py
class PaintingWorkshop:
    def __init__(self, title, description, date, instructor, duration):
        self.title = title
        self.description = description
        self.date = date
        self.instructor = instructor
        self.duration = duration

    def get_details(self):
        return f"{self.title} - {self.description} (Date: {self.date}, Instructor: {self.instructor}, Duration: {self.duration} hours)"