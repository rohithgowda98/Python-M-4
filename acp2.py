"""
Weekly Habit Tracker
This program demonstrates:
1. Creating tuples to store habit information
2. Creating tuples for weekly completion records
3. Finding tuple length with len()
4. Accessing values using indexing (positive and negative)
5. Extracting sub-tuples using slicing
6. Exploring tuple immutability (why tuples can't be changed)
7. Workarounds to "update" tuples
"""

# ============================================
# SECTION 1: CREATE HABIT INFORMATION TUPLES
# ============================================

print("=" * 70)
print("        📅 WEEKLY HABIT TRACKER")
print("=" * 70)
print()

# Each habit is stored as a tuple: (name, category, target_per_week, emoji)
habit_1 = ("Drink Water", "Health", 7, "💧")
habit_2 = ("Exercise", "Fitness", 5, "🏃")
habit_3 = ("Read Books", "Learning", 4, "📚")
habit_4 = ("Meditate", "Wellness", 7, "🧘")
habit_5 = ("Journal", "Reflection", 3, "✍️")

# Store all habits in a tuple (tuple of tuples)
habits = (habit_1, habit_2, habit_3, habit_4, habit_5)

print("📋 YOUR HABITS THIS WEEK")
print("-" * 60)
print(f"{'#':<3} {'Habit':<15} {'Category':<12} {'Target':<8} {'Emoji'}")
print("-" * 60)

for i, habit in enumerate(habits, 1):
    name, category, target, emoji = habit
    print(f"{i:<3} {name:<15} {category:<12} {target}/week  {emoji}")

print()

# ============================================
# SECTION 2: CREATE WEEKLY COMPLETION RECORDS
# ============================================

print("📊 WEEKLY COMPLETION RECORDS")
print("-" * 50)

# Days of the week (as a tuple - order matters!)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Weekly records for each habit (True = completed, False = not completed)
water_record = (True, True, True, True, True, True, True)        # 7/7 - Perfect!
exercise_record = (True, False, True, True, False, True, False)  # 4/7
reading_record = (True, True, False, True, False, False, True)   # 4/7
meditation_record = (True, True, True, True, True, True, True)   # 7/7 - Perfect!
journal_record = (False, True, False, True, False, True, False)  # 3/7

print("Weekly Records (✔ = completed, ✘ = missed):")
print()

# Display as a visual tracker
print(f"{'Habit':<15} {'Mon':<5} {'Tue':<5} {'Wed':<5} {'Thu':<5} {'Fri':<5} {'Sat':<5} {'Sun':<5}")
print("-" * 60)

all_records = (water_record, exercise_record, reading_record, meditation_record, journal_record)

for habit, record in zip(habits, all_records):
    name = habit[0]
    marks = ["✔" if done else "✘" for done in record]
    print(f"{name:<15} {marks[0]:<5} {marks[1]:<5} {marks[2]:<5} {marks[3]:<5} {marks[4]:<5} {marks[5]:<5} {marks[6]:<5}")

print()

# ============================================
# SECTION 3: TUPLE LENGTH
# ============================================

print("📏 TUPLE LENGTH")
print("-" * 50)

# len() returns the number of items in a tuple
print(f"   Number of habits:           {len(habits)}")
print(f"   Days in a week:             {len(days)}")
print(f"   Water record length:        {len(water_record)}")
print(f"   Exercise record length:     {len(exercise_record)}")
print(f"   Reading record length:      {len(reading_record)}")
print(f"   Meditation record length:   {len(meditation_record)}")
print(f"   Journal record length:      {len(journal_record)}")

# Individual habit tuple length
print(f"\n   Length of habit_1 tuple:    {len(habit_1)}")
print(f"   (name, category, target, emoji) → 4 items")
print()

# ============================================
# SECTION 4: INDEXING - ACCESSING VALUES
# ============================================

print("🎯 INDEXING - ACCESSING VALUES")
print("-" * 50)

# Accessing items in a single habit tuple
print("1. Accessing Items in habit_1 (Drink Water):")
print(f"   habit_1[0] → Name:     {habit_1[0]}")
print(f"   habit_1[1] → Category: {habit_1[1]}")
print(f"   habit_1[2] → Target:   {habit_1[2]}")
print(f"   habit_1[3] → Emoji:    {habit_1[3]}")
print()

# Negative indexing
print("2. Negative Indexing (from end):")
print(f"   habit_1[-1] → Emoji:    {habit_1[-1]}")
print(f"   habit_1[-2] → Target:   {habit_1[-2]}")
print(f"   habit_1[-3] → Category: {habit_1[-3]}")
print(f"   habit_1[-4] → Name:     {habit_1[-4]}")
print()

