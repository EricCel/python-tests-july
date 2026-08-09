#Generate a list of tuples (name, grade) and sort it from highest to lowest grade.
students = [('Robert','C'),('Albert','A'),('Michael','D'),('Peter','F'),('Aaron','B')]
students.sort(key=lambda x:x[1])
print(students)