"""
School Snack Counter
This program demonstrates:
1. Creating snack boxes with sets
2. Adding new snacks to sets
3. Finding shared snacks (intersection)
4. Creating an array (list) of snack counts
5. Adding values to the array
6. Using count() to count occurrences
7. Using reverse() to explore the final result
"""

from array import array

# ============================================
# SECTION 1: CREATE SNACK BOXES WITH SETS
# ============================================

print("=" * 70)
print("        🍎 SCHOOL SNACK COUNTER")
print("=" * 70)
print()

# Create snack boxes for different classrooms using sets
# Sets automatically remove duplicates and are unordered
classroom_a_snacks = {"apple", "banana", "orange", "grapes", "apple"}  # Duplicate apple
classroom_b_snacks = {"banana", "chips", "cookie", "orange", "juice"}
classroom_c_snacks = {"apple", "banana", "cookie", "water", "grapes"}

print("🍱 SNACK BOXES (Sets)")
print("-" * 50)
print(f"   Classroom A: {classroom_a_snacks}")
print(f"   Classroom B: {classroom_b_snacks}")
print(f"   Classroom C: {classroom_c_snacks}")
print()

# Show that duplicates are automatically removed
print("📌 Note: 'apple' was added twice to Classroom A,")
print("   but sets automatically remove duplicates!")
print(f"   Classroom A has {len(classroom_a_snacks)} unique snacks")
print()

# ============================================
# SECTION 2: ADDING NEW SNACKS TO SETS
# ============================================

print("➕ ADDING NEW SNACKS")
print("-" * 50)

# Add a single snack using .add()
print("1. Adding a single snack:")
classroom_a_snacks.add("mango")
print(f"   ✅ Added 'mango' to Classroom A")
print(f"   Classroom A: {classroom_a_snacks}")
print()

# Trying to add a duplicate (no effect)
print("2. Adding a duplicate snack (no change):")
classroom_a_snacks.add("apple")
print(f"   ⚠️ Tried to add 'apple' again (already exists)")
print(f"   Classroom A: {classroom_a_snacks}")
print(f"   Still {len(classroom_a_snacks)} snacks")
print()

# Add multiple snacks using .update()
print("3. Adding multiple snacks at once:")
classroom_b_snacks.update(["pretzel", "yogurt", "granola"])
print(f"   ✅ Added 'pretzel', 'yogurt', 'granola' to Classroom B")
print(f"   Classroom B: {classroom_b_snacks}")
print()

# Add multiple snacks from another set
extra_snacks = {"popcorn", "trail_mix"}
classroom_c_snacks.update(extra_snacks)
print(f"4. Adding snacks from another set:")
print(f"   ✅ Added {extra_snacks} to Classroom C")
print(f"   Classroom C: {classroom_c_snacks}")
print()

# ============================================
# SECTION 3: FINDING SHARED SNACKS
# ============================================

print("🤝 FINDING SHARED SNACKS")
print("-" * 50)

# Find snacks common to ALL classrooms (intersection)
common_all = classroom_a_snacks & classroom_b_snacks & classroom_c_snacks
print("1. Snacks in ALL classrooms (intersection of all three):")
print(f"   {common_all}")
print()

# Find snacks shared between two classrooms
common_ab = classroom_a_snacks & classroom_b_snacks
print("2. Snacks shared between A and B:")
print(f"   {common_ab}")

common_bc = classroom_b_snacks & classroom_c_snacks
print("\n3. Snacks shared between B and C:")
print(f"   {common_bc}")

common_ac = classroom_a_snacks & classroom_c_snacks
print("\n4. Snacks shared between A and C:")
print(f"   {common_ac}")
print()

# Find all unique snacks across all classrooms (union)
all_snacks = classroom_a_snacks | classroom_b_snacks | classroom_c_snacks
print("5. ALL unique snacks across all classrooms (union):")
print(f"   {all_snacks}")
print(f"   Total unique snacks: {len(all_snacks)}")
print()

# Find snacks unique to each classroom (difference)
only_a = classroom_a_snacks - classroom_b_snacks - classroom_c_snacks
print("6. Snacks ONLY in Classroom A:")
print(f"   {only_a}")

only_b = classroom_b_snacks - classroom_a_snacks - classroom_c_snacks
print("\n7. Snacks ONLY in Classroom B:")
print(f"   {only_b}")

