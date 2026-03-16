grades = [78,92,65,92,81,74,99,67,88,99]
grades.sort()
print(f"Low to High {sorted (grades)}\nthe 3 lowest grades are: {grades[0:3]}")
print(f"High to Low {sorted (grades, reverse=True)}\nthe 3 highest grades are: {grades[7:10]}")


