class Cohort:
      def __init__(self,name,description,start_date,end_date,total_students):
         self .name = name  
         self.description=description
         self.start_date= start_date
         self.end_date=end_date
         self.total_students=total_students  
      def display_info(self):
          print (f"Cohort Name:{self.name}")  
          print(f"Total Students:{self.total_students}")

cohort4=Cohort(
    name="Ramula" ,
    description= "A cohort for computer science course",
    start_date="2023-20-08",
    end_date="2026-19-07",
    total_students=66
)    
 

class Cohort:
    def __init__(data,name,description,start_date,end_date,total_students):
     data.name=name
     data.description=description
     data.start_date= start_date
     data.end_date=end_date
     data.total_students=total_students
       
cohort5=Cohort(
       name="Rubuga",
       description= "A cohort for computer science course",
    start_date="2023-20-08",
    end_date="2026-19-07",
    total_students=50
)

def display_info(data):
          print (f"Cohort Name:{data.name}")  
          print(f"Total Students:{data.total_students}")



