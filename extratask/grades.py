grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

# grades_by_assignment = { }
grades_dic = {}
for j in range(1, len(grades[0])):
    temp_list = []
    for i in range(1, len(grades)):
        temp_list.append(int(grades[i][j]))
    grades_dic[grades[0][j]] = temp_list
print(grades_dic)

# print(grades[[0][j]])
# grade_lists={}
# for row in grades[1:]:
#     print(row[0])
#     # grade_lists[row[0]=list(map(int,row[1:]))
