import pandas

student_dict = {
    "student": ["angela","jame","lily"],
    "score": [46,23,56]
}

for (key, value) in student_dict.items():
    print(value)

print(student_dict.items())
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# #loop through a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

#loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == 'angela':
        print(row.score)
        


