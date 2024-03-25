# --------------------------------------------------------------------------
# This program converts a list containing duplicates to sets,
# which automatically remove the duplicates.
# Then it is converted back to a list, and the sort function is used to
# reorder the list again, as sets do not maintain the order of elements.
# --------------------------------------------------------------------------

name_number = 0

list_1 = ["Daniel", "Daniel", "Silvia", "Benjamin", "Silvia", "Benjamin", "Benjamin"]

print("\n" + "-" * 100)
print(f"Number of elements in the list before set function: {len(list_1)}\n")

duplicates = set()

for i in list_1:
	name_number += 1
	print(f"Name {name_number}: {i}")
	if list_1.count(i) > 1:
		duplicates.add(i)

print(f"\nList elements before set function: {list_1}")

print("\n" + "-" * 100)

name_number = 0

duplicates = list(duplicates)

print("\nThe duplicates are:")
for i in duplicates:
	name_number += 1
	print(f"Name {name_number}: {i} ({list_1.count(i)} times)")

print("\n" + "-" * 100)

set_without_duplicates = set(list_1)
list_without_duplicates = list(set_without_duplicates)
list_without_duplicates.sort()

print(f"\nNumber of elements in the list after set function: {len(list_without_duplicates)}\n")

name_number = 0

for i in list_without_duplicates:
	name_number += 1
	print(f"Name {name_number}: {i}")

print(f"\nList elements after set function: {list_without_duplicates}")

print("\n" + "-" * 100)
# --------------------------------------------------------------------------
