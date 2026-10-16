"""
Library Book Availability Checker
This program demonstrates:
1. Pairing book names with copy counts (using zip and dict)
2. Filtering available books (using filter and comprehensions)
3. Updating late fees using map()
4. Combining values with zip()
5. Stopping the program early when a chosen book is unavailable (break)
"""

# ============================================
# SECTION 1: SETUP LIBRARY DATA
# ============================================

print("=" * 70)
print("        📚 LIBRARY BOOK AVAILABILITY CHECKER")
print("=" * 70)
print()

# Library book names and their available copies
book_names = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Harry Potter and the Sorcerer's Stone",
    "The Hobbit",
    "Fahrenheit 451",
    "Moby Dick",
    "War and Peace"
]

available_copies = [3, 0, 5, 2, 0, 7, 4, 1, 0, 2]

# Pair book names with copy counts using zip()
library_pairs = list(zip(book_names, available_copies))

print("📖 LIBRARY INVENTORY (Book → Copies)")
print("-" * 60)
print(f"{'#':<4} {'Book Title':<45} {'Copies'}")
print("-" * 60)

for i, (book, copies) in enumerate(library_pairs, 1):
    status = "✅" if copies > 0 else "❌"
    print(f"{i:<4} {status} {book:<43} {copies}")

print()

# Create a dictionary for faster lookups
library_dict = dict(library_pairs)
print(f"📊 Total books in catalog: {len(library_dict)}")
print()

# ============================================
# SECTION 2: FILTERING AVAILABLE BOOKS
# ============================================

print("🔍 FILTERING AVAILABLE BOOKS")
print("-" * 50)

# Method 1: Using filter() with a lambda function
available_books = list(filter(lambda pair: pair[1] > 0, library_pairs))

print("1. Using filter() with lambda:")
print(f"   Available books: {len(available_books)}")
for book, copies in available_books:
    print(f"      ✅ {book} ({copies} copies)")
print()

# Method 2: Using list comprehension
available_comprehension = [(book, copies) for book, copies in library_pairs if copies > 0]

print("2. Using list comprehension:")
for book, copies in available_comprehension:
    print(f"      ✅ {book} ({copies} copies)")
print()

# Method 3: Filter out unavailable books
unavailable_books = list(filter(lambda pair: pair[1] == 0, library_pairs))

print("3. Unavailable books (0 copies):")
for book, copies in unavailable_books:
    print(f"      ❌ {book}")
print()

# Method 4: Filter books with low stock (1-2 copies)
low_stock = [(book, copies) for book, copies in library_pairs if 0 < copies <= 2]

print("4. Low stock (1-2 copies):")
for book, copies in low_stock:
    print(f"      ⚠️ {book} ({copies} copies)")
print()

# Filter books with plenty of copies (5+)
well_stocked = [(book, copies) for book, copies in library_pairs if copies >= 5]

print("5. Well-stocked (5+ copies):")
for book, copies in well_stocked:
    print(f"      📚 {book} ({copies} copies)")
print()

# ============================================
# SECTION 3: USING MAP() TO UPDATE VALUES
# ============================================

print("💰 UPDATING LATE FEES USING map()")
print("-" * 50)

# Book return scenarios: days overdue for different members
member_names = ["Aisha", "Ben", "Chloe", "Daniel", "Emma"]
days_overdue = [0, 3, 7, 2, 14]

# Late fee rate: $0.50 per day
LATE_FEE_RATE = 0.50

print("1. Original days overdue:")
for member, days in zip(member_names, days_overdue):
    print(f"   {member}: {days} days overdue")
print()

# Using map() to calculate late fees
# map() applies a function to every item in an iterable
late_fees = list(map(lambda days: days * LATE_FEE_RATE, days_overdue))

print("2. Late fees calculated with map():")
for member, days, fee in zip(member_names, days_overdue, late_fees):
    print(f"   {member:<8} {days:>3} days × ${LATE_FEE_RATE} = ${fee:.2f}")
print()

