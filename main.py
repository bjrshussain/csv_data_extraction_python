
"""
Read multiple CSV files to extract desired data / Filter or categorize data basen on the following.

    1. Create a CSV file that contains all employees with all their information extracted from all
        given files.
        Sort by = customer ID, ascending
        ORDER = ID, FIRST NAME, LAST NAME, SALARY, EMPLOYER, CITY

    2. Create csv file per employer, e.g. google.csv will contain list of customers that work for Google.
        Sorted by = employer name, alphabetically
        ORDER= FIRST NAME, LAST NAME, EMPLOYER. SORT

    3. Create CSV files for employees in each city, e.g. Houston.csv will contain employees from
        houston only.
        Sort by = City, alphabetically
        ORDER = ID, FIRST NAME, LAST NAME, CITY

    INPUT FILES:
        employee.csv
        employer.csv
        salaries.csv
"""

import csv


class Employee:
    def __init__(self, emp_id, first, last, city, salary=None, employer=None):
        self.id = emp_id
        self.first = first
        self.last = last
        self.city = city
        self.salary = salary
        self.employer = employer


def main():
    all_objects = []

    # READ EMPLOYEES
    with open("employee.csv", "r") as file:
        reader = csv.reader(file)
        for each in reader:
            emp_id = each[0]
            first = each[1]
            last = each[2]
            city = each[3]
            emp = Employee(emp_id=emp_id, first=first, last=last, city=city)
            all_objects.append(emp)


#     READ EMPLOYERS
    with open("employer.csv", "r") as file:
        reader = csv.reader(file)
        for each in reader:
            emp_id = each[0]
            employer = each[1]
            for emp in all_objects:
                if emp.id == emp_id:
                    emp.employer = employer

    # READ SALARY FILE
    with open("salaries.csv", "r") as f:
        reader = csv.reader(f)

        for each in reader:
            id_ = each[0]
            sal = each[1]

            for employee in all_objects:
                if employee.id == id_:
                    employee.salary = sal

# EXPORT SECTION
    def sorting_key(x):
        return x.id
    all_objects.sort(key=sorting_key)
    
#     EXPORT A CSV WITH ALL THE EMPLOYEES WITH DETAILS
    with open("details.csv", "w") as file:
        writer = csv.writer(file)
        for each in all_objects:
            row = [each.id, each.first, each.last, each.salary, each.employer, each.city]
            writer.writerow(row)

    # list of employers
    employer_list = []
    for each in all_objects:
        employer_list.append(each.employer)
    employer_list = list(set(employer_list))

    # EXPORT FILES for EACH EMPLOYER
    for each in employer_list:
        filename = each + ".csv"
        print(filename)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for item in all_objects:
                if item.employer == each:
                    row = [item.first, item.last, item.employer]
                    writer.writerow(row)

    city_list = []
    for each in all_objects:
        employer_list.append(each.city)
    city_list = list(set(employer_list))

    # EXPORT A CSV FILE BASED ON CITY
    for each in city_list:
        filename = each + ".csv"
        print(filename)
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for item in all_objects:
                if item.city == each:
                    row = [item.id, item.first, item.last, item.city]
                    writer.writerow(row)


if __name__ == "__main__":
    main()







