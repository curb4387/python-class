# Write your program here
salary = float(input("Enter the starting salary: "))
percent_increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: " ))
percent_increase = percent_increase / 100

print("")
print("Year", "%8s" % "Salary")
print("-------------")
for one_year in range(1, years + 1):
    print("%2s" % one_year, "%12s" % f"${salary:.2f}")
    salary += salary * percent_increase