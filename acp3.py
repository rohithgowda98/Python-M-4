"""
Student Subject Record Cleaner
This program demonstrates:
1. Creating dictionaries for student records
2. Accessing values safely (get(), in, try/except)
3. Adding new records and updating existing ones
4. Removing duplicate or unwanted entries
5. Checking dictionary length with len()
6. Iterating through final records
7. Cleaning and organizing data
"""

# ============================================
# SECTION 1: CREATE INITIAL STUDENT RECORDS
# ============================================

print("=" * 70)
print("        📚 STUDENT SUBJECT RECORD CLEANER")
print("=" * 70)
print()

# Create a dictionary of student records
# Key = student name, Value = another dictionary with subject details
student_records = {
    "Aisha": {
        "math": 92,
        "science": 88,
        "english": 95,
        "history": 78
    },
    "Ben": {
        "math": 75,
        "science": 82,
        "english": 68,
        "history": 71
    },
    "Chloe": {
        "math": 88,
        "science": 94,
        "english": 91,
        "history": 87
    },
    "Daniel": {
        "math": 65,
        "science": 58,
        "english": 72,
        "history": 69
    },
    "Emma": {
        "math": 98,
        "science": 96,
        "english": 94,
        "history": 92
    }
}

print("📋 INITIAL STUDENT RECORDS")
print("-" * 60)
print(f"{'Student':<10} {'Math':<8} {'Science':<10} {'English':<10} {'History'}")
print("-" * 60)

for name, subjects in student_records.items():
    print(f"{name:<10} {subjects['math']:<8} {subjects['science']:<10} "
          f"{subjects['english']:<10} {subjects['history']}")

print()

# ============================================
# SECTION 2: SAFE VALUE ACCESS
# ============================================

print("🔍 SAFE VALUE ACCESS")
print("-" * 50)

# --- Method 1: Direct access (can crash if key missing) ---
print("1. Direct Access (risky):")
try:
    aisha_math = student_records["Aisha"]["math"]
    print(f"   Aisha's math score: {aisha_math}")
except KeyError as e:
    print(f"   ❌ KeyError: {e}")

print()

# --- Method 2: Using .get() (safe, returns None or default) ---
print("2. Using .get() (safe):")
aisha_math = student_records.get("Aisha", {}).get("math", "Not found")
print(f"   Aisha's math: {aisha_math}")

# Trying to access a non-existent student
unknown_student = student_records.get("Zara", {}).get("math", "Not found")
print(f"   Zara's math (doesn't exist): {unknown_student}")

# Trying to access a non-existent subject
unknown_subject = student_records.get("Aisha", {}).get("physics", "Not found")
print(f"   Aisha's physics (doesn't exist): {unknown_subject}")

print()

# --- Method 3: Using 'in' operator to check first ---
print("3. Using 'in' operator (safe):")
if "Ben" in student_records:
    if "math" in student_records["Ben"]:
        print(f"   Ben's math: {student_records['Ben']['math']}")
    else:
        print("   Ben has no math record")

if "Zara" in student_records:
    print(f"   Zara's record: {student_records['Zara']}")
else:
    print("   Zara is not in the records")

print()

# --- Method 4: Using try/except (explicit error handling) ---
print("4. Using try/except (explicit):")
try:
    score = student_records["Chloe"]["science"]
    print(f"   Chloe's science: {score}")
except KeyError as e:
    print(f"   ❌ Missing key: {e}")

try:
    score = student_records["Zara"]["math"]
except KeyError as e:
    print(f"   ❌ Missing key: {e}")

print()

# --- Helper function for safe access ---
def get_score(records, student, subject, default="N/A"):
    """Safely retrieve a student's subject score."""
    return records.get(student, {}).get(subject, default)

