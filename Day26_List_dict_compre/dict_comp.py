import random
names = ['Alex', 'Khanh', 'Huy', 'Kakashi','Obito']


students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
print(students_scores.items())

sentence = "What is the airspeed velcocity of an Unladen Swallow?"
passed_students = {student:score  for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

result = {word:len(word) for word in sentence.split()}
print(result)