# Using map() to apply a tiered discount based on days overdue
def calculate_fee(days):
    """Calculate late fee with progressive discount for long overdue items."""
    if days == 0:
        return 0.0
    elif days <= 3:
        return days * 0.50        # Standard rate
    elif days <= 7:
        return days * 0.50 * 0.90  # 10% discount for 4-7 days
    else:
        return days * 0.50 * 0.80  # 20% discount for 8+ days

adjusted_fees = list(map(calculate_fee, days_overdue))

print("3. Adjusted fees with tiered discount:")
print(f"   {'Member':<10} {'Days':<6} {'Standard':<10} {'Adjusted':<10} {'Saved'}")
print("   " + "-" * 50)
for member, days, standard, adjusted in zip(member_names, days_overdue, late_fees, adjusted_fees):
    saved = standard - adjusted
    print(f"   {member:<10} {days:<6} ${standard:<9.2f} ${adjusted:<9.2f} ${saved:.2f}")
print()

# Using map() with multiple iterables
print("4. Using map() with two iterables:")
book_fees = list(map(
    lambda book_days, rate: book_days[1] * rate,
    zip(book_names[:5], days_overdue),
    [0.50] * 5
))

for book, days, fee in zip(book_names[:5], days_overdue, book_fees):
    print(f"   {book:<45} ${fee:.2f}")
print()

# Using map() to format strings
print("5. Using map() to format display strings:")
formatted = list(map(
    lambda pair: f"'{pair[0]}' has {pair[1]} copies",
    library_pairs[:5]
))

for text in formatted:
    print(f"   {text}")
print()

# ============================================
# SECTION 4: COMBINING VALUES WITH zip()
# ============================================

print("🔗 COMBINING VALUES WITH zip()")
print("-" * 50)

# zip() pairs elements from multiple iterables
print("1. Basic zip() - two lists:")
authors = [
    "F. Scott Fitzgerald",
    "Harper Lee",
    "George Orwell",
    "Jane Austen",
    "J.D. Salinger",
    "J.K. Rowling",
    "J.R.R. Tolkien",
    "Ray Bradbury",
    "Herman Melville",
    "Leo Tolstoy"
]

book_author_pairs = list(zip(book_names, authors, available_copies))

print(f"   {'Book':<40} {'Author':<25} {'Copies'}")
print("   " + "-" * 75)
for book, author, copies in book_author_pairs[:5]:
    print(f"   {book:<40} {author:<25} {copies}")
print("   ... (showing 5 of 10)")
print()

# zip() with three lists - books, copies, and popularity
popularity_scores = [85, 92, 88, 78, 74, 98, 95, 82, 65, 70]

full_data = list(zip(book_names, authors, available_copies, popularity_scores))

print("2. Three-way zip - Book, Author, Copies, Popularity:")
print(f"   {'Book':<40} {'Copies':<8} {'Popularity'}")
print("   " + "-" * 60)
for book, author, copies, pop in full_data[:5]:
    print(f"   {book:<40} {copies:<8} {pop}%")
print()

# zip() stops at shortest iterable
print("3. zip() stops at shortest iterable:")
short_list = [1, 2, 3]
long_list = ["a", "b", "c", "d", "e"]

zipped = list(zip(short_list, long_list))
print(f"   zip([1,2,3], ['a','b','c','d','e']) = {zipped}")
print(f"   Result has only {len(zipped)} pairs (length of shorter list)")
print()

# Unzip using zip(*iterable)
print("4. Unzipping with zip(*):")
books, auths, copies, pops = zip(*full_data)
print(f"   Unzipped books: {list(books)[:3]}... ({len(books)} total)")
print(f"   Unzipped authors: {list(auths)[:2]}... ({len(auths)} total)")
print(f"   Unzipped copies: {list(copies)}")
print()

# Building a dictionary from zip
print("5. Building a dictionary from zip:")
book_popularity = dict(zip(book_names, popularity_scores))
print("   Book popularity dictionary:")
for book, pop in list(book_popularity.items())[:3]:
    print(f"      {book}: {pop}%")
print("   ...")
print()

# Combining for a summary
print("6. Comprehensive summary using zip:")
print(f"   {'Book':<35} {'Copies':<8} {'Popularity':<12} {'Status'}")
print("   " + "-" * 70)