print("5. Using a Safe Access Helper Function:")
print(f"   Aisha's math:        {get_score(student_records, 'Aisha', 'math')}")
print(f"   Emma's history:      {get_score(student_records, 'Emma', 'history')}")
print(f"   Zara's math:         {get_score(student_records, 'Zara', 'math')}")
print(f"   Ben's physics:       {get_score(student_records, 'Ben', 'physics')}")
print()

# ============================================
# SECTION 3: ADDING NEW RECORDS
# ============================================

print("➕ ADDING NEW RECORDS")
print("-" * 50)

# Add a new student with all subjects
print("1. Adding new student 'Faisal':")
student_records["Faisal"] = {
    "math": 81,
    "science": 79,
    "english": 85,
    "history": 88
}
print(f"   ✅ Added Faisal with {len(student_records['Faisal'])} subjects")

# Add another student
print("\n2. Adding new student 'Grace':")
student_records["Grace"] = {
    "math": 90,
    "science": 87,
    "english": 93,
    "history": 89
}
print(f"   ✅ Added Grace with {len(student_records['Grace'])} subjects")

# Add a new subject to an existing student
print("\n3. Adding new subject 'computer' to Aisha:")
student_records["Aisha"]["computer"] = 96
print(f"   ✅ Aisha now has {len(student_records['Aisha'])} subjects")

# Add a subject to multiple students
print("\n4. Adding 'art' to multiple students:")
for student in ["Ben", "Chloe", "Daniel"]:
    student_records[student]["art"] = 85  # Temporary placeholder
print(f"   ✅ Added 'art' to Ben, Chloe, Daniel")

print()

# Show updated records
print("📋 Updated Student Records:")
print("-" * 60)
for name, subjects in student_records.items():
    print(f"   {name:<10} → {subjects}")

print()

# ============================================
# SECTION 4: UPDATING EXISTING RECORDS
# ============================================

print("✏️ UPDATING EXISTING RECORDS")
print("-" * 50)

# Update a single value
print("1. Updating Daniel's math score (65 → 72):")
old_score = student_records["Daniel"]["math"]
student_records["Daniel"]["math"] = 72
print(f"   ✅ Changed from {old_score} to {student_records['Daniel']['math']}")

# Update using .update() method
print("\n2. Updating Ben's scores using .update():")
student_records["Ben"].update({
    "math": 80,
    "science": 85,
    "english": 74
})
print(f"   ✅ Ben's updated scores: math=80, science=85, english=74")

# Update an entire record
print("\n3. Updating entire record for Daniel:")
student_records["Daniel"] = {
    "math": 78,
    "science": 82,
    "english": 79,
    "history": 75
}
print(f"   ✅ Replaced Daniel's record: {student_records['Daniel']}")

# Increment a score (bonus points)
print("\n4. Adding bonus points to Emma's scores:")
for subject in student_records["Emma"]:
    student_records["Emma"][subject] += 2
print(f"   ✅ Emma's scores after +2 bonus: {student_records['Emma']}")

print()

# ============================================
# SECTION 5: REMOVING UNWANTED ENTRIES
# ============================================

print("🗑️ REMOVING UNWANTED ENTRIES")
print("-" * 50)

# --- Remove using del ---
print("1. Removing 'history' from Ben using del:")
if "history" in student_records["Ben"]:
    del student_records["Ben"]["history"]
    print(f"   ✅ Removed history from Ben")

# --- Remove using .pop() ---
print("\n2. Removing 'art' from Chloe using .pop():")
art_score = student_records["Chloe"].pop("art", None)
print(f"   ✅ Removed art score: {art_score}")

# --- Remove using .pop() with default (safe) ---
print("\n3. Trying to remove 'physics' from Aisha (doesn't exist):")
result = student_records["Aisha"].pop("physics", "Not found")
print(f"   ✅ Result: {result} (no error!)")

# --- Remove an entire student ---
print("\n4. Removing student 'Daniel' entirely:")
if "Daniel" in student_records:
    del student_records["Daniel"]
    print(f"   ✅ Removed Daniel from records")

