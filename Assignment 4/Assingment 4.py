eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]

for students in students:
    for x,y in students.items():
      print("{}: {}" .format(x, y))

def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total / len(numbers)
    return result

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  weighted_average = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
  return weighted_average

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

letter_grade = get_letter_grade(get_average(mikasa))
print(letter_grade)

def get_class_average(students):
  results = []
  for student in students:
    results.append(get_average(student))
  return average(results)

students = [eren, mikasa, armin]

print (get_class_average(students))

print (get_letter_grade(get_class_average(students)))