for book, copies, pop in zip(book_names, available_copies, popularity_scores):
    if copies == 0:
        status = "❌ Out of stock"
    elif copies <= 2:
        status = "⚠️ Low stock"
    else:
        status = "✅ Available"
    print(f"   {book:<35} {copies:<8} {pop}%{' ' * 7} {status}")
print()

# ============================================
# SECTION 5: EARLY STOPPING WITH BREAK
# ============================================

print("🚪 EARLY STOPPING - BOOK AVAILABILITY CHECK")
print("-" * 50)

def check_book_availability(book_title, library):
    """
    Check if a book is available. Stops early if not.
    Returns tuple: (is_available, copies, message)
    """
    # Normalize for case-insensitive matching
    search_title = book_title.strip().lower()
    
    # Search for the book
    for book, copies in library.items():
        if book.lower() == search_title:
            if copies > 0:
                return True, copies, f"✅ '{book}' is available! ({copies} copies)"
            else:
                return False, 0, f"❌ '{book}' is currently OUT OF STOCK"
    
    # Book not found
    return False, 0, f"⚠️ '{book_title}' is not in our catalog"

print("1. Checking specific books:")
test_books = [
    "1984",
    "Moby Dick",
    "The Hobbit",
    "The Alchemist",     # Not in catalog
    "Harry Potter and the Sorcerer's Stone"
]

for title in test_books:
    available, copies, message = check_book_availability(title, library_dict)
    print(f"   {message}")
print()

# Demonstrating break in a loop
print("2. Processing requests until an unavailable book is found:")
print("   (Program stops when it encounters an unavailable book)")
print()

requested_books = [
    "The Hobbit",
    "1984",
    "Pride and Prejudice",
    "Moby Dick",            # ← This will stop the loop
    "The Great Gatsby",
    "War and Peace"
]

processed = 0
for book in requested_books:
    available, copies, message = check_book_availability(book, library_dict)
    print(f"   Request {processed + 1}: {message}")
    
    if not available:
        print(f"\n   🛑 STOPPING: '{book}' is not available.")
        print(f"   Processed {processed} available books before stopping.")
        break
    
    processed += 1

print()

# Break in a while loop
print("3. Using break in a while loop (user input simulation):")
print()

# Simulate user requests
simulated_requests = ["The Hobbit", "1984", "Moby Dick"]
request_index = 0

while request_index < len(simulated_requests):
    book = simulated_requests[request_index]
    available, copies, message = check_book_availability(book, library_dict)
    
    print(f"   Searching for: '{book}'")
    print(f"   Result: {message}")
    
    if not available:
        print(f"   🛑 Stopping search - book unavailable.")
        break
    
    request_index += 1

print()

# Using break with a condition inside the loop
print("4. Finding the first unavailable book in popular list:")
print()

popular_books = [
    ("1984", 88),
    ("Harry Potter and the Sorcerer's Stone", 98),
    ("The Hobbit", 95),
    ("Moby Dick", 65),      # ← Out of stock
    ("To Kill a Mockingbird", 92)
]

for book, popularity in popular_books:
    available, copies, message = check_book_availability(book, library_dict)
    
    print(f"   Checking: {book} (Popularity: {popularity}%)")
    
    if not available:
        print(f"   ⚠️ Popular book '{book}' is unavailable!")
        print(f"   🛑 Stopping to alert librarian.")
        break
    else:
        print(f"   ✅ Available ({copies} copies)")
print()

# ============================================
# SECTION 6: CONTINUE VS BREAK
# ============================================

print("⏭️ CONTINUE VS BREAK")
print("-" * 50)

print("1. Using CONTINUE (skip unavailable, keep going):")
print()

available_count = 0
unavailable_count = 0

for book in requested_books:
    available, copies, message = check_book_availability(book, library_dict)
    
    if not available:
        print(f"   ⏭️ Skipping '{book}' (unavailable)")
        unavailable_count += 1
        continue  # Skip to next iteration
    
    print(f"   ✅ Processing '{book}'")
    available_count += 1

print(f"\n   Processed: {available_count} available, {unavailable_count} skipped")
print()

print("2. Using BREAK (stop at first unavailable):")
print()