# --- Remove using .pop() for a student ---
print("\n5. Removing student 'Faisal' using .pop():")
faisal_record = student_records.pop("Faisal", None)
print(f"   ✅ Removed Faisal's record: {faisal_record}")

# --- Remove all students with a specific condition ---
print("\n6. Removing students with math score below 70:")
students_to_remove = [
    name for name, subjects in student_records.items()
    if subjects.get("math", 0) < 70
]

for student in students_to_remove:
    del student_records[student]
    print(f"   ✅ Removed {student} (math < 70)")

if not students_to_remove:
    print("   No students needed removal")

print()

# Show current state
print("📋 Records After Cleaning:")
print("-" * 50)
for name, subjects in student_records.items():
    print(f"   {name}: {subjects}")

print()

# ============================================
# SECTION 6: REMOVING DUPLICATES
# ============================================

print("🔄 REMOVING DUPLICATE ENTRIES")
print("-" * 50)

# Create a dict with duplicate scores (simulating dirty data)
dirty_records = {
    "Aisha": {"math": 92, "science": 88},
    "Ben": {"math": 92, "science": 88},      # Same scores as Aisha
    "Chloe": {"math": 88, "science": 94},
    "Daniel": {"math": 92, "science": 88},   # Same scores as Aisha
    "Emma": {"math": 98, "science": 96}
}

print("Original 'dirty' records:")
for name, subjects in dirty_records.items():
    print(f"   {name}: {subjects}")
print()

# Find duplicate records
def find_duplicates(records):
    """Find students with identical score records."""
    seen = {}
    duplicates = []
    
    for name, subjects in records.items():
        # Create a hashable key from the score dictionary
        score_key = tuple(sorted(subjects.items()))
        
        if score_key in seen:
            duplicates.append((name, seen[score_key]))
        else:
            seen[score_key] = name
    
    return duplicates

duplicates = find_duplicates(dirty_records)

print("Duplicate Detection:")
if duplicates:
    for dup_name, original_name in duplicates:
        print(f"   ⚠️ {dup_name} has same scores as {original_name}")
else:
    print("   ✅ No duplicates found")

print()

# Remove duplicates (keep first occurrence)
def remove_duplicates(records):
    """Remove duplicate records, keeping the first occurrence."""
    seen = set()
    cleaned = {}
    
    for name, subjects in records.items():
        score_key = tuple(sorted(subjects.items()))
        
        if score_key not in seen:
            seen.add(score_key)
            cleaned[name] = subjects
        else:
            print(f"   🗑️ Removed duplicate: {name}")
    
    return cleaned

print("Cleaning duplicates:")
cleaned_records = remove_duplicates(dirty_records)

print(f"\n   Before: {len(dirty_records)} students")
print(f"   After:  {len(cleaned_records)} students")
print()

print("Cleaned records:")
for name, subjects in cleaned_records.items():
    print(f"   {name}: {subjects}")
print()

# ============================================
# SECTION 7: CHECKING DICTIONARY LENGTH
# ============================================

print("📏 CHECKING DICTIONARY LENGTH")
print("-" * 50)

# Length of main dictionary
print(f"   Number of students: {len(student_records)}")

# Length of each student's subject dictionary
print("\n   Subjects per student:")
for name, subjects in student_records.items():
    print(f"      {name:<10} → {len(subjects)} subjects")

print()

# Length after adding more students
print("   Adding 3 more students...")
student_records["Hassan"] = {"math": 85, "science": 80, "english": 88}
student_records["Ivy"] = {"math": 91, "science": 89, "english": 94}
student_records["Jack"] = {"math": 70, "science": 72, "english": 68}

print(f"   Updated student count: {len(student_records)}")

# Length after removing
print(f"\n   Removing 'Jack'...")
student_records.pop("Jack", None)
print(f"   Student count now: {len(student_records)}")

print()

# ============================================
# SECTION 8: ITERATING THROUGH RECORDS
# ============================================

