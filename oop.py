# OBEJECT ORIANTED PROGRAMMING
# Wth oop we start by creating a class
# A class name starts with a capital lette and in singular


# cohort class

#assignment
# Add a constructor for the cohort class (read about the constructors)
# Add the method to the lass that pyints the cohort name and the total number of students 
#Create a new instance / object of the cohort class.
class Cohort:
    def __init__(self, name, description, start_date ,end_date,student_total_num ):
        self.name = name
        self .description = description
        self.start_date = start_date
        self.end_date = end_date
        self.student_total_num = student_total_num
    def print_cohort_info(self):
        print(f"Cohort Name of students: {self.name}") 
        print(f"Total number of students: {self.student_total_num}")
Cohort4 = Cohort(name ="python programing",
                 description ="A corse on python programing",
                 start_date ="28-08-2024",end_date="04-12-2024",
                student_total_num = 54)
Cohort4.print_cohort_info()

        
    
        
        
      
    


    
        