processed = 0
for book in requested_books:
    available, copies, message = check_book_availability(book, library_dict)
    
    if not available:
        print(f"   🛑 Stopping at '{book}' (unavailable)")
        break
    
    print(f"   ✅ Processing '{book}'")
    processed += 1

print(f"\n   Processed: {processed} books, then stopped")
print()

# ============================================
# SECTION 7: COMBINING ALL TECHNIQUES
# ============================================

print("🎯 COMBINING ALL TECHNIQUES")
print("-" * 50)

print("Scenario: Library member checking out books")
print("-" * 50)

# Member's book requests with desired quantity
member_requests = [
    ("The Hobbit", 1),
    ("1984", 2),
    ("Moby Dick", 1),        # Will stop here (0 copies)
    ("Pride and Prejudice", 1),
    ("The Great Gatsby", 1)
]

checked_out = []
total_copies_needed = 0

print("\nProcessing member requests:")

for book, quantity in member_requests:
    available, copies, message = check_book_availability(book, library_dict)
    
    print(f"\n   Request: {quantity}× '{book}'")
    
    if not available:
        print(f"   ❌ Cannot fulfill - {message}")
        print(f"   🛑 Stopping request processing")
        break
    
    if copies < quantity:
        print(f"   ⚠️ Only {copies} copies available (requested {quantity})")
        print(f"   ✅ Checking out {copies} copies")
        checked_out.append((book, copies))
        total_copies_needed += copies
    else:
        print(f"   ✅ Checking out {quantity} copies")
        checked_out.append((book, quantity))
        total_copies_needed += quantity

print("\n" + "-" * 50)
print("📋 CHECKOUT SUMMARY:")
print("-" * 50)

if checked_out:
    for book, qty in checked_out:
        print(f"   ✅ {qty}× {book}")
    print(f"\n   Total books checked out: {total_copies_needed}")
else:
    print("   No books checked out")

print()

# ============================================
# SECTION 8: LATE FEE PROCESSING WITH MAP
# ============================================

print("💰 COMPREHENSIVE LATE FEE PROCESSING")
print("-" * 50)

# Multiple members with overdue books
overdue_data = [
    ("Aisha", "The Hobbit", 5),
    ("Ben", "1984", 0),
    ("Chloe", "Pride and Prejudice", 12),
    ("Daniel", "The Great Gatsby", 3),
    ("Emma", "Harry Potter and the Sorcerer's Stone", 8),
]

print("Raw overdue data:")
for member, book, days in overdue_data:
    print(f"   {member:<8} | {book:<40} | {days} days overdue")
print()

# Extract components using zip(*)
members, books, days_list = zip(*overdue_data)

# Calculate fees using map()
def calculate_fee_with_cap(days):
    """Calculate late fee with maximum cap of $10."""
    fee = days * 0.50
    return min(fee, 10.0)  # Cap at $10

fees = list(map(calculate_fee_with_cap, days_list))

# Display combined results
print("Late fees calculated:")
print(f"   {'Member':<10} {'Book':<40} {'Days':<6} {'Fee'}")
print("   " + "-" * 65)

total_fees = 0
for member, book, days, fee in zip(members, books, days_list, fees):
    print(f"   {member:<10} {book:<40} {days:<6} ${fee:.2f}")
    total_fees += fee

print("   " + "-" * 65)
print(f"   {'TOTAL':<10} {'':<40} {'':<6} ${total_fees:.2f}")
print()

# Apply fee waiver for members with excellent history
excellent_members = {"Aisha", "Ben"}

print("After applying waivers for excellent members:")
adjusted_fees = list(map(
    lambda data: 0 if data[0] in excellent_members else calculate_fee_with_cap(data[1]),
    zip(members, days_list)
))

for member, days, original, adjusted in zip(members, days_list, fees, adjusted_fees):
    waiver = " (waived)" if original != adjusted else ""
    print(f"   {member:<10} ${original:.2f} → ${adjusted:.2f}{waiver}")

new_total = sum(adjusted_fees)
print(f"\n   Original total: ${total_fees:.2f}")
print(f"   After waivers:  ${new_total:.2f}")
print(f"   Savings:        ${total_fees - new_total:.2f}")
print()

