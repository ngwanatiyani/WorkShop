from painting_workshop import PaintingWorkshop
from craft_workshop import CraftWorkshop
from cooking_workshop import CookingWorkshop
from photography_workshop import PhotographyWorkshop  
from dance_workshop import DanceWorkshop
from music_workshop import MusicWorkshop
def main():
    # create a PaintingWorkshop instance
    
    painting_workshop = PaintingWorkshop("Painting Workshop", "Learn to paint with watercolors", "2021-06-01", "John Doe", 2)
    print(painting_workshop.get_details())
    print()
    
    # create a CraftWorkshop instance
    craft_workshop = CraftWorkshop("Craft Workshop", "Create a beautiful piece of art", "2021-06-02", "Jane Doe")
    print(craft_workshop.get_details())
    print()
    
    # create a CookingWorkshop instance
    cooking_workshop = CookingWorkshop("Cooking Workshop", "Learn to cook delicious meals", "2021-06-03", "Alice Smith", 2)
    print(cooking_workshop.get_details()) 
    print()
    
    # create a PhotographyWorkshop instance
    photography_workshop = PhotographyWorkshop("Photography Workshop", "Learn to take great photos", "2021-06-04", "Bob Brown")     
    print(photography_workshop.get_details())
    print() 
    
    # create a DanceWorkshop instance
# Inside the main() function in main.py
    dance_workshop = DanceWorkshop("Dance Workshop", "Learn to dance like a pro", "2024-06-05", "Sara Johnson", 2) 
    print(dance_workshop.get_details())
    print()
    
    # create a MusicWorkshop instance
    music_workshop = MusicWorkshop("Music Workshop", "Learn to play the guitar", "2024-06-06", "Mike Davis")
    print(music_workshop.get_details())
    print()
    
if __name__ == "__main__":
    main()
# Output
# Painting Workshop - Learn to paint with watercolors (Date: 2021-06-01, Instructor: John Doe, Duration: 2 hours)
#
# Craft Workshop - Create a beautiful piece of art (Date: 2021-06-02, Instructor: Jane Doe)
#
# Cooking Workshop - Learn to cook delicious meals (Date: 2021-06-03, Instructor: Alice Smith, Duration: 2 hours)
#
# Photography Workshop - Learn to take great photos (Date: 2021-06-04, Instructor: Bob Brown)
#
# Dance Workshop - Learn to dance like a pro (Date: 2024-06-05, Instructor: Sara Johnson, Duration: 2 hours)
#
# Music Workshop - Learn to play the guitar (Date: 2024-06-06, Instructor: Mike Davis)
# In the main.py file, we create instances of each workshop type and call the get_details() method to print the details of each workshop.
# The code is more organized and easier to manage because we have separated the workshop classes into different files.
# This makes it easier to add new workshop types in the future without modifying the existing code.
# The code is also more readable and maintainable because each workshop class is defined in its own file, making it easier to understand and work with.
# By following this approach, we have achieved a better separation of concerns and improved code organization.
# This is an example of how to structure a Python project with multiple classes and files. This approach can be applied to larger projects to improve code organization and maintainability.
# Conclusion
# In this tutorial, we have learned how to structure a Python project with multiple classes and files. We have explored different ways to organize classes and files in a Python project, including:
# Defining multiple classes in a single file

   
    
