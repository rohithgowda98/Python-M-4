# Exercise 1: Add a new student and their mark
students.append("Kiran")
marks.append(87)
print(f"New student added. Total: {len(marks)}")

# Exercise 2: Find all students scoring above 85
high_scorers = [(s, m) for s, m in zip(students, marks) if m > 85]
print(f"High scorers: {high_scorers}")

# Exercise 3: Calculate the class average using a loop
total = 0
for mark in marks:
    total += mark
avg = total / len(marks)
print(f"Class average: {avg:.2f}")

# Exercise 4: Reverse the marks list without changing the original
reversed_marks = marks[::-1]
print(f"Original:  {marks}")
print(f"Reversed:  {reversed_marks}")

# Exercise 5: Create a list of failing students (mark < 60)
failing = [(s, m) for s, m in zip(students, marks) if m < 60]
print(f"Failing students: {failing}")

# Exercise 6: Update a mark using indexing
marks[0] = 85  # Aisha got a re-grade
print(f"Aisha's new mark: {marks[0]}")

# Exercise 7: Use slicing to split the class into two groups
group_a = students[:5]
group_b = students[5:]
print(f"Group A: {group_a}")
print(f"Group B: {group_b}")

# Exercise 8: Find the second highest mark
sorted_marks = sorted(marks, reverse=True)
second_highest = sorted_marks[1]
print(f"Second highest mark: {second_highest}")