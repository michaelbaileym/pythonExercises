ANSWER_KEY = {"1": "A", "2": "C", "3": "B", "4": "B" }
students = {}

students['Mike'] = {"1": "D", "2": "B", "3": "D", "4": "B" }
students['Jeff'] = {"1": "C", "2": "D", "3": "B", "4": "B" }
students['John'] = {"1": "A", "2": "C", "3": "D", "4": "A" }

for student, answers in students.items():
    grade = 0
    for question, answer in ANSWER_KEY.items():
       if answer == ANSWER_KEY[question]:
           grade += 1
    students[student]["grade"] = grade

print(students[student][0])