# Accessing items in the habits tuple (tuple of tuples)
print("3. Accessing Nested Tuples:")
print(f"   habits[0]     → {habits[0]}")
print(f"   habits[0][0]  → First habit name: {habits[0][0]}")
print(f"   habits[1][0]  → Second habit name: {habits[1][0]}")
print(f"   habits[-1][0] → Last habit name: {habits[-1][0]}")
print()

# Accessing completion records
print("4. Accessing Completion Records:")
print(f"   water_record[0]  → Monday:    {water_record[0]}")
print(f"   water_record[6]  → Sunday:    {water_record[6]}")
print(f"   water_record[-1] → Last day:  {water_record[-1]}")
print(f"   days[0]          → {days[0]}: {water_record[0]}")
print(f"   days[-1]         → {days[-1]}: {water_record[-1]}")
print()

# ============================================
# SECTION 5: SLICING - EXTRACTING SUB-TUPLES
# ============================================

print("✂️ SLICING - EXTRACTING SUB-TUPLES")
print("-" * 50)

# Basic slicing
print("1. Basic Slicing of Days Tuple:")
print(f"   days[0:3]   → First 3 days:  {days[0:3]}")
print(f"   days[3:6]   → Middle 3 days: {days[3:6]}")
print(f"   days[:5]    → First 5 days:  {days[:5]}")
print(f"   days[5:]    → Last 2 days:   {days[5:]}")
print()

# Negative slicing
print("2. Negative Slicing:")
print(f"   days[-2:]   → Last 2 days:   {days[-2:]}")
print(f"   days[:-2]   → All but last 2: {days[:-2]}")
print()

# Slicing with step
print("3. Slicing with Step:")
print(f"   days[::2]   → Every 2nd day: {days[::2]}")
print(f"   days[1::2]  → Odd positions: {days[1::2]}")
print(f"   days[::-1]  → Reversed:      {days[::-1]}")
print()

# Slicing habit tuples
print("4. Slicing Habit Information:")
print(f"   habit_1[:2]  → Name & category: {habit_1[:2]}")
print(f"   habit_1[2:]  → Target & emoji:  {habit_1[2:]}")
print(f"   habit_1[1:3] → Category & target: {habit_1[1:3]}")
print()

# Slicing the habits tuple
print("5. Slicing Habits (tuple of tuples):")
print(f"   habits[:2]   → First 2 habits:")
for h in habits[:2]:
    print(f"      {h}")
print(f"   habits[-2:]  → Last 2 habits:")
for h in habits[-2:]:
    print(f"      {h}")
print()

# Slicing completion records - weekday vs weekend
print("6. Weekday vs Weekend Analysis:")
for habit, record in zip(habits, all_records):
    name = habit[0]
    weekdays = record[:5]  # Monday-Friday
    weekend = record[5:]   # Saturday-Sunday
    weekday_count = sum(weekdays)
    weekend_count = sum(weekend)
    print(f"   {name:<15} Weekdays: {weekday_count}/5  Weekend: {weekend_count}/2")

print()

# ============================================
# SECTION 6: TUPLE IMMUTABILITY
# ============================================

print("🔒 TUPLE IMMUTABILITY - WHY TUPLES CAN'T BE CHANGED")
print("-" * 60)

print("Tuples are IMMUTABLE - once created, they cannot be modified.")
print("Let's see what happens when we try to change them:\n")

# Demonstration 1: Trying to change an item
print("1. Trying to change an item in a tuple:")

try:
    habit_1[0] = "Drink More Water"  # Attempting to modify
except TypeError as e:
    print(f"   ❌ TypeError: {e}")

print()

# Demonstration 2: Trying to append
print("2. Trying to append to a tuple:")

try:
    habits.append(("Sleep Early", "Health", 7, "😴"))
except AttributeError as e:
    print(f"   ❌ AttributeError: {e}")

print()

# Demonstration 3: Trying to delete an item
print("3. Trying to delete an item from a tuple:")

try:
    del habit_1[1]
except TypeError as e:
    print(f"   ❌ TypeError: {e}")

print()

# Demonstrate that strings inside tuples are also immutable
print("4. Strings inside tuples are also immutable:")

try:
    habit_1[0][0] = "d"  # Trying to change first char of string inside tuple
except TypeError as e:
    print(f"   ❌ TypeError: {e}")

print()

# But note - if a tuple contains a mutable object (like a list), that object CAN be changed
print("5. Tuples can contain mutable objects (but this is risky):")
habit_with_list = ("Reading", ["fiction", "non-fiction"], 7)
print(f"   Original: {habit_with_list}")

# The list inside CAN be modified
habit_with_list[1].append("biography")
print(f"   After append to inner list: {habit_with_list}")
print("   ⚠️ The tuple itself didn't change, but the list inside it did!")