print("🔄 ITERATING THROUGH FINAL RECORDS")
print("-" * 50)

# --- Method 1: Iterate keys ---
print("1. Iterating through keys (student names):")
for student in student_records:
    print(f"   • {student}")
print()

# --- Method 2: Iterate values ---
print("2. Iterating through values (subject dictionaries):")
for subjects in student_records.values():
    print(f"   {subjects}")
print()

# --- Method 3: Iterate items (key-value pairs) ---
print("3. Iterating through items (name + subjects):")
for name, subjects in student_records.items():
    total = sum(subjects.values())
    average = total / len(subjects) if subjects else 0
    print(f"   {name:<10} → {len(subjects)} subjects, Avg: {average:.1f}")
print()

# --- Method 4: Nested iteration ---
print("4. Nested iteration (each student, each subject):")
for name, subjects in student_records.items():
    print(f"\n   {name}:")
    for subject, score in subjects.items():
        print(f"      {subject:<12} → {score}")
print()

# --- Method 5: Iterate with enumerate ---
print("5. Iterating with enumerate (numbered list):")
for i, (name, subjects) in enumerate(student_records.items(), 1):
    print(f"   {i}. {name}: {subjects}")
print()

# --- Method 6: Iterate in sorted order ---
print("6. Iterating in alphabetical order:")
for name in sorted(student_records.keys()):
    print(f"   {name}: {student_records[name]}")
print()

# --- Method 7: Iterate and filter ---
print("7. Iterating with filter (top performers):")
for name, subjects in student_records.items():
    avg = sum(subjects.values()) / len(subjects)
    if avg >= 85:
        print(f"   ⭐ {name}: Average = {avg:.1f}")
print()

# ============================================
# SECTION 9: COMPREHENSIVE SUMMARY
# ============================================

print("=" * 70)
print("📊 COMPREHENSIVE SUMMARY REPORT")
print("=" * 70)
print()

# Calculate class statistics per subject
subjects_all = set()
for subjects in student_records.values():
    subjects_all.update(subjects.keys())

subjects_all = sorted(subjects_all)

print("📈 Subject-wise Statistics:")
print("-" * 70)
print(f"{'Subject':<12} {'Count':<8} {'Total':<8} {'Average':<10} {'Highest':<10} {'Lowest'}")
print("-" * 70)

for subject in subjects_all:
    scores = [
        subjects[subject]
        for subjects in student_records.values()
        if subject in subjects
    ]
    
    if scores:
        count = len(scores)
        total = sum(scores)
        avg = total / count
        highest = max(scores)
        lowest = min(scores)
        
        print(f"{subject:<12} {count:<8} {total:<8} {avg:<10.1f} {highest:<10} {lowest}")

print()

# Student-wise summary
print("📊 Student-wise Summary:")
print("-" * 70)
print(f"{'Student':<10} {'Subjects':<10} {'Total':<8} {'Average':<10} {'Grade'}")
print("-" * 70)

for name, subjects in sorted(student_records.items()):
    if subjects:
        total = sum(subjects.values())
        avg = total / len(subjects)
        
        if avg >= 90:
            grade = "A+"
        elif avg >= 85:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"{name:<10} {len(subjects):<10} {total:<8} {avg:<10.1f} {grade}")

print()

# ============================================
# SECTION 10: FINAL REPORT CARD
# ============================================

print("=" * 70)
print("📋 FINAL CLEANED RECORDS")
print("=" * 70)
print()

report = f"""
╔══════════════════════════════════════════════════════════════╗
║            STUDENT SUBJECT RECORD CLEANER                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📊 RECORD SUMMARY                                           ║
║     Total Students:     {len(student_records):<35} ║
║     Total Subjects:     {len(subjects_all):<35} ║
║     Subjects:           {', '.join(subjects_all):<35} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🧹 CLEANING ACTIONS TAKEN                                   ║
║     ✅ Added new students (Faisal, Grace, Hassan, Ivy)      ║
║     ✅ Added new subject (computer, art)                     ║
║     ✅ Updated existing scores (Daniel, Ben)                 ║
║     ✅ Removed unwanted entries (Daniel, Faisal)             ║
║     ✅ Removed duplicates (Daniel from dirty_records)        ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🏆 TOP PERFORMER                                            ║
"""

