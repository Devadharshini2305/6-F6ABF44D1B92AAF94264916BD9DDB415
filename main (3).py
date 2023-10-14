class students:
 def __init__(self,name,roll_number,cpga):
    self.name=name
    self.roll_number=roll_number
    self.cpga=cpga
def sort_students(students_list):
  sorted_students=sorted(students_list,key=lambda student:student.cpga,reverse=True)
  return sorted_students
students=[student("Abi","a 1",2),student("Bharathi","b2",3)]
sorted_students=sort_students(students)
for student in sorted_students:
  print("name:{},roll_number:{},cpqa:{}".format(student.name,student.roll_number,student.cpqa))


                                                                                     