# But you still cannot replace the list with a new one
try:
    habit_with_list[1] = ["new", "list"]
except TypeError as e:
    print(f"   ❌ Cannot replace the list reference: {e}")

print()

# ============================================
# SECTION 7: WHY IMMUTABILITY IS USEFUL
# ============================================

print("✨ WHY TUPLE IMMUTABILITY IS USEFUL")
print("-" * 50)

print("""
Tuples being immutable provides several benefits:

   🔒 SAFETY: Data can't be accidentally changed
   ⚡ SPEED: Tuples are faster than lists
   🔑 HASHABLE: Can be used as dictionary keys
   📌 CONSTANT DATA: Perfect for fixed data like days of week
   🧵 THREAD-SAFE: Can be safely shared between threads
   📦 MEMORY EFFICIENT: Uses less memory than lists
""")

# Example: Using tuples as dictionary keys (impossible with lists)
habit_scores = {
    ("Drink Water", "Health"): 7,
    ("Exercise", "Fitness"): 5,
    ("Read Books", "Learning"): 4,
    ("Meditate", "Wellness"): 7,
    ("Journal", "Reflection"): 3
}

print("   ✅ Tuples work as dictionary keys:")
for key, value in habit_scores.items():
    print(f"      {key} → {value} days/week")

print()

# Trying the same with a list would fail
print("   ❌ Lists cannot be dictionary keys:")
try:
    list_key_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"      TypeError: {e}")

print()

# ============================================
# SECTION 8: WORKAROUNDS FOR "UPDATING" TUPLES
# ============================================

print("🔧 WORKAROUNDS FOR UPDATING TUPLES")
print("-" * 50)

print("Since tuples can't be changed, here's how to 'update' them:\n")

# Original habit
original_habit = ("Drink Water", "Health", 7, "💧")
print(f"   Original: {original_habit}")

# Method 1: Concatenation - create a new tuple
updated_habit = (original_habit[0], original_habit[1], 8, original_habit[3])
print(f"   Method 1 (rebuild): {updated_habit}")

# Method 2: Convert to list, modify, convert back to tuple
temp_list = list(original_habit)
temp_list[2] = 8  # Update target from 7 to 8
updated_habit_2 = tuple(temp_list)
print(f"   Method 2 (list round-trip): {updated_habit_2}")

# Method 3: Concatenation to add new items
extended_tuple = original_habit + ("Morning",)
print(f"   Method 3 (concatenate): {extended_tuple}")

# Method 4: Slicing + concatenation to replace middle item
new_habit = original_habit[:2] + (10,) + original_habit[3:]
print(f"   Method 4 (slice + rebuild): {new_habit}")

print()

# Practical example: update all targets to 7 for a new month
print("   📅 Practical Example - Reset All Targets to 7:")
print("   " + "-" * 45)

# Original habits
new_habits = ()
for habit in habits:
    # Rebuild each habit with target = 7
    updated = (habit[0], habit[1], 7, habit[3])
    new_habits += (updated,)

print(f"   Old habits count: {len(habits)}")
print(f"   New habits count: {len(new_habits)}")
print()

for h in new_habits:
    print(f"      {h}")

print()

# ============================================
# SECTION 9: TUPLE UNPACKING
# ============================================

print("📦 TUPLE UNPACKING")
print("-" * 50)

# Unpacking a single habit
name, category, target, emoji = habit_1
print(f"   Unpacked habit_1:")
print(f"      Name:     {name}")
print(f"      Category: {category}")
print(f"      Target:   {target}")
print(f"      Emoji:    {emoji}")
print()

# Unpacking days
mon, tue, wed, thu, fri, sat, sun = days
print(f"   Unpacked days:")
print(f"      Weekend days: {sat}, {sun}")
print()

# Unpacking with * (star) to collect remaining items
first_habit, *other_habits = habits
print(f"   First habit: {first_habit}")
print(f"   Other habits count: {len(other_habits)}")
print()

# Using * to get first and last
first, *middle, last = days
print(f"   First day: {first}")
print(f"   Middle days: {middle}")
print(f"   Last day: {last}")
print()

# ============================================
# SECTION 10: HABIT TRACKER SUMMARY
# ============================================

print("=" * 70)
print("📊 WEEKLY HABIT TRACKER SUMMARY")
print("=" * 70)
print()

# Calculate completion statistics
total_possible = 0
total_completed = 0

print("📈 COMPLETION STATISTICS")
print("-" * 60)
print(f"{'Habit':<15} {'Target':<8} {'Done':<8} {'Rate':<8} {'Status'}")
print("-" * 60)