# Find top performer
top_student = None
top_avg = 0
for name, subjects in student_records.items():
    if subjects:
        avg = sum(subjects.values()) / len(subjects)
        if avg > top_avg:
            top_avg = avg
            top_student = name

report += f"║     {top_student:<15} Average: {top_avg:.1f}{' ' * 30} ║\n"
report += f"""║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

print(report)

# ============================================
# SECTION 11: CONCEPT SUMMARY
# ============================================

print("=" * 70)
print("🎓 KEY CONCEPTS DEMONSTRATED")
print("=" * 70)

concepts = [
    "",
    "1. CREATING DICTIONARIES:",
    "   ✓ student_records = {'Aisha': {'math': 92, ...}, ...}",
    "   ✓ Nested dictionaries (dict of dicts)",
    "   ✓ Key-value pairs with meaningful keys",
    "",
    "2. SAFE VALUE ACCESS:",
    "   ✓ dict['key']           → Direct (risky - KeyError)",
    "   ✓ dict.get('key')       → Safe (returns None)",
    "   ✓ dict.get('key', def)  → Safe with default",
    "   ✓ 'key' in dict         → Check existence first",
    "   ✓ try/except KeyError   → Explicit error handling",
    "",
    "3. ADDING RECORDS:",
    "   ✓ dict['new_key'] = value        → Add new entry",
    "   ✓ dict['existing']['sub'] = val  → Add nested item",
    "   ✓ dict.update({...})             → Bulk add/update",
    "",
    "4. UPDATING RECORDS:",
    "   ✓ dict['key'] = new_value        → Replace value",
    "   ✓ dict.update({...})             → Merge updates",
    "   ✓ dict['key']['sub'] += n        → Modify nested",
    "",
    "5. REMOVING RECORDS:",
    "   ✓ del dict['key']                → Remove entry",
    "   ✓ dict.pop('key')                → Remove & return",
    "   ✓ dict.pop('key', default)       → Safe removal",
    "   ✓ dict.clear()                   → Remove all",
    "",
    "6. DICTIONARY LENGTH:",
    "   ✓ len(dict)                      → Number of keys",
    "   ✓ Nested lengths for sub-dicts",
    "",
    "7. ITERATION:",
    "   ✓ for key in dict:               → Iterate keys",
    "   ✓ for val in dict.values():      → Iterate values",
    "   ✓ for k, v in dict.items():      → Iterate pairs",
    "   ✓ Nested loops for nested dicts",
    "   ✓ enumerate() for indexed iteration",
    "   ✓ sorted() for ordered iteration",
    "",
    "8. REMOVING DUPLICATES:",
    "   ✓ Compare score tuples as keys",
    "   ✓ Use a set to track seen records",
    "   ✓ Keep first occurrence, skip rest",
]

print("\n".join(concepts))

print("\n" + "=" * 70)
print("         🎉 STUDENT RECORD CLEANER COMPLETE!")
print("=" * 70)
print("\n💡 KEY TAKEAWAYS:")
print("   • Dictionaries store key-value pairs (fast lookups)")
print("   • Use .get() or 'in' for safe access")
print("   • Add with dict[key] = value")
print("   • Update with dict.update() or direct assignment")
print("   • Remove with del or .pop() (pop is safer)")
print("   • Use len() to count keys")
print("   • Iterate with .keys(), .values(), .items()")
print("   • Nested dicts handle complex data structures")
print("\n📌 Remember: Dictionaries are mutable, ordered (Python 3.7+),")
print("   and use keys for O(1) lookups!")
print("🌟 Clean your data for accurate results!")
print("=" * 70)