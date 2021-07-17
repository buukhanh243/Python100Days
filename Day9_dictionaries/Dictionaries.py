student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermirone": 99, 
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
 score = student_scores[student]
 if score > 90:
     student_grades[student] = 'Out standing'
 elif score > 80:
     student_grades[student] = 'Exceeds Expectations'
 elif score > 70:
     student_grades[student] = 'Acceptable'
 else:
     student_grades[student] = 'Fail'


print(student_grades)

#nesting
capitals = {
 'france': "Paris",
 'germany': 'Berlin'
}
#Nesting Dictionary in a Dictionary
travel_log = {
 'France': {'cities_visited': ['Paris','Little','dijon'], 'total_visits':12},
 'Germany': ['Berlin', 'Hamburg','Stuttgart']
}

# ['A', 'B', ['C', 'D']]

#Nesting Dictionary in a List
travel_log = [
 {
  'country':'France',
  'cities_visited': ['Paris','Little','dijon'],
  'total_visits':12
 },
 {
  'country':'Germany',
  'cities_visited': ['Berlin', 'Hamburg','Stuttgart'],
  'total_visits':5
 }
]


