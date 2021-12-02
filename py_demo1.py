"""
py_demo1.py
11/30/2021
Connor Dupuis
"""


def compute_data(file):
    """
    Read through a file and split and strip to
    find the avg, min, and max values of
    salaries
    Also find the satisfaction of all the
    respondents in the file, return only
    the satisfied respondents
    :param file: File to read data from
    :return: Max, min, and avg salaries as floats in a tuple
    also return number of satisfied respondents
    """
    salaries = []
    satisfaction = {}
    satisfied = 0
    with open(file, encoding='utf-8') as fin:
        lines = fin.readlines()

        for line in lines[1:]:
            new_line = line.strip().split('|')
            salaries.append(float(new_line[4]))
            if str(new_line[2]) not in satisfaction:
                satisfaction[str(new_line[2])] = 0
            satisfaction[str(new_line[2])] += 1

        max_salary = max(salaries)
        min_salary = min(salaries)
        avg_salary = sum(salaries) / len(salaries)

        for key, val in satisfaction.items():
            if not key.lower().__contains__('dissatisfied'):
                satisfied += val
        return max_salary, min_salary, avg_salary, satisfied


if __name__ == "__main__":
    returned_data = compute_data('data.txt')
    print(f"Max salary: ${returned_data[0]:,.2f}"           # format to desired currency
          + f"\nMin salary: ${returned_data[1]:,.2f}"       # format to desired currency
          + f"\nAverage salary: ${returned_data[2]:,.2f}"   # format to desired currency
          + f"\nSatisfied Respondents: {returned_data[3]}")