only_c = classroom_c_snacks - classroom_a_snacks - classroom_b_snacks
print("\n8. Snacks ONLY in Classroom C:")
print(f"   {only_c}")
print()

# Find snacks that are NOT shared (symmetric difference)
unique_to_one = classroom_a_snacks ^ classroom_b_snacks ^ classroom_c_snacks
print("9. Snacks NOT shared across all (symmetric difference):")
print(f"   {unique_to_one}")
print()

# ============================================
# SECTION 4: SET OPERATIONS SUMMARY
# ============================================

print("📊 SET OPERATIONS SUMMARY")
print("-" * 50)

print(f"   Classroom A: {len(classroom_a_snacks)} snacks")
print(f"   Classroom B: {len(classroom_b_snacks)} snacks")
print(f"   Classroom C: {len(classroom_c_snacks)} snacks")
print()
print(f"   Common to ALL: {len(common_all)} snacks → {common_all}")
print(f"   Shared A&B:    {len(common_ab)} snacks → {common_ab}")
print(f"   Shared B&C:    {len(common_bc)} snacks → {common_bc}")
print(f"   Shared A&C:    {len(common_ac)} snacks → {common_ac}")
print(f"   Total unique:  {len(all_snacks)} snacks")
print()

# ============================================
# SECTION 5: CREATE ARRAY OF SNACK COUNTS
# ============================================

print("📊 CREATING ARRAY OF SNACK COUNTS")
print("-" * 50)

# Create an array of snack counts per day (Monday to Friday)
# Using array module for typed arrays
daily_snack_counts = array('i', [25, 30, 22, 35, 28])

print("1. Original daily snack counts (Mon-Fri):")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day, count in zip(days, daily_snack_counts):
    print(f"   {day:<10} → {count} snacks")
print()

print(f"   Array type: {daily_snack_counts.typecode}")
print(f"   Array length: {len(daily_snack_counts)}")
print(f"   Array contents: {daily_snack_counts.tolist()}")
print()

# Create another array for a different week
week2_counts = array('i', [20, 28, 33, 27, 40])
print("2. Second week snack counts:")
for day, count in zip(days, week2_counts):
    print(f"   {day:<10} → {count} snacks")
print()

# ============================================
# SECTION 6: ADDING VALUES TO THE ARRAY
# ============================================

print("➕ ADDING VALUES TO THE ARRAY")
print("-" * 50)

# Add a single value using .append()
print("1. Adding Saturday count (15) using .append():")
daily_snack_counts.append(15)
print(f"   ✅ Added 15 snacks for Saturday")
print(f"   Array now: {daily_snack_counts.tolist()}")
print(f"   Length: {len(daily_snack_counts)}")
print()

# Add multiple values using .extend()
print("2. Adding Sunday count using .extend():")
daily_snack_counts.extend([18])
print(f"   ✅ Added 18 snacks for Sunday")
print(f"   Array now: {daily_snack_counts.tolist()}")
print()

# Insert a value at a specific position
print("3. Inserting a value at position 0:")
daily_snack_counts.insert(0, 12)
print(f"   ✅ Inserted 12 at the beginning")
print(f"   Array now: {daily_snack_counts.tolist()}")
print()

# Add more values to make it a full month (4 weeks)
print("4. Adding more weekly data:")
more_weeks = array('i', [22, 31, 26, 38, 29, 20, 15])
daily_snack_counts.extend(more_weeks)
print(f"   ✅ Added {len(more_weeks)} more values")
print(f"   Array now has {len(daily_snack_counts)} values")
print()

# ============================================
# SECTION 7: WORKING WITH THE FULL ARRAY
# ============================================

print("📈 WORKING WITH THE FULL ARRAY")
print("-" * 50)

# Convert to list for easier manipulation
all_counts = daily_snack_counts.tolist()

print(f"   Full array: {all_counts}")
print(f"   Total values: {len(all_counts)}")
print()

# Basic statistics
total = sum(all_counts)
average = total / len(all_counts)
minimum = min(all_counts)
maximum = max(all_counts)

print(f"   Total snacks: {total}")
print(f"   Average: {average:.1f}")
print(f"   Minimum: {minimum}")
print(f"   Maximum: {maximum}")
print()

# ============================================
# SECTION 8: USING COUNT()
# ============================================

print("🔢 USING count() METHOD")
print("-" * 50)