for habit, record in zip(habits, all_records):
    name = habit[0]
    target = habit[2]
    completed = sum(record)
    
    total_possible += 7
    total_completed += completed
    
    rate = (completed / 7) * 100
    
    if rate == 100:
        status = "🏆 Perfect!"
    elif rate >= 70:
        status = "⭐ Great!"
    elif rate >= 50:
        status = "👍 Good"
    else:
        status = "💪 Keep going"
    
    print(f"{name:<15} {target}/week  {completed}/7     {rate:>5.1f}%   {status}")

print("-" * 60)
overall_rate = (total_completed / total_possible) * 100
print(f"{'OVERALL':<15} {'':<8} {total_completed}/{total_possible}   {overall_rate:>5.1f}%")
print()

# ============================================
# SECTION 11: FINAL REPORT
# ============================================

print("=" * 70)
print("📋 FINAL WEEKLY REPORT")
print("=" * 70)
print()

# Build a clean report
report = f"""
╔══════════════════════════════════════════════════════════════╗
║              WEEKLY HABIT TRACKER REPORT                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📅 Week: {days[0]} to {days[-1]:<40} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  📊 OVERALL STATISTICS                                       ║
║     Total Habits:      {len(habits):<36} ║
║     Total Days:        {len(days):<36} ║
║     Total Opportunities: {total_possible:<34} ║
║     Total Completions: {total_completed:<36} ║
║     Overall Rate:      {overall_rate:.1f}%{' ' * 32} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🏆 PERFECT HABITS (7/7):                                    ║
"""

# Add perfect habits to report
for habit, record in zip(habits, all_records):
    if sum(record) == 7:
        report += f"║     ✅ {habit[0]:<51} ║\n"

report += f"""║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  💪 HABITS NEEDING ATTENTION:                                ║
"""

# Add habits needing attention
for habit, record in zip(habits, all_records):
    completed = sum(record)
    if completed < habit[2]:  # Below target
        gap = habit[2] - completed
        report += f"║     ⚠️ {habit[0]:<20} ({gap} short of target){' ' * 15} ║\n"

report += f"""║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🔒 TUPLE IMMUTABILITY NOTE:                                 ║
║     Your habit data is stored in tuples, which cannot        ║
║     be changed directly. This ensures data integrity!        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

print(report)

# ============================================
# SECTION 12: CONCEPT SUMMARY
# ============================================

print("=" * 70)
print("🎓 KEY CONCEPTS DEMONSTRATED")
print("=" * 70)

concepts = [
    "",
    "1. CREATING TUPLES:",
    "   ✓ habit = ('Drink Water', 'Health', 7, '💧')",
    "   ✓ days = ('Monday', 'Tuesday', ...)",
    "   ✓ Nested tuples: habits = (habit_1, habit_2, ...)",
    "",
    "2. TUPLE LENGTH:",
    "   ✓ len(habits)    → Number of habits",
    "   ✓ len(water_record) → Number of days (7)",
    "",
    "3. INDEXING:",
    "   ✓ habit[0]   → First item (name)",
    "   ✓ habit[-1]  → Last item (emoji)",
    "   ✓ habits[0][0] → Nested access",
    "",
    "4. SLICING:",
    "   ✓ days[:5]   → Weekdays (Mon-Fri)",
    "   ✓ days[5:]   → Weekend (Sat-Sun)",
    "   ✓ days[::-1] → Reversed days",
    "",
    "5. TUPLE IMMUTABILITY:",
    "   ✓ Cannot modify items: tuple[0] = x  ❌",
    "   ✓ Cannot append/remove: tuple.append()  ❌",
    "   ✓ Cannot delete items: del tuple[0]  ❌",
    "   ✓ Workaround: create a new tuple",
    "",
    "6. TUPLE UNPACKING:",
    "   ✓ name, category, target, emoji = habit",
    "   ✓ first, *rest = habits",
    "   ✓ a, b, c, d, e, f, g = days",
    "",
    "7. WHY TUPLES?",
    "   ✓ Immutable → Safe from accidental changes",
    "   ✓ Hashable → Can be dictionary keys",
    "   ✓ Faster → Better performance",
    "   ✓ Fixed data → Days of week, coordinates",
]

print("\n".join(concepts))

print("\n" + "=" * 70)
print("         🎉 WEEKLY HABIT TRACKER COMPLETE!")
print("=" * 70)
print("\n💡 KEY TAKEAWAYS:")
print("   • Tuples are ordered and immutable (cannot be changed)")
print("   • Use len() to count items in a tuple")
print("   • Index with [0], [-1] for first/last items")
print("   • Slice with [start:end] to extract sub-tuples")
print("   • Unpack tuples into multiple variables")
print("   • To 'update', create a new tuple instead")
print("   • Use tuples for fixed data (days, coordinates, configs)")
print("\n📌 Remember: Tuples protect your data from change!")
print("🌟 Use tuples when data should stay constant!")
print("=" * 70)