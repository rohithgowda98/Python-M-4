"""
Student Scores Analyzer
This program demonstrates:
1. Storing student scores in a dictionary
2. Using loops to calculate the class average
3. Using loops to find the top scorer
4. Looking up any student by name (with safe error handling)
"""

# ============================================
# SECTION 1: STORE STUDENT SCORES
# ============================================

print("=" * 60)
print("        🎓 STUDENT SCORES ANALYZER")
print("=" * 60)
print()

# Dictionary: student name → score (out of 100)
student_scores = {
    "Aisha": 92,
    "Ben": 75,
    "Chloe": 88,
    "Daniel": 65,
    "Emma": 98,
    "Faisal": 81,
    "Grace": 90,
    "Hassan": 59,
    "Ivy": 87,
    "Jack": 73
}

print("📋 STUDENT SCORES")
print("-" * 40)
for name, score in student_scores.items():
    print(f"   {name:<10} → {score}")
print()

# ============================================
# SECTION 2: FIND THE CLASS AVERAGE (LOOP)
# ============================================

print("📊 CLASS AVERAGE")
print("-" * 40)

# Use a loop to sum all scores
total = 0
for score in student_scores.values():
    total += score

# Calculate average
average = total / len(student_scores)

print(f"   Total students: {len(student_scores)}")
print(f"   Total score:    {total}")
print(f"   Class average:  {average:.2f}")
print()

# Compare each student against the average
print("📈 Comparison with Average:")
print("-" * 40)
for name, score in student_scores.items():
    if score > average:
        status = "📈 Above average"
    elif score < average:
        status = "📉 Below average"
    else:
        status = "➖ At average"
    print(f"   {name:<10} {score:>3}  {status}")
print()

# ============================================
# SECTION 3: FIND THE TOP SCORER (LOOP)
# ============================================

print("🏆 TOP SCORER")
print("-" * 40)

# Use a loop to find the highest score
top_name = None
top_score = -1  # Start below any possible score

for name, score in student_scores.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f"   🥇 Top scorer: {top_name} with {top_score} marks")
print()

# Bonus: find lowest scorer too
lowest_name = None
lowest_score = 101  # Start above any possible score

for name, score in student_scores.items():
    if score < lowest_score:
        lowest_score = score
        lowest_name = name

print(f"   📉 Lowest scorer: {lowest_name} with {lowest_score} marks")
print()

# ============================================
# SECTION 4: LOOK UP A STUDENT BY NAME
# ============================================

print("🔍 LOOK UP A STUDENT")
print("-" * 40)


def look_up_student(name, scores):
    """Safely look up a student's score by name."""
    # Case-insensitive lookup
    for student, score in scores.items():
        if student.lower() == name.strip().lower():
            return student, score
    return None, None


# Try some lookups
searches = ["Emma", "ben", "ZARA", "Grace"]

for query in searches:
    student, score = look_up_student(query, student_scores)
    if student:
        print(f"   ✅ '{query}' → {student} scored {score}")
    else:
        print(f"   ❌ '{query}' not found in class records")
print()

# ============================================
# SECTION 5: INTERACTIVE LOOKUP
# ============================================

print("=" * 60)
print("🔎 INTERACTIVE STUDENT LOOKUP")
print("=" * 60)
print("Type a student's name to see their score.")
print("Type 'quit' to exit.\n")

while True:
    query = input("Enter student name: ").strip()

    if query.lower() in ("quit", "exit", "q"):
        print("\n👋 Goodbye!")
        break

    if not query:
        print("   ⚠️ Please enter a name.\n")
        continue

    student, score = look_up_student(query, student_scores)

    if student:
        # Show extra context
        difference = score - average
        if score > average:
            note = f"📈 {difference:+.2f} above class average"
        elif score < average:
            note = f"📉 {difference:+.2f} below class average"
        else:
            note = "➖ Exactly at class average"

        print(f"   ✅ {student} scored {score}/100")
        print(f"      {note}\n")
    else:
        print(f"   ❌ No student named '{query}' found.")
        print(f"      Class members: {', '.join(student_scores.keys())}\n")