# count() on array
print("1. Using count() on array:")
print(f"   Count of 25 in array: {daily_snack_counts.count(25)}")
print(f"   Count of 30 in array: {daily_snack_counts.count(30)}")
print(f"   Count of 22 in array: {daily_snack_counts.count(22)}")
print(f"   Count of 100 (not present): {daily_snack_counts.count(100)}")
print()

# Create a list with repeated values for better count() demonstration
snack_votes = ["apple", "banana", "apple", "chips", "apple", 
               "banana", "cookie", "apple", "banana", "chips",
               "apple", "chips", "banana", "apple", "cookie"]

print("2. Using count() on a list (snack votes):")
print(f"   List: {snack_votes}")
print()

# Count each snack
unique_votes = set(snack_votes)
print("   Vote counts:")
for snack in sorted(unique_votes):
    count = snack_votes.count(snack)
    bar = "█" * count
    print(f"      {snack:<10} → {count} votes  {bar}")
print()

# Find the most popular snack
most_popular = max(unique_votes, key=lambda s: snack_votes.count(s))
least_popular = min(unique_votes, key=lambda s: snack_votes.count(s))

print(f"   🏆 Most popular: {most_popular} ({snack_votes.count(most_popular)} votes)")
print(f"   📉 Least popular: {least_popular} ({snack_votes.count(least_popular)} votes)")
print()

# Count in set operations
print("3. Using count() with sets:")
print(f"   'apple' in classroom_a: {classroom_a_snacks.count('apple') if hasattr(classroom_a_snacks, 'count') else 'N/A (set)'}")
print("   Note: Sets don't have .count() because they have unique items only")
print()

# ============================================
# SECTION 9: USING reverse()
# ============================================

print("🔄 USING reverse() METHOD")
print("-" * 50)

# Create a fresh list to demonstrate reverse()
snack_queue = ["apple", "banana", "chips", "cookie", "grapes", "mango"]

print("1. Original snack queue:")
print(f"   {snack_queue}")
print()

# Reverse the list in place
snack_queue.reverse()
print("2. After .reverse() (in-place):")
print(f"   {snack_queue}")
print()

# Reverse a copy (using slicing) to keep original
original_queue = ["apple", "banana", "chips", "cookie", "grapes"]
reversed_copy = original_queue[::-1]

print("3. Reversed copy (using slicing) - original unchanged:")
print(f"   Original:  {original_queue}")
print(f"   Reversed:  {reversed_copy}")
print()

# Reverse the array
print("4. Reversing the array:")
print(f"   Before: {daily_snack_counts.tolist()[:10]}...")
daily_snack_counts.reverse()
print(f"   After:  {daily_snack_counts.tolist()[:10]}...")
print()

# Double reverse returns to original
daily_snack_counts.reverse()
print("5. Double reverse (back to original):")
print(f"   {daily_snack_counts.tolist()[:10]}...")
print()

# ============================================
# SECTION 10: COMBINED EXAMPLE
# ============================================

print("🎯 COMBINED EXAMPLE - SNACK POPULARITY CONTEST")
print("-" * 50)

# Step 1: Create a list of all snacks brought by students
all_snacks_brought = (
    list(classroom_a_snacks) +
    list(classroom_b_snacks) +
    list(classroom_c_snacks)
)

print(f"1. All snacks brought (before counting):")
print(f"   {all_snacks_brought}")
print(f"   Total items: {len(all_snacks_brought)}")
print()

# Step 2: Count occurrences
print("2. Snack frequency:")
snack_counts = {}
for snack in all_snacks_brought:
    snack_counts[snack] = snack_counts.get(snack, 0) + 1

for snack, count in sorted(snack_counts.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"   {snack:<12} → {count}  {bar}")
print()

# Step 3: Create array of counts
count_values = array('i', list(snack_counts.values()))
print(f"3. Array of counts: {count_values.tolist()}")
print(f"   Array length: {len(count_values)}")
print()

# Step 4: Reverse the array
count_values.reverse()
print(f"4. Reversed array: {count_values.tolist()}")
print()

# Step 5: Count specific values in the array
print("5. Counting specific values in the array:")
for value in [1, 2, 3]:
    count = count_values.count(value)
    print(f"   Snacks with count {value}: {count}")
print()

# Step 6: Reverse back to original
count_values.reverse()
print(f"6. Final array (reversed back): {count_values.tolist()}")
print()

# ============================================
# SECTION 11: SUMMARY REPORT
# ============================================

print("=" * 70)
print("📋 FINAL SUMMARY REPORT")
print("=" * 70)
print()