# ============================================
# SECTION 9: FINAL REPORT
# ============================================

print("=" * 70)
print("📋 FINAL LIBRARY REPORT")
print("=" * 70)
print()

# Compile all statistics
total_books = len(library_dict)
total_copies = sum(available_copies)
available_books_count = sum(1 for c in available_copies if c > 0)
unavailable_books_count = total_books - available_books_count
avg_copies = total_copies / total_books

report = f"""
╔══════════════════════════════════════════════════════════════╗
║            LIBRARY BOOK AVAILABILITY REPORT                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📚 CATALOG STATISTICS                                       ║
║     Total Book Titles:      {total_books:<32} ║
║     Total Copies Available: {total_copies:<32} ║
║     Average Copies/Title:   {avg_copies:<32.1f} ║
║                                                              ║
║     ✅ Titles in Stock:     {available_books_count:<32} ║
║     ❌ Titles Out of Stock: {unavailable_books_count:<32} ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  🏆 MOST POPULAR (from data)                                 ║
║     Harry Potter and the Sorcerer's Stone: 98%               ║
║     The Hobbit: 95%                                          ║
║     To Kill a Mockingbird: 92%                               ║
║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  ⚠️ NEEDS RESTOCKING                                         ║
"""

# Add out-of-stock books
for book, copies in library_dict.items():
    if copies == 0:
        report += f"║     ❌ {book:<52} ║\n"

report += f"""║                                                              ║
║  ─────────────────────────────────────────────────────────   ║
║                                                              ║
║  💰 LATE FEES SUMMARY                                        ║
║     Total Fees (before waivers): ${total_fees:<27.2f} ║
║     Total Fees (after waivers):  ${new_total:<27.2f} ║
║     Total Waived:                ${total_fees - new_total:<27.2f} ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

print(report)

# ============================================
# SECTION 10: CONCEPT SUMMARY
# ============================================

print("=" * 70)
print("🎓 KEY CONCEPTS DEMONSTRATED")
print("=" * 70)

concepts = [
    "",
    "1. PAIRING WITH zip():",
    "   ✓ zip(names, copies) → Pairs items from multiple lists",
    "   ✓ dict(zip(keys, values)) → Build dictionary from pairs",
    "   ✓ zip(*pairs) → Unzip back into separate lists",
    "   ✓ Stops at shortest iterable",
    "",
    "2. FILTERING:",
    "   ✓ filter(lambda x: condition, iterable) → Keep matching items",
    "   ✓ [x for x in items if condition] → List comprehension",
    "   ✓ Filter by availability, stock level, or custom criteria",
    "",
    "3. USING map():",
    "   ✓ map(function, iterable) → Apply function to each item",
    "   ✓ Lazy evaluation (returns iterator, use list() to materialize)",
    "   ✓ Can work with multiple iterables",
    "   ✓ Common uses: transformations, calculations, formatting",
    "",
    "4. EARLY STOPPING WITH break:",
    "   ✓ break exits the loop immediately",
    "   ✓ Useful for fail-fast scenarios",
    "   ✓ 'continue' skips current iteration and continues",
    "   ✓ 'break' stops the entire loop",
    "",
    "5. COMBINING TECHNIQUES:",
    "   ✓ zip + map → Process parallel data",
    "   ✓ zip + filter → Select from paired data",
    "   ✓ zip + break → Process until condition fails",
    "   ✓ All together for complex data pipelines",
]

print("\n".join(concepts))

print("\n" + "=" * 70)
print("         🎉 LIBRARY BOOK CHECKER COMPLETE!")
print("=" * 70)
print("\n💡 KEY TAKEAWAYS:")
print("   • Use zip() to pair related data from multiple sources")
print("   • Use filter() or comprehensions to select items")
print("   • Use map() to transform each item in a collection")
print("   • Use break to stop early when a condition fails")
print("   • Use continue to skip items without stopping")
print("   • Combine techniques for powerful data processing")
print("\n📌 Remember: map() and filter() are lazy - wrap in list()")
print("   to see results immediately.")
print("🌟 Efficient data processing is key to good programs!")
print("=" * 70)