# Build a comprehensive summary
report = f"""
╔══════════════════════════════════════════════════════════════╗
║              SCHOOL SNACK COUNTER SUMMARY                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🍱 SNACK BOXES (SETS)                                       ║
║     Classroom A: {len(classroom_a_snacks):<3} snacks{' ' * 40} ║
║     Classroom B: {len(classroom_b_snacks):<3} snacks{' ' * 40} ║
║     Classroom C: {len(classroom_c_snacks):<3} snacks{' ' * 40} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🤝 SHARED SNACKS                                            ║
║     Common to ALL: {len(common_all):<3} snacks{' ' * 37} ║
║     Shared A & B:  {len(common_ab):<3} snacks{' ' * 37} ║
║     Shared B & C:  {len(common_bc):<3} snacks{' ' * 37} ║
║     Shared A & C:  {len(common_ac):<3} snacks{' ' * 37} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  📊 ARRAY STATISTICS                                         ║
║     Total values: {len(daily_snack_counts):<3}{' ' * 41} ║
║     Total snacks: {total:<4}{' ' * 40} ║
║     Average:      {average:<6.1f}{' ' * 38} ║
║     Minimum:      {minimum:<4}{' ' * 40} ║
║     Maximum:      {maximum:<4}{' ' * 40} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🏆 TOP SNACKS                                               ║
"""

# Add top 3 snacks
top_snacks = sorted(snack_counts.items(), key=lambda x: -x[1])[:3]
for rank, (snack, count) in enumerate(top_snacks, 1):
    report += f"║     {rank}. {snack:<15} {count} time(s){' ' * 30} ║\n"

report += f"""║                                                              ║
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
    "1. CREATING SETS:",
    "   ✓ classroom = {'apple', 'banana', 'orange'}",
    "   ✓ Automatically removes duplicates",
    "   ✓ Unordered collection of unique items",
    "",
    "2. ADDING TO SETS:",
    "   ✓ set.add(item)         → Add one item",
    "   ✓ set.update([items])   → Add multiple items",
    "   ✓ set.update(other_set) → Merge sets",
    "",
    "3. SET OPERATIONS:",
    "   ✓ & (intersection)      → Common items",
    "   ✓ | (union)             → All unique items",
    "   ✓ - (difference)        → Items in first only",
    "   ✓ ^ (symmetric diff)    → Items in only one set",
    "",
    "4. CREATING ARRAYS:",
    "   ✓ from array import array",
    "   ✓ arr = array('i', [1, 2, 3])  → Typed integer array",
    "   ✓ Typecodes: 'i' (int), 'f' (float), 'd' (double)",
    "",
    "5. ADDING TO ARRAYS:",
    "   ✓ arr.append(value)      → Add one value",
    "   ✓ arr.extend([values])   → Add multiple values",
    "   ✓ arr.insert(index, val) → Insert at position",
    "",
    "6. USING count():",
    "   ✓ list.count(value)   → Count occurrences in list",
    "   ✓ arr.count(value)    → Count occurrences in array",
    "   ✓ Sets don't have count() (items are unique)",
    "",
    "7. USING reverse():",
    "   ✓ list.reverse()      → Reverse in place",
    "   ✓ arr.reverse()       → Reverse in place",
    "   ✓ list[::-1]          → Reverse into new list",
    "",
    "8. SETS vs LISTS vs ARRAYS:",
    "   ✓ Set:   Unique items, unordered, fast lookup",
    "   ✓ List:  Ordered, allows duplicates, flexible",
    "   ✓ Array: Ordered, typed (all same type), memory-efficient",
]

print("\n".join(concepts))

print("\n" + "=" * 70)
print("         🎉 SCHOOL SNACK COUNTER COMPLETE!")
print("=" * 70)
print("\n💡 KEY TAKEAWAYS:")
print("   • Sets store unique items (no duplicates)")
print("   • Use & for intersection, | for union, - for difference")
print("   • Sets are perfect for finding shared items")
print("   • Arrays store typed data efficiently")
print("   • count() tells you how many times a value appears")
print("   • reverse() flips a list or array in place")
print("   • Use [::-1] to reverse without changing original")
print("\n📌 Remember: Choose the right data structure!")
print("   • Sets for uniqueness & comparison")
print("   • Lists for ordered, flexible data")
print("   • Arrays for typed, memory-efficient data")
print("🌟 Happy snacking and coding!")
print("